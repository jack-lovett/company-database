from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.address import Address, AddressCreate
from services.address import AddressService

router = APIRouter(prefix="/addresses", tags=["addresses"])


@router.post("/", response_model=Address)
def create_address(address: AddressCreate, database: Session = Depends(get_database)):
    address_service = AddressService()
    return address_service.create(database, address.dict())


@router.get("/", response_model=list[Address])
def get_addresses(database: Session = Depends(get_database)):
    address_service = AddressService()
    return address_service.get_all(database)
