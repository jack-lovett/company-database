from pydantic import BaseModel


class StaffProjectBase(BaseModel):
    staff_id: int
    project_id: int


class StaffProjectCreate(StaffProjectBase):
    pass


class StaffProjectUpdate(StaffProjectBase):
    pass


class StaffProject(StaffProjectBase):
    class Config:
        orm_mode = True
