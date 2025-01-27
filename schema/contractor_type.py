from pydantic import BaseModel
from typing import Optional

class ContractorType(BaseModel):
    contractor_type_id: int
    contractor_type: str
    contractor_type_description: Optional[str] = None

    class Config:
        orm_mode = True
