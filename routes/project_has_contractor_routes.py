from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.project_has_contractor_schema import ProjectHasContractor, ProjectHasContractorCreate
from services.project_has_contractor_service import ProjectHasContractorService

router = APIRouter(prefix="/project_has_contractors", tags=["project_has_contractors"])


@router.post("/", response_model=ProjectHasContractor)
def create_project_has_contractor(project_has_contractor: ProjectHasContractorCreate,
                                  database: Session = Depends(get_database)):
    project_has_contractor_service = ProjectHasContractorService()
    return project_has_contractor_service.create(database, project_has_contractor.dict())


@router.get("/", response_model=list[ProjectHasContractor])
def get_project_has_contractors(database: Session = Depends(get_database)):
    project_has_contractor_service = ProjectHasContractorService()
    return project_has_contractor_service.get_all(database)
