from crud.project import CRUDProject
from services.base import BaseService

class ProjectService(BaseService):
    def __init__(self):
        super().__init__(CRUDProject())