from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.contractor_type import ContractorType, ContractorTypeCreate
from services.contractor_type import ContractorTypeService

router = APIRouter(prefix="/contractor_types", tags=["contractor_types"])


@router.post("/", response_model=ContractorType)
def create_contractor_type(contractor_type: ContractorTypeCreate, database: Session = Depends(get_database)):
    contractor_type_service = ContractorTypeService()
    return contractor_type_service.create(database, contractor_type.dict())


@router.get("/", response_model=list[ContractorType])
def get_contractor_types(database: Session = Depends(get_database)):
    contractor_type_service = ContractorTypeService()
    return contractor_type_service.get_all(database)
