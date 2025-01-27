from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Contact(BaseModel):
    contact_id: int
    address_id: Optional[int] = None
    postal_address_id: Optional[int] = None
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
    contact_creation_datetime: datetime

    class Config:
        orm_mode = True
