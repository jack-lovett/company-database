
from fastapi import APIRouter, Depends, HTTPException
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

@project_router.get("/search/{first_name}", response_model=List[Project])
def get_projects_by_first_name(first_name: str, database: Session = Depends(get_database)):
    projects = project_service.get_projects_by_client_first_name(database, first_name)

    if not projects:
        raise HTTPException(status_code=404, detail="No projects found for that client")

    return projects
