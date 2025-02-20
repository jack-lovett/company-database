from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

from app.models.site_model import Site


class SoilClassBase(SQLModel):
    abbreviation: str = Field(max_length=45)
    class_: str = Field(max_length=45, sa_column_kwargs={"name": "class"})
    description: str = Field(max_length=45)


class SoilClass(SoilClassBase, table=True):
    __tablename__ = "soil_class"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationship
    sites: List[Site] = Relationship(back_populates="soil_class")


class SoilClassCreate(SoilClassBase):
    pass


class SoilClassUpdate(SoilClassBase):
    pass


class SoilClassDisplay(SoilClassBase):
    id: int
