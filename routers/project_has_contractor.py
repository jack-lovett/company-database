
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.project_has_contractor import ProjectHasContractor, ProjectHasContractorCreate, ProjectHasContractorUpdate
from services.project_has_contractor import ProjectHasContractorService
from database import get_database

project_has_contractor_router = APIRouter()

project_has_contractor_service = ProjectHasContractorService()

@project_has_contractor_router.post("/", response_model=ProjectHasContractor)
def create_project_has_contractor(obj: ProjectHasContractorCreate, database: Session = Depends(get_database)):
    return project_has_contractor_service.create(database, obj)

@project_has_contractor_router.get("/project_has_contractor_id", response_model=ProjectHasContractor)
def get_project_has_contractor(project_has_contractor_id: int, database: Session = Depends(get_database)):
    return project_has_contractor_service.get_by_id(database, project_has_contractor_id)

@project_has_contractor_router.put("/project_has_contractor_id", response_model=ProjectHasContractor)
def update_project_has_contractor(project_has_contractor_id: int, obj: ProjectHasContractorUpdate, database: Session = Depends(get_database)):
    return project_has_contractor_service.update(database, project_has_contractor_id, obj)

@project_has_contractor_router.delete("/project_has_contractor_id", response_model=ProjectHasContractor)
def delete_project_has_contractor(project_has_contractor_id: int, database: Session = Depends(get_database)):
    return project_has_contractor_service.delete(database, project_has_contractor_id)

@project_has_contractor_router.get("/", response_model=List[ProjectHasContractor])
def get_project_has_contractors(database: Session = Depends(get_database)):
    return project_has_contractor_service.get_all(database)
