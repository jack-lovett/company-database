from crud.base_crud import CRUDBase
from models.client_model import Client


class CRUDClient(CRUDBase):
    def __init__(self):
        super().__init__(Client)
