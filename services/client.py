from crud.client import CRUDClient
from services.base import BaseService


class ClientService(BaseService):
    def __init__(self):
        super().__init__(CRUDClient())
