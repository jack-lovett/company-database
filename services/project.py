from crud.project import CRUDProject
from services.address import AddressService
from services.base import BaseService
from services.client import ClientService
from services.contact import ContactService


class ProjectService(BaseService):
    def __init__(self):
        super().__init__(CRUDProject())

    def enrich_project(self, database, project):
        """Convert foreign keys into meaningful values for display."""
        project_dict = project.__dict__.copy()

        client_service = ClientService()
        contact_service = ContactService()
        address_service = AddressService()

        # Fetch client details
        client = client_service.get_by_id(database, project.client_id)
        if client:
            primary_contact = contact_service.get_by_id(database, client.primary_contact_id)
            project_dict[
                'client_name'] = f"{primary_contact.contact_first_name} {primary_contact.contact_last_name}" if primary_contact else "Unknown Client"
        else:
            project_dict['client_name'] = "Unknown Client"

        # Fetch address details
        address = address_service.get_by_id(database, project.address_id)
        if address:
            project_dict[
                'full_address'] = f"{address.address_street}, {address.address_suburb}, {address.address_city}, {address.address_state} {address.address_postal_code}"
        else:
            project_dict['full_address'] = "Unknown Address"

        return project_dict

    def get_enriched_projects(self, database):
        """Retrieve all projects with enriched values."""
        projects = self.get_all(database)
        return [self.enrich_project(database, project) for project in projects]
