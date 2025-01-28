from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.contractor_type import ContractorType, ContractorTypeCreate, ContractorTypeUpdate
from services.contractor_type import ContractorTypeService
from database import get_database

contractor_type_router = APIRouter()

contractor_type_service = ContractorTypeService()

@contractor_type_router.post("/", response_model=ContractorType)
def create_contractor_type(obj: ContractorTypeCreate, database: Session = Depends(get_database)):
    return contractor_type_service.create(database, obj)

@contractor_type_router.get("/contractor_type_id", response_model=ContractorType)
def get_contractor_type(contractor_type_id: int, database: Session = Depends(get_database)):
    return contractor_type_service.get_by_id(database, contractor_type_id)

@contractor_type_router.put("/contractor_type_id", response_model=ContractorType)
def update_contractor_type(contractor_type_id: int, obj: ContractorTypeUpdate, database: Session = Depends(get_database)):
    return contractor_type_service.update(database, contractor_type_id, obj)

@contractor_type_router.delete("/contractor_type_id", response_model=ContractorType)
def delete_contractor_type(contractor_type_id: int, database: Session = Depends(get_database)):
    return contractor_type_service.delete(database, contractor_type_id)

@contractor_type_router.get("/", response_model=List[ContractorType])
def get_contractor_types(database: Session = Depends(get_database)):
    return contractor_type_service.get_all(database)
