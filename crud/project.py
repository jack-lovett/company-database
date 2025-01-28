from crud.base import CRUDBase
from models.project import Project

class CRUDProject(CRUDBase):
    def __init__(self):
        super().__init__(Project)