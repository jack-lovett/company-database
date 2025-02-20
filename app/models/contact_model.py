from datetime import datetime
from typing import Optional, List

from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field, Relationship


class ContactBase(SQLModel):
    first_name: str = Field(max_length=45)
    last_name: str = Field(max_length=45)
    phone: Optional[str] = Field(default=None, max_length=20)
    email: Optional[str] = Field(default=None, max_length=255)
    business_name: Optional[str] = Field(default=None, max_length=255)
    abn: Optional[str] = Field(default=None, max_length=11)
    accounts_email: Optional[str] = Field(default=None, max_length=255)
    website: Optional[str] = Field(default=None, max_length=255)
    discipline: Optional[str] = Field(default=None, max_length=255)
    address_id: Optional[int] = Field(default=None, foreign_key="address.id")
    postal_address_id: Optional[int] = Field(default=None, foreign_key="address.id")
    creation_datetime: datetime = Field(default_factory=datetime.utcnow)


class Contact(ContactBase, table=True):
    __tablename__ = "contact"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    contractors: List["Contractor"] = Relationship(back_populates="contact")
    staff: List["Staff"] = Relationship(back_populates="contact")
    billing_address: Optional["Address"] = Relationship(
        back_populates="contacts_as_billing",
        sa_relationship_kwargs={
            "foreign_keys": "[Contact.address_id]",
            "overlaps": "contacts_as_postal"
        }
    )
    postal_address: Optional["Address"] = Relationship(
        back_populates="contacts_as_postal",
        sa_relationship_kwargs={
            "foreign_keys": "[Contact.postal_address_id]",
            "overlaps": "contacts_as_billing"
        }
    )
    primary_for_clients: List["Client"] = Relationship(
        back_populates="primary_contact",
        sa_relationship_kwargs={"foreign_keys": "Client.primary_contact_id"}
    )
    secondary_for_clients: List["Client"] = Relationship(
        back_populates="secondary_contact",
        sa_relationship_kwargs={"foreign_keys": "Client.secondary_contact_id"}
    )


class ContactCreate(ContactBase):
    pass


class ContactUpdate(SQLModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    business_name: Optional[str] = None
    abn: Optional[str] = None
    accounts_email: Optional[str] = None
    website: Optional[str] = None
    discipline: Optional[str] = None
    address_id: Optional[int] = None
    postal_address_id: Optional[int] = None
