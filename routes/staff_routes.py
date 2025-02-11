from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.staff_schema import Staff, StaffCreate
from services.staff_service import StaffService

router = APIRouter(prefix="/staff", tags=["staff"])


@router.post("/", response_model=Staff)
def create_staff(staff: StaffCreate, database: Session = Depends(get_database)):
    staff_service = StaffService()
    return staff_service.create(database, staff.dict())


@router.get("/", response_model=list[Staff])
def get_staff(database: Session = Depends(get_database)):
    staff_service = StaffService()
    return staff_service.get_all(database)
