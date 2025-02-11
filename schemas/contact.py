"""
Contact schema for API request/response validation.

Contains Pydantic models for contact operations:

ContactBase: Common fields for contact data
ContactCreate: Schema for creating new contacts
ContactUpdate: Schema for updating existing contacts, making required fields optional
Contact: Complete contact model including system-generated fields
These schemas ensure proper data validation and serialization between the API and database.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


#
class ContactBase(BaseModel):
    """Base class contains all fields that can be inputted by the user."""
    contact_first_name: str
    contact_last_name: str
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    contact_business_name: Optional[str] = None
    contact_abn: Optional[str] = None
    contact_accounts_email: Optional[str] = None
    contact_website: Optional[str] = None
    contact_discipline: Optional[str] = None
    address_id: Optional[int] = None
    postal_address_id: Optional[int] = None


class ContactCreate(ContactBase):
    """Create class inherits contact but serves as a clear semantic marker indicating this
    schema is specifically for creating contacts. Allows for future additions specific to creation."""
    pass


#
class ContactUpdate(ContactBase):
    """Convert required fields to optional as they are not required to change when updating."""
    contact_first_name: Optional[str] = None
    contact_last_name: Optional[str] = None


class Contact(ContactBase):
    """Inherits contactbase but adds system generated fields."""
    contact_id: int
    contact_creation_datetime: datetime

    class Config:
        from_attributes = True


class ContactDisplay(ContactBase):
    contact_id: int
    contact_first_name: str
    contact_last_name: str
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    contact_business_name: Optional[str] = None
    contact_abn: Optional[str] = None
    contact_accounts_email: Optional[str] = None
    contact_website: Optional[str] = None
    contact_discipline: Optional[str] = None
    billing_address: str
    postal_address: str
    contact_creation_datetime: datetime
