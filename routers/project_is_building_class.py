from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.project_is_building_class import ProjectIsBuildingClass, ProjectIsBuildingClassCreate, \
    ProjectIsBuildingClassUpdate
from services.project_is_building_class import ProjectIsBuildingClassService

project_is_building_class_router = APIRouter()

project_is_building_class_service = ProjectIsBuildingClassService()


@project_is_building_class_router.post("/", response_model=ProjectIsBuildingClass)
def create_project_is_building_class(obj: ProjectIsBuildingClassCreate, database: Session = Depends(get_database)):
    return project_is_building_class_service.create(database, obj)


@project_is_building_class_router.get("/project_is_building_class_id", response_model=ProjectIsBuildingClass)
def get_project_is_building_class(project_is_building_class_id: int, database: Session = Depends(get_database)):
    return project_is_building_class_service.get_by_id(database, project_is_building_class_id)


@project_is_building_class_router.put("/project_is_building_class_id", response_model=ProjectIsBuildingClass)
def update_project_is_building_class(project_is_building_class_id: int, obj: ProjectIsBuildingClassUpdate,
                                     database: Session = Depends(get_database)):
    return project_is_building_class_service.update(database, project_is_building_class_id, obj)


@project_is_building_class_router.delete("/project_is_building_class_id", response_model=ProjectIsBuildingClass)
def delete_project_is_building_class(project_is_building_class_id: int, database: Session = Depends(get_database)):
    return project_is_building_class_service.delete(database, project_is_building_class_id)


@project_is_building_class_router.get("/", response_model=List[ProjectIsBuildingClass])
def get_project_is_building_classs(database: Session = Depends(get_database)):
    return project_is_building_class_service.get_all(database)
