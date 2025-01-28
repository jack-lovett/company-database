from crud.contact import CRUDContact
from services.base import BaseService

class ContactService(BaseService):
    def __init__(self):
        super().__init__(CRUDContact())