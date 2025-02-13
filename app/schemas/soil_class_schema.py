from pydantic import BaseModel


class SoilClassBase(BaseModel):
    abbreviation: str
    class_: str
    description: str


class SoilClassCreate(SoilClassBase):
    pass


class SoilClassUpdate(SoilClassBase):
    pass


class SoilClass(SoilClassBase):
    id: int

    class Config:
        from_attributes = True
