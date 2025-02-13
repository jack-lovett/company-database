from typing import Optional

from pydantic import BaseModel


class ContractorTypeBase(BaseModel):
    type: str
    description: Optional[str] = None


class ContractorTypeCreate(ContractorTypeBase):
    pass  # No additional fields for creation


class ContractorTypeUpdate(ContractorTypeBase):
    type: Optional[str] = None


class ContractorType(ContractorTypeBase):
    id: int

    class Config:
        from_attributes = True
