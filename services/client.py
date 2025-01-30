from crud.client import CRUDClient
from services.base import BaseService
from services.contact import ContactService


class ClientService(BaseService):
    def __init__(self):
        super().__init__(CRUDClient())

    def enrich_client(self, database, client):
        """Convert foreign keys into meaningful values for display."""
        client_dict = client.__dict__.copy()

        contact_service = ContactService()

        # Fetch primary contact details
        primary_contact = contact_service.get_by_id(database, client.primary_contact_id)
        if primary_contact:
            client_dict['primary_contact_name'] = (
                f"{primary_contact.contact_first_name} {primary_contact.contact_last_name}"
            )
            client_dict['primary_contact_email'] = primary_contact.contact_email or "N/A"
            client_dict['primary_contact_phone'] = primary_contact.contact_phone or "N/A"
        else:
            client_dict['primary_contact_name'] = "Unknown Contact"
            client_dict['primary_contact_email'] = "N/A"
            client_dict['primary_contact_phone'] = "N/A"

        # Count associated projects
        client_dict['project_count'] = len(client.projects)

        return client_dict

    def get_enriched_clients(self, database):
        """Retrieve all clients with enriched values."""
        clients = self.get_all(database)
        return [self.enrich_client(database, client) for client in clients]
