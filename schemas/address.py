from enum import Enum
from typing import Optional

from pydantic import BaseModel


# Enum for Address Types
class AddressTypeEnum(str, Enum):
    billing_address = "billing_address"
    postal_address = "postal_address"

class AddressBase(BaseModel):
    address_street: str
    address_suburb: str
    address_city: str
    address_state: str
    address_postal_code: str
    address_country: str
    address_type: AddressTypeEnum


class AddressCreate(AddressBase):
    pass  # For creating a new address


class AddressUpdate(AddressBase):
    address_street: Optional[str] = None
    address_suburb: Optional[str] = None
    address_city: Optional[str] = None
    address_state: Optional[str] = None
    address_postal_code: Optional[str] = None
    address_country: Optional[str] = None
    address_type: Optional[AddressTypeEnum] = None


class Address(AddressBase):
    address_id: int

    class Config:
        from_attributes = True  # Allow pydantic to read data from SQLAlchemy model
