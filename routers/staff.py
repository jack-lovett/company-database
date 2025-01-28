
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.staff import Staff, StaffCreate, StaffUpdate
from services.staff import StaffService
from database import get_database

staff_router = APIRouter()

staff_service = StaffService()

@staff_router.post("/", response_model=Staff)
def create_staff(obj: StaffCreate, database: Session = Depends(get_database)):
    return staff_service.create(database, obj)

@staff_router.get("/staff_id", response_model=Staff)
def get_staff(staff_id: int, database: Session = Depends(get_database)):
    return staff_service.get_by_id(database, staff_id)

@staff_router.put("/staff_id", response_model=Staff)
def update_staff(staff_id: int, obj: StaffUpdate, database: Session = Depends(get_database)):
    return staff_service.update(database, staff_id, obj)

@staff_router.delete("/staff_id", response_model=Staff)
def delete_staff(staff_id: int, database: Session = Depends(get_database)):
    return staff_service.delete(database, staff_id)

@staff_router.get("/", response_model=List[Staff])
def get_staffs(database: Session = Depends(get_database)):
    return staff_service.get_all(database)
