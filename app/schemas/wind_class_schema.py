from pydantic import BaseModel


class WindClassBase(BaseModel):
    class_: str


class WindClassCreate(WindClassBase):
    pass


class WindClassUpdate(WindClassBase):
    pass


class WindClassDisplay(BaseModel):
    id: int
    class_: str


class WindClass(WindClassBase):
    id: int

    class Config:
        from_attributes = True
