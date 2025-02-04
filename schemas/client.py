"""Client schema for API request/response validation.

Contains Pydantic models for client operations:

ClientBase: Common fields for client data including primary and secondary contact relationships
ClientCreate: Schema for creating new clients
ClientUpdate: Schema for updating existing clients, making required fields optional
Client: Complete client model including system-generated fields and creation timestamp
ClientDisplay: Extended client model for displaying client information with contact details
These schemas ensure proper data validation and serialization between the API and database.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ClientBase(BaseModel):
    primary_contact_id: int
    secondary_contact_id: Optional[int] = None


class ClientCreate(ClientBase):
    pass


class ClientUpdate(ClientBase):
    primary_contact_id: Optional[int] = None
    secondary_contact_id: Optional[int] = None
    # Probably shouldn't be able to update creation time
    # client_creation_datetime: Optional[datetime] = None


class Client(ClientBase):
    client_id: int
    client_creation_datetime: datetime

    class Config:
        from_attributes = True


class ClientDisplay(BaseModel):
    client_id: int
    client_creation_datetime: datetime
    # primary_contact_id: int
    # secondary_contact_id: int
    client_name: str
    primary_contact_email: str
    primary_contact_phone: str
