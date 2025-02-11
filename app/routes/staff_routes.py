from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.staff_schema import Staff, StaffCreate
from app.services.staff_service import StaffService

router = APIRouter(prefix="/staff", tags=["staff"])


@router.post("/", response_model=Staff)
def create_staff(staff: StaffCreate, database: Session = Depends(get_database)):
    staff_service = StaffService()
    return staff_service.create(database, staff.dict())


@router.get("/", response_model=list[Staff])
def get_staff(database: Session = Depends(get_database)):
    staff_service = StaffService()
    return staff_service.get_all(database)
