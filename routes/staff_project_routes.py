from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.staff_project_schema import StaffProject, StaffProjectCreate
from services.staff_project_service import StaffProjectService

router = APIRouter(prefix="/staff_projects", tags=["staff_projects"])


@router.post("/", response_model=StaffProject)
def create_staff_project(staff_project: StaffProjectCreate, database: Session = Depends(get_database)):
    staff_project_service = StaffProjectService()
    return staff_project_service.create(database, staff_project.dict())


@router.get("/", response_model=list[StaffProject])
def get_staff_projects(database: Session = Depends(get_database)):
    staff_project_service = StaffProjectService()
    return staff_project_service.get_all(database)
