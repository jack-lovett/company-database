from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.staff_time import StaffTime, StaffTimeCreate, StaffTimeUpdate
from services.staff_time import StaffTimeService

staff_time_router = APIRouter()

staff_time_service = StaffTimeService()


@staff_time_router.post("/", response_model=StaffTime)
def create_staff_time(obj: StaffTimeCreate, database: Session = Depends(get_database)):
    return staff_time_service.create(database, obj)


@staff_time_router.get("/staff_time_id", response_model=StaffTime)
def get_staff_time(staff_time_id: int, database: Session = Depends(get_database)):
    return staff_time_service.get_by_id(database, staff_time_id)


@staff_time_router.put("/staff_time_id", response_model=StaffTime)
def update_staff_time(staff_time_id: int, obj: StaffTimeUpdate, database: Session = Depends(get_database)):
    return staff_time_service.update(database, staff_time_id, obj)


@staff_time_router.delete("/staff_time_id", response_model=StaffTime)
def delete_staff_time(staff_time_id: int, database: Session = Depends(get_database)):
    return staff_time_service.delete(database, staff_time_id)


@staff_time_router.get("/", response_model=List[StaffTime])
def get_staff_times(database: Session = Depends(get_database)):
    return staff_time_service.get_all(database)
