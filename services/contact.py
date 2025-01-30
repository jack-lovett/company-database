from crud.contact import CRUDContact
from services.address import AddressService
from services.base import BaseService


class ContactService(BaseService):
    def __init__(self):
        super().__init__(CRUDContact())

    def enrich_contact(self, database, contact):
        """Convert foreign keys into meaningful values for display."""
        contact_dict = contact.__dict__.copy()

        address_service = AddressService()

        # Fetch billing address details
        billing_address = address_service.get_by_id(database, contact.address_id)
        if billing_address:
            contact_dict[
                'billing_address'] = f"{billing_address.address_street}, {billing_address.address_suburb}, {billing_address.address_city}, {billing_address.address_state} {billing_address.address_postal_code}"
        else:
            contact_dict['billing_address'] = "No Billing Address"

        # Fetch postal address details
        postal_address = address_service.get_by_id(database, contact.postal_address_id)
        if postal_address:
            contact_dict[
                'postal_address'] = f"{postal_address.address_street}, {postal_address.address_suburb}, {postal_address.address_city}, {postal_address.address_state} {postal_address.address_postal_code}"
        else:
            contact_dict['postal_address'] = "No Postal Address"

        return contact_dict

    def get_enriched_contacts(self, database):
        """Retrieve all contacts with enriched values."""
        contacts = self.get_all(database)
        return [self.enrich_contact(database, contact) for contact in contacts]
