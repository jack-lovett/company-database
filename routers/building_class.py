from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.building_class import BuildingClass, BuildingClassCreate, BuildingClassUpdate
from services.building_class import BuildingClassService

building_class_router = APIRouter()

building_class_service = BuildingClassService()


@building_class_router.post("/", response_model=BuildingClass)
def create_building_class(obj: BuildingClassCreate, database: Session = Depends(get_database)):
    return building_class_service.create(database, obj)


@building_class_router.get("/building_class_id", response_model=BuildingClass)
def get_building_class(building_class_id: int, database: Session = Depends(get_database)):
    return building_class_service.get_by_id(database, building_class_id)


@building_class_router.put("/building_class_id", response_model=BuildingClass)
def update_building_class(building_class_id: int, obj: BuildingClassUpdate, database: Session = Depends(get_database)):
    return building_class_service.update(database, building_class_id, obj)


@building_class_router.delete("/building_class_id", response_model=BuildingClass)
def delete_building_class(building_class_id: int, database: Session = Depends(get_database)):
    return building_class_service.delete(database, building_class_id)


@building_class_router.get("/", response_model=List[BuildingClass])
def get_building_classs(database: Session = Depends(get_database)):
    return building_class_service.get_all(database)
