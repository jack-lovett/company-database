from crud.address import CRUDAddress
from services.base import BaseService

class AddressService(BaseService):
    def __init__(self):
        super().__init__(CRUDAddress())