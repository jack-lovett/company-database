import importlib
from typing import Generic, TypeVar, Type, List
import inflection
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlmodel import SQLModel

from app.core.database import get_database
from app.services.base_service import BaseService

# Define generic type variables
ModelType = TypeVar("ModelType", bound=SQLModel)
ServiceType = TypeVar("ServiceType", bound=BaseService)


# Helper function to automatically determine the service class and prefix
def get_models_and_service(model: Type[ModelType]):
    model_name = model.__name__
    display_model_name = f"{model_name}Display"
    service_class_name = f"{model_name}Service"

    # Get the module path for both model and service
    model_module_path = f"app.models.{inflection.underscore(model_name)}_model"
    service_module_path = f"app.services.{inflection.underscore(model_name)}_service"

    # Import display model from same module as base model
    model_module = importlib.import_module(model_module_path)
    display_model = getattr(model_module, display_model_name)

    # Import service
    service_module = importlib.import_module(service_module_path)
    service_class = getattr(service_module, service_class_name)

    prefix = inflection.pluralize(model_name).replace("_", "-").lower()

    return service_class, display_model, prefix


class CRUDRouter(Generic[ModelType]):
    """Generates CRUD routes dynamically for a given model."""

    def __init__(self, model: Type[ModelType]):
        service_class, display_model, prefix = get_models_and_service(model)

        self.router = APIRouter(prefix=f"/{prefix}", tags=[prefix])
        self.service = service_class()

        # Dynamic routes for CRUD operations
        @self.router.post("/", response_model=model)
        def create(element: model, database: Session = Depends(get_database)):
            return self.service.create(database, element.dict())

        @self.router.get("/", response_model=List[display_model])
        def get_all(database: Session = Depends(get_database)):
            records = self.service.get_all(database)
            return [self.service.enrich_record(database, record) for record in records]

        @self.router.get("/{object_id}", response_model=model)
        def get_by_id(object_id: int, database: Session = Depends(get_database)):
            return self.service.get_by_id(database, object_id)

        @self.router.put("/{object_id}", response_model=model)
        def update(object_id: int, element: model, database: Session = Depends(get_database)):
            return self.service.update(database, object_id, element.dict())

        @self.router.delete("/{object_id}", response_model=model)
        def delete(object_id: int, database: Session = Depends(get_database)):
            return self.service.delete(database, object_id)

    def get_router(self):
        return self.router
