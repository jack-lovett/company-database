from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.soil_class_schema import SoilClass
from app.services.soil_class_service import SoilClassService

router = APIRouter(prefix="/soil-classes", tags=["soil-classes"])


@router.get("/", response_model=list[SoilClass])
def get_soil_classes(database: Session = Depends(get_database)):
    service = SoilClassService()
    return service.get_all(database)
