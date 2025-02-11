from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.building_class_schema import BuildingClass, BuildingClassCreate
from services.building_class_service import BuildingClassService

router = APIRouter(prefix="/building_classes", tags=["building_classes"])


@router.post("/", response_model=BuildingClass)
def create_building_class(building_class: BuildingClassCreate, database: Session = Depends(get_database)):
    building_class_service = BuildingClassService()
    return building_class_service.create(database, building_class.dict())


@router.get("/", response_model=list[BuildingClass])
def get_building_classes(database: Session = Depends(get_database)):
    building_class_service = BuildingClassService()
    return building_class_service.get_all(database)
