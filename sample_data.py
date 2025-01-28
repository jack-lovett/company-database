from decimal import Decimal
from sqlalchemy.orm import Session
from database import get_database
from models import Client, Contact, Address, Project, ContractorType, Contractor, ProjectHasContractor, \
    ProjectIsBuildingClass, Budget, BuildingClass, CallLog, StaffTime, StaffProject, Note
from faker import Faker
from datetime import datetime
import random

fake = Faker()


def create_addresses(database: Session, number_of_records: int):
    """Generate and insert test address data."""
    addresses = [
        Address(
            address_street=fake.street_address(),
            address_suburb=fake.city(),
            address_city=fake.city(),
            address_state=fake.state(),
            address_postal_code="3433",
            address_country=fake.country(),
            address_type=fake.word(ext_word_list=["billing_address", "shipping_address"])
        )
        for _ in range(number_of_records)
    ]
    database.add_all(addresses)
    database.commit()
    return addresses


def create_contacts(database: Session, number_of_records: int, addresses: list):
    """Generate and insert test contact data."""
    contacts = [
        Contact(
            address_id=fake.random_element(addresses).address_id,
            postal_address_id=fake.random_element(addresses).address_id,
            contact_first_name=fake.first_name(),
            contact_last_name=fake.last_name(),
            contact_phone="0438910998",
            contact_email=fake.email(),
            contact_business_name=fake.company(),
            contact_abn=str(fake.random_number(11)),
            contact_accounts_email=fake.email(),
            contact_website=fake.url(),
            contact_discipline=fake.company()
        )
        for _ in range(number_of_records)
    ]
    database.add_all(contacts)
    database.commit()
    return contacts


def create_clients(database: Session, contacts: list):
    """Generate and insert test client data."""
    clients = [
        Client(
            primary_contact_id=contact.contact_id,
            secondary_contact_id=contact.contact_id
        )
        for contact in contacts
    ]
    database.add_all(clients)
    database.commit()
    return clients


def create_projects(database: Session, clients: list, addresses: list):
    """Generate and insert test project data."""
    project_statuses = ['lead', 'job', 'completed', 'no_sale']
    project_referral_sources = ['google', 'referral', 'repeat_client', 'jkc', 'smce', 'word_of_mouth', 'website']
    project_payment_bases = ['lump_sum', 'hourly_rate']

    projects = [
        Project(
            client_id=client.client_id,
            address_id=fake.random_element(addresses).address_id,
            project_status=fake.random_element(project_statuses),
            project_description=fake.text(),
            project_initial_inquiry_date=fake.date_this_decade(),
            project_start_date=fake.date_this_year(),
            project_end_date=fake.date_this_year(),
            project_storeys=random.randint(1, 3),  # Assuming a random number of storeys
            project_referral_source=fake.random_element(project_referral_sources),
            project_payment_basis=fake.random_element(project_payment_bases),
            project_creation_datetime=datetime.now()
        )
        for client in clients
    ]
    database.add_all(projects)
    database.commit()
    return projects


def create_contractor_types(database: Session):
    """Generate and insert contractor types."""
    contractor_types = [
        ContractorType(contractor_type="Electrician", contractor_type_description="Electrical work"),
        ContractorType(contractor_type="Plumber", contractor_type_description="Plumbing services"),
        ContractorType(contractor_type="Carpenter", contractor_type_description="Woodworking and carpentry"),
        ContractorType(contractor_type="Builder", contractor_type_description="General construction")
    ]
    database.add_all(contractor_types)
    database.commit()
    return contractor_types


def create_contractors(database: Session, number_of_records: int):
    """Generate and insert contractor data."""
    contractors = [
        Contractor(
            contact_id=fake.random_element([contact.contact_id for contact in database.query(Contact).all()])
        )
        for _ in range(number_of_records)
    ]
    database.add_all(contractors)
    database.commit()
    return contractors


def create_project_has_contractors(database: Session, contractors: list, projects: list, contractor_types: list):
    """Associate contractors with projects."""
    project_ids = [project.project_id for project in projects]
    for contractor in contractors:
        project_id = fake.random_element(project_ids)  # Randomly pick a project
        contractor_type_id = fake.random_element([ct.contractor_type_id for ct in contractor_types])
        project_has_contractor = ProjectHasContractor(
            project_id=project_id,
            contractor_id=contractor.contractor_id,
            contractor_type_id=contractor_type_id
        )
        database.add(project_has_contractor)
    database.commit()


def create_notes(database: Session, number_of_records: int, projects: list, clients: list):
    """Generate and insert notes for projects."""
    notes = [
        Note(
            project_id=fake.random_element([project.project_id for project in projects]),
            client_id=fake.random_element([client.client_id for client in clients]),
            note_type=fake.random_element(['comment', 'reminder', 'follow_up']),
            note_content=fake.text(max_nb_chars=200),
        )
        for _ in range(number_of_records)
    ]
    database.add_all(notes)
    database.commit()


def create_building_classes(database: Session, number_of_records: int):
    """Generate and insert building class data."""
    building_classes = [
        BuildingClass(
            building_class_code=fake.state_abbr(),  # Two-letter code for building class
            building_class_description=fake.text(max_nb_chars=255)
        )
        for _ in range(number_of_records)
    ]
    database.add_all(building_classes)
    database.commit()
    return building_classes


def create_project_is_building_class(database: Session, building_classes: list, projects: list):
    """Associate building classes with projects."""
    project_ids = [project.project_id for project in projects]
    for building_class in building_classes:
        num_associations = random.randint(1, 5)  # Random number of associations
        selected_projects = random.sample(project_ids, num_associations)
        associations = [
            ProjectIsBuildingClass(
                building_class_building_class_id=building_class.building_class_id,
                project_project_id=project_id
            )
            for project_id in selected_projects
        ]
        database.add_all(associations)
    database.commit()


def generate_test_data(database: Session, number_of_records: int):
    """Main function to generate test data for the database."""
    try:
        # Generate data
        addresses = create_addresses(database, number_of_records)
        contacts = create_contacts(database, number_of_records, addresses)
        clients = create_clients(database, contacts)
        projects = create_projects(database, clients, addresses)
        contractor_types = create_contractor_types(database)
        contractors = create_contractors(database, number_of_records)

        # Create associations
        create_project_has_contractors(database, contractors, projects, contractor_types)
        create_notes(database, number_of_records, projects, clients)
        building_classes = create_building_classes(database, number_of_records)
        create_project_is_building_class(database, building_classes, projects)

        print("Test data inserted successfully.")
    except Exception as e:
        print(f"Error generating test data: {e}")


def main():
    db = next(get_database())  # Start a session
    try:
        generate_test_data(db, 10)  # Insert 10 test data records
    finally:
        db.close()


if __name__ == "__main__":
    main()
