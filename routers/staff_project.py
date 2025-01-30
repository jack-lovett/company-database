from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.staff_project import StaffProject, StaffProjectCreate, StaffProjectUpdate
from services.staff_project import StaffProjectService

staff_project_router = APIRouter()

staff_project_service = StaffProjectService()


@staff_project_router.post("/", response_model=StaffProject)
def create_staff_project(obj: StaffProjectCreate, database: Session = Depends(get_database)):
    return staff_project_service.create(database, obj)


@staff_project_router.get("/staff_project_id", response_model=StaffProject)
def get_staff_project(staff_project_id: int, database: Session = Depends(get_database)):
    return staff_project_service.get_by_id(database, staff_project_id)


@staff_project_router.put("/staff_project_id", response_model=StaffProject)
def update_staff_project(staff_project_id: int, obj: StaffProjectUpdate, database: Session = Depends(get_database)):
    return staff_project_service.update(database, staff_project_id, obj)


@staff_project_router.delete("/staff_project_id", response_model=StaffProject)
def delete_staff_project(staff_project_id: int, database: Session = Depends(get_database)):
    return staff_project_service.delete(database, staff_project_id)


@staff_project_router.get("/", response_model=List[StaffProject])
def get_staff_projects(database: Session = Depends(get_database)):
    return staff_project_service.get_all(database)
