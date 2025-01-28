
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.contractor import Contractor, ContractorCreate, ContractorUpdate
from services.contractor import ContractorService
from database import get_database

contractor_router = APIRouter()

contractor_service = ContractorService()

@contractor_router.post("/", response_model=Contractor)
def create_contractor(obj: ContractorCreate, database: Session = Depends(get_database)):
    return contractor_service.create(database, obj)

@contractor_router.get("/contractor_id", response_model=Contractor)
def get_contractor(contractor_id: int, database: Session = Depends(get_database)):
    return contractor_service.get_by_id(database, contractor_id)

@contractor_router.put("/contractor_id", response_model=Contractor)
def update_contractor(contractor_id: int, obj: ContractorUpdate, database: Session = Depends(get_database)):
    return contractor_service.update(database, contractor_id, obj)

@contractor_router.delete("/contractor_id", response_model=Contractor)
def delete_contractor(contractor_id: int, database: Session = Depends(get_database)):
    return contractor_service.delete(database, contractor_id)

@contractor_router.get("/", response_model=List[Contractor])
def get_contractors(database: Session = Depends(get_database)):
    return contractor_service.get_all(database)
