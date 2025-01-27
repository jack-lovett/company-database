# schemas/building_class.py
from pydantic import BaseModel
from typing import Optional

class BuildingClassBase(BaseModel):
    building_class_code: str
    building_class_description: Optional[str] = None

class BuildingClassCreate(BuildingClassBase):
    pass

class BuildingClassUpdate(BuildingClassBase):
    building_class_code: Optional[str] = None
    building_class_description: Optional[str] = None

class BuildingClass(BuildingClassBase):
    building_class_id: int

    class Config:
        from_attributes = True
