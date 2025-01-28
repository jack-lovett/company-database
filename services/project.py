from sqlalchemy.orm import Session

from crud.project import CRUDProject
from models import Contact, Client
from services.base import BaseService


class ProjectService(BaseService):
    def __init__(self):
        super().__init__(CRUDProject())

    def get_projects_by_client_first_name(self, database: Session, first_name: str):
        # Explicitly specify which contact (primary or secondary) to join with
        clients = database.query(Client) \
            .join(Contact, Contact.contact_id == Client.primary_contact_id) \
            .filter(Contact.contact_first_name.ilike(first_name)) \
            .all()

        if not clients:
            return []

        # Extract project IDs from the clients associated with the first name
        project_ids = [client.projects for client in clients]

        # Flatten the list of project IDs and return the projects
        return [project for sublist in project_ids for project in sublist]
