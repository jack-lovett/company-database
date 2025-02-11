from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.project_schema import Project, ProjectCreate, ProjectDisplay
from app.services.project_service import ProjectService

router = APIRouter(prefix="/projects", tags=["projects"])

project_service = ProjectService()


@router.post("/", response_model=Project)
def create_project(project: ProjectCreate, database: Session = Depends(get_database)):
    service = ProjectService()
    return service.create(database, project.dict())


@router.get("/", response_model=list[ProjectDisplay])
def get_projects(database: Session = Depends(get_database), skip: int = 0, limit: int = 10):
    service = ProjectService()
    return service.get_enriched_projects(database)


@router.get("/next-number")
def get_next_project_number(database: Session = Depends(get_database)):
    service = ProjectService()
    next_number = service.generate_project_number(database)
    return {"project_number": next_number}
