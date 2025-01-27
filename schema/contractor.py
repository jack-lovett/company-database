from pydantic import BaseModel

class Contractor(BaseModel):
    contractor_id: int
    contact_id: int

    class Config:
        orm_mode = True
