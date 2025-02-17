from enum import Enum
from typing import Optional

from pydantic import BaseModel


# Enum for Address Types
class AddressTypeEnum(str, Enum):
    billing_address = "billing_address"
    postal_address = "postal_address"
    shipping_address = "shipping_address"
    office_address = "office_address"


class AddressBase(BaseModel):
    street: str
    suburb: str
    city: str
    state: str
    postal_code: str
    country: str
    type: AddressTypeEnum


class AddressCreate(AddressBase):
    pass  # For creating a new address


class AddressUpdate(AddressBase):
    street: Optional[str] = None
    suburb: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    type: Optional[AddressTypeEnum] = None


class AddressDisplay(BaseModel):
    id: int
    street: str
    suburb: str
    city: str
    state: str
    postal_code: str
    country: str
    type: AddressTypeEnum


class Address(AddressBase):
    id: int
