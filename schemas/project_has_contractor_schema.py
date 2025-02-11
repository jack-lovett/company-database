from enum import Enum

from pydantic import BaseModel


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
    # In many-to-many relationship tables, we do not update, instead delete entry and create new one
    pass


class ProjectHasContractor(ProjectHasContractorBase):
    class Config:
        from_attributes = True
