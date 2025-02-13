# schemas/routes.py
from typing import Optional

from pydantic import BaseModel


class BuildingClassBase(BaseModel):
    code: str
    description: Optional[str] = None


class BuildingClassCreate(BuildingClassBase):
    pass


class BuildingClassUpdate(BuildingClassBase):
    code: Optional[str] = None
    description: Optional[str] = None


class BuildingClass(BuildingClassBase):
    id: int

    class Config:
        from_attributes = True
