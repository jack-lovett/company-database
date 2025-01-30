from crud.address import CRUDAddress
from services.base import BaseService


class AddressService(BaseService):
    def __init__(self):
        super().__init__(CRUDAddress())

    def enrich_address(self, database, address):
        """Convert foreign keys into meaningful values for display."""
        address_dict = address.__dict__.copy()

        from services.contact import ContactService
        contact_service = ContactService()

        # Fetch contacts associated with the address
        billing_contacts = [contact_service.get_by_id(database, contact.contact_id) for contact in
                            address.contacts_as_billing]
        postal_contacts = [contact_service.get_by_id(database, contact.contact_id) for contact in
                           address.contacts_as_postal]

        address_dict['billing_contacts'] = [f"{contact.contact_first_name} {contact.contact_last_name}" for contact in
                                            billing_contacts if contact]
        address_dict['postal_contacts'] = [f"{contact.contact_first_name} {contact.contact_last_name}" for contact in
                                           postal_contacts if contact]

        return address_dict

    def get_enriched_addresses(self, database):
        """Retrieve all addresses with enriched values."""
        addresses = self.get_all(database)
        return [self.enrich_address(database, address) for address in addresses]
