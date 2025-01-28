# schemas/client.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ClientBase(BaseModel):
    primary_contact_id: int
    secondary_contact_id: Optional[int] = None


class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    primary_contact_id: Optional[int] = None
    secondary_contact_id: Optional[int] = None
    client_creation_datetime: Optional[datetime] = None

class Client(ClientBase):
    client_id: int
    client_creation_datetime: datetime

    class Config:
        from_attributes = True
