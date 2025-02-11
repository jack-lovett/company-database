from app.crud.base_crud import CRUDBase
from app.models.project_model import Project


class CRUDProject(CRUDBase):
    def __init__(self):
        super().__init__(Project)
