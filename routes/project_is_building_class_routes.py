from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.project_is_building_class_schema import ProjectIsBuildingClass, ProjectIsBuildingClassCreate
from services.project_is_building_class_service import ProjectIsBuildingClassService

router = APIRouter(prefix="/project_is_building_classes", tags=["project_is_building_classes"])


@router.post("/", response_model=ProjectIsBuildingClass)
def create_project_is_building_class(project_is_building_class: ProjectIsBuildingClassCreate,
                                     database: Session = Depends(get_database)):
    project_is_building_class_service = ProjectIsBuildingClassService()
    return project_is_building_class_service.create(database, project_is_building_class.dict())


@router.get("/", response_model=list[ProjectIsBuildingClass])
def get_project_is_building_classes(database: Session = Depends(get_database)):
    project_is_building_class_service = ProjectIsBuildingClassService()
    return project_is_building_class_service.get_all(database)
