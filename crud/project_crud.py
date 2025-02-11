from crud.base_crud import CRUDBase
from models.project_model import Project


class CRUDProject(CRUDBase):
    def __init__(self):
        super().__init__(Project)
