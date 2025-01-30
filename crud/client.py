from crud.base import CRUDBase
from models.client import Client


class CRUDClient(CRUDBase):
    def __init__(self):
        super().__init__(Client)
