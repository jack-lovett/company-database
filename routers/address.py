from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database  # Import the dependency function
from schemas.address import Address, AddressCreate, AddressUpdate
from services.address import AddressService

address_router = APIRouter()

address_service = AddressService()


@address_router.post("/", response_model=Address)
def create_address(obj: AddressCreate, database: Session = Depends(get_database)):
    return address_service.create(database, obj)


@address_router.get("/address_id", response_model=Address)
def get_address(address_id: int, database: Session = Depends(get_database)):
    return address_service.get_by_id(database, address_id)


@address_router.put("/address_id", response_model=Address)
def update_address(address_id: int, obj: AddressUpdate, database: Session = Depends(get_database)):
    return address_service.update(database, address_id, obj)


@address_router.delete("/address_id", response_model=Address)
def delete_address(address_id: int, database: Session = Depends(get_database)):
    return address_service.delete(database, address_id)


@address_router.get("/", response_model=List[Address])
def get_addresses(database: Session = Depends(get_database)):
    return address_service.get_all(database)
