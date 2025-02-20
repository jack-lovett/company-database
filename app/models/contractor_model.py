from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from app.models.project_has_contractor_model import ProjectHasContractor


class ContractorBase(SQLModel):
    contact_id: int = Field(foreign_key="contact.id")


class Contractor(ContractorBase, table=True):
    __tablename__ = "contractor"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    contact: "Contact" = Relationship(back_populates="contractors")
    projects: List["Project"] = Relationship(
        back_populates="contractors",
        link_model=ProjectHasContractor
    )


class ContractorCreate(ContractorBase):
    pass


class ContractorUpdate(SQLModel):
    contact_id: Optional[int] = None

class ContractorDisplay(ContractorBase):
    id: int