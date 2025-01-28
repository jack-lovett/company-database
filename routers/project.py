
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.project import Project, ProjectCreate, ProjectUpdate
from services.project import ProjectService
from database import get_database

project_router = APIRouter()

project_service = ProjectService()

@project_router.post("/", response_model=Project)
def create_project(obj: ProjectCreate, database: Session = Depends(get_database)):
    return project_service.create(database, obj)

@project_router.get("/project_id", response_model=Project)
def get_project(project_id: int, database: Session = Depends(get_database)):
    return project_service.get_by_id(database, project_id)

@project_router.put("/project_id", response_model=Project)
def update_project(project_id: int, obj: ProjectUpdate, database: Session = Depends(get_database)):
    return project_service.update(database, project_id, obj)

@project_router.delete("/project_id", response_model=Project)
def delete_project(project_id: int, database: Session = Depends(get_database)):
    return project_service.delete(database, project_id)

@project_router.get("/", response_model=List[Project])
def get_projects(database: Session = Depends(get_database)):
    return project_service.get_all(database)
