from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.project import Project, ProjectCreate, ProjectDisplay
from services.project import ProjectService

router = APIRouter(prefix="/projects", tags=["projects"])

project_service = ProjectService()


@router.post("/", response_model=Project)
def create_project(project: ProjectCreate, db: Session = Depends(get_database)):
    service = ProjectService()
    return service.create(db, project.dict())


@router.get("/", response_model=list[ProjectDisplay])
def get_projects(database: Session = Depends(get_database), skip: int = 0, limit: int = 10):
    service = ProjectService()
    return service.get_enriched_projects(database)
