from enum import Enum
from typing import Optional, List

from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field, Relationship


class AddressType(str, Enum):
    billing_address = "billing_address"
    postal_address = "postal_address"
    shipping_address = "shipping_address"
    office_address = "office_address"


class AddressBase(SQLModel):
    street: str = Field(max_length=45)
    suburb: str = Field(max_length=45)
    city: str = Field(max_length=45)
    state: str = Field(max_length=45)
    postal_code: str = Field(max_length=4)
    country: str = Field(max_length=45)
    type: AddressType


class Address(AddressBase, table=True):
    __tablename__ = "address"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    contacts_as_billing: List["Contact"] = Relationship(
        back_populates="billing_address",
        sa_relationship_kwargs={"foreign_keys": "Contact.address_id"}
    )
    contacts_as_postal: List["Contact"] = Relationship(
        back_populates="postal_address",
        sa_relationship_kwargs={"foreign_keys": "Contact.postal_address_id"}
    )
    sites: List["Site"] = Relationship(back_populates="address")

    def __str__(self) -> str:
        return f"{self.street}, {self.suburb}, {self.city}, {self.state} {self.postal_code}"


# For API operations that don't need the ID
class AddressCreate(AddressBase):
    pass


# For partial updates
class AddressUpdate(SQLModel):
    street: Optional[str] = None
    suburb: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    type: Optional[AddressType] = None


class AddressDisplay(AddressBase):
    id: int