from typing import Optional
from sqlmodel import SQLModel, Field


class ContractorTypeBase(SQLModel):
    type: str = Field(max_length=255)
    description: Optional[str] = Field(default=None)


class ContractorType(ContractorTypeBase, table=True):
    __tablename__ = "contractor_type"
    
    id: Optional[int] = Field(default=None, primary_key=True)


class ContractorTypeCreate(ContractorTypeBase):
    pass


class ContractorTypeUpdate(SQLModel):
    type: Optional[str] = None
    description: Optional[str] = None
