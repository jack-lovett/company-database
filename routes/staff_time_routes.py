from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.staff_time_schema import StaffTime, StaffTimeCreate
from services.staff_time_service import StaffTimeService

router = APIRouter(prefix="/staff_times", tags=["staff_times"])


@router.post("/", response_model=StaffTime)
def create_staff_time(staff_time: StaffTimeCreate, database: Session = Depends(get_database)):
    staff_time_service = StaffTimeService()
    return staff_time_service.create(database, staff_time.dict())


@router.get("/", response_model=list[StaffTime])
def get_staff_times(database: Session = Depends(get_database)):
    staff_time_service = StaffTimeService()
    return staff_time_service.get_all(database)
