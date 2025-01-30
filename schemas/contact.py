from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ContactBase(BaseModel):
    contact_first_name: str
    contact_last_name: str
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    contact_business_name: Optional[str] = None
    contact_abn: Optional[str] = None
    contact_acn: Optional[str] = None
    contact_accounts_email: Optional[str] = None
    contact_website: Optional[str] = None
    contact_discipline: Optional[str] = None


class ContactCreate(ContactBase):
    address_id: Optional[int] = None
    postal_address_id: Optional[int] = None


class ContactUpdate(ContactBase):
    contact_first_name: Optional[str] = None
    contact_last_name: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    contact_business_name: Optional[str] = None
    contact_abn: Optional[str] = None
    contact_acn: Optional[str] = None
    contact_accounts_email: Optional[str] = None
    contact_website: Optional[str] = None
    contact_discipline: Optional[str] = None


class Contact(ContactBase):
    contact_id: int
    contact_creation_datetime: datetime

    class Config:
        from_attributes = True
