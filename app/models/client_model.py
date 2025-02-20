from datetime import datetime
from typing import Optional, List

from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field, Relationship


class ClientBase(SQLModel):
    primary_contact_id: int = Field(foreign_key="contact.id")
    secondary_contact_id: Optional[int] = Field(default=None, foreign_key="contact.id")
    creation_datetime: datetime = Field(default_factory=datetime.utcnow)


class Client(ClientBase, table=True):
    __tablename__ = "client"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    primary_contact: "Contact" = Relationship(
        back_populates="primary_for_clients",
        sa_relationship_kwargs={"foreign_keys": "[Client.primary_contact_id]"}
    )
    secondary_contact: Optional["Contact"] = Relationship(
        back_populates="secondary_for_clients",
        sa_relationship_kwargs={"foreign_keys": "[Client.secondary_contact_id]"}
    )
    projects: List["Project"] = Relationship(back_populates="client")
    notes: List["Note"] = Relationship(back_populates="client")
    call_logs: List["CallLog"] = Relationship(back_populates="client")


class ClientCreate(ClientBase):
    pass


class ClientUpdate(SQLModel):
    primary_contact_id: Optional[int] = None
    secondary_contact_id: Optional[int] = None


class ClientDisplay(SQLModel):
    id: int
    name: str
    creation_datetime: datetime
    primary_contact_email: str
    primary_contact_phone: str
    secondary_contact_name: Optional[str] = None
    secondary_contact_email: Optional[str] = None
    secondary_contact_phone: Optional[str] = None
