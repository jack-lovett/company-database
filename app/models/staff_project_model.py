from sqlmodel import SQLModel, Field


class StaffProject(SQLModel, table=True):
    __tablename__ = "staff_project"

    staff_id: int = Field(
        foreign_key="staff.id",
        primary_key=True
    )
    project_id: int = Field(
        foreign_key="project.id",
        primary_key=True
    )


# For API operations
class StaffProjectCreate(SQLModel):
    staff_id: int
    project_id: int


class StaffProjectDisplay(StaffProjectCreate):
    pass
