from typing import Optional

from pydantic import BaseModel


class ContractorBase(BaseModel):
    contact_id: int


class ContractorCreate(ContractorBase):
    pass  # No additional fields for creation


class ContractorUpdate(ContractorBase):
    contact_id: Optional[int] = None


class Contractor(ContractorBase):
    id: int

    class Config:
        from_attributes = True
