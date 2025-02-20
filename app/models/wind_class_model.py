from typing import Optional, List

from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field, Relationship


class WindClassBase(SQLModel):
    class_: str = Field(max_length=2, sa_column_kwargs={"name": "class"})


class WindClass(WindClassBase, table=True):
    __tablename__ = "wind_class"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationship
    sites: List["Site"] = Relationship(back_populates="wind_class")


class WindClassCreate(WindClassBase):
    pass


class WindClassUpdate(WindClassBase):
    pass


class WindClassDisplay(SQLModel):
    id: int
    class_: str
