from typing import Optional, List

from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field, Relationship


class LocalAuthorityBase(SQLModel):
    name: str = Field(max_length=45)
    website: Optional[str] = Field(default=None, max_length=45)


class LocalAuthority(LocalAuthorityBase, table=True):
    __tablename__ = "local_authority"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationship
    sites: List["Site"] = Relationship(back_populates="local_authority")


class LocalAuthorityCreate(LocalAuthorityBase):
    pass


class LocalAuthorityUpdate(LocalAuthorityBase):
    pass


class LocalAuthorityDisplay(LocalAuthorityBase):
    pass
