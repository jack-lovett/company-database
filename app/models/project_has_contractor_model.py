from sqlmodel import SQLModel, Field


class ProjectHasContractor(SQLModel, table=True):
    __tablename__ = 'project_has_contractor'

    project_id: int = Field(foreign_key="project.id", primary_key=True)
    contractor_id: int = Field(foreign_key="contractor.id", primary_key=True)
    contractor_type_id: int = Field(foreign_key="contractor_type.id")


# For API operations
class ProjectHasContractorCreate(SQLModel):
    project_id: int
    contractor_id: int
    contractor_type_id: int


class ProjectHasContractorDisplay(ProjectHasContractor):
    pass
