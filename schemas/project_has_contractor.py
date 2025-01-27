from pydantic import BaseModel
from typing import Optional
from enum import Enum


class ContractorTypeEnum(str, Enum):
    type_a = "type_a"
    type_b = "type_b"
    type_c = "type_c"


class ProjectHasContractorBase(BaseModel):
    project_id: int
    contractor_id: int
    contractor_type_id: int


class ProjectHasContractorCreate(ProjectHasContractorBase):
    pass


class ProjectHasContractorUpdate(ProjectHasContractorBase):
    contractor_type_id: Optional[int] = None


class ProjectHasContractor(ProjectHasContractorBase):
    class Config:
        from_attributes = True
