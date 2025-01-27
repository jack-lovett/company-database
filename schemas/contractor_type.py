from pydantic import BaseModel
from typing import Optional

class ContractorTypeBase(BaseModel):
    contractor_type: str
    contractor_type_description: Optional[str] = None

class ContractorTypeCreate(ContractorTypeBase):
    pass  # No additional fields for creation

class ContractorTypeUpdate(ContractorTypeBase):
    contractor_type: Optional[str] = None
    contractor_type_description: Optional[str] = None

class ContractorType(ContractorTypeBase):
    contractor_type_id: int

    class Config:
        from_attributes = True
