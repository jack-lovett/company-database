from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.wind_class_schema import WindClass
from app.services.wind_class_service import WindClassService

router = APIRouter(prefix="/wind-classes", tags=["wind-classes"])


@router.get("/", response_model=list[WindClass])
def get_wind_classes(database: Session = Depends(get_database)):
    service = WindClassService()
    return service.get_all(database)
