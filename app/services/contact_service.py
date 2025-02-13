from app.crud.contact_crud import CRUDContact
from app.services.address_service import AddressService
from app.services.base_service import BaseService


class ContactService(BaseService):
    def __init__(self):
        super().__init__(CRUDContact())

    def enrich_contact(self, database, contact):
        """Convert foreign keys into meaningful values for display."""
        contact_dict = contact.__dict__.copy()

        address_service = AddressService()

        # Fetch billing address details
        billing_address = address_service.get_by_id(database, contact.id)
        if billing_address:
            contact_dict[
                'billing_address'] = f"{billing_address.street}, {billing_address.suburb}, {billing_address.city}, {billing_address.state} {billing_address.postal_code}"
        else:
            contact_dict['billing_address'] = "No Billing Address"

        # Fetch postal address details
        postal_address = address_service.get_by_id(database, contact.postal_address_id)
        if postal_address:
            contact_dict[
                'postal_address'] = f"{postal_address.street}, {postal_address.suburb}, {postal_address.city}, {postal_address.state} {postal_address.postal_code}"
        else:
            contact_dict['postal_address'] = "No Postal Address"

        return contact_dict

    def get_enriched_contacts(self, database):
        """Retrieve all contacts with enriched values."""
        contacts = self.get_all(database)
        return [self.enrich_contact(database, contact) for contact in contacts]
