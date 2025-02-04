from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.contractor import Contractor, ContractorCreate
from services.contractor import ContractorService

router = APIRouter(prefix="/contractors", tags=["contractors"])


@router.post("/", response_model=Contractor)
def create_contractor(contractor: ContractorCreate, database: Session = Depends(get_database)):
    contractor_service = ContractorService()
    return contractor_service.create(database, contractor.dict())


@router.get("/", response_model=list[Contractor])
def get_contractors(database: Session = Depends(get_database)):
    contractor_service = ContractorService()
    return contractor_service.get_all(database)
