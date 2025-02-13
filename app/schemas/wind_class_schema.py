from pydantic import BaseModel


class WindClassBase(BaseModel):
    class_: str


class WindClassCreate(WindClassBase):
    pass


class WindClassUpdate(WindClassBase):
    pass


class WindClass(WindClassBase):
    id: int

    class Config:
        from_attributes = True
