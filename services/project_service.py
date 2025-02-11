from datetime import datetime

from crud.project_crud import CRUDProject
from services.address_service import AddressService
from services.base_service import BaseService
from services.client_service import ClientService
from services.contact_service import ContactService


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

    def generate_project_number(self, database) -> int:
        """Generate a unique project number based on year and sequence.
        Format: YYYY###, e.g., 2025001, 2025002, etc."""
        current_year = datetime.now().year

        # Get all projects
        all_projects = self.crud.get_all(database)
        if not all_projects:
            # First project ever
            return current_year * 1000 + 1

        # Filter projects for current year
        current_year_projects = [
            project for project in all_projects
            if project.project_number // 1000 == current_year
        ]

        if not current_year_projects:
            # First project of the year
            return current_year * 1000 + 1

        # Get highest number for current year and increment
        highest_number = max(project.project_number for project in current_year_projects)
        return highest_number + 1

    def create(self, database, data):
        """Create a new project with an automatically generated project number."""
        if isinstance(data, dict):
            data['project_number'] = self.generate_project_number(database)
        else:
            data.project_number = self.generate_project_number(database)
        return super().create(database, data)
