from pydantic import BaseModel


class SoilClassBase(BaseModel):
    abbreviation: str
    class_: str
    description: str


class SoilClassCreate(SoilClassBase):
    pass


class SoilClassUpdate(SoilClassBase):
    pass


class SoilClassDisplay(BaseModel):
    id: int
    abbreviation: str
    class_: str
    description: str


class SoilClass(SoilClassBase):
    id: int

    class Config:
        from_attributes = True
