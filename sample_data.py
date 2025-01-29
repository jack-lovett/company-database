from decimal import Decimal
from sqlalchemy.orm import Session
from database import get_database
from models import Client, Contact, Address, Project, ContractorType, Contractor, ProjectHasContractor, \
    ProjectIsBuildingClass, Budget, BuildingClass, CallLog, StaffTime, StaffProject, Note, Staff
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
    """Generate and insert test client data with different primary and secondary contacts."""
    clients = []

    for contact in contacts:
        secondary_contact = random.choice([c for c in contacts if c.contact_id != contact.contact_id])

        clients.append(Client(
            primary_contact_id=contact.contact_id,
            secondary_contact_id=secondary_contact.contact_id
        ))

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


def create_staff(database: Session, number_of_records: int, contacts: list):
    """Generate and insert staff data."""
    staff_roles = ['secretary', 'director', 'building_designer', 'draftsperson', 'junior_draftsperson']
    employment_statuses = ['full_time', 'part_time', 'casual', 'not_employed']

    staff_members = [
        Staff(
            contact_id=fake.random_element(contacts).contact_id,
            staff_role=fake.random_element(staff_roles),
            staff_employment_status=fake.random_element(employment_statuses),
            staff_hire_date=fake.date_this_decade(),
            staff_notes=fake.text(max_nb_chars=200)
        )
        for _ in range(number_of_records)
    ]
    database.add_all(staff_members)
    database.commit()
    return staff_members


def create_staff_time(database: Session, number_of_records: int, staff: list, projects: list):
    """Generate and insert staff time logs."""
    staff_times = [
        StaffTime(
            staff_id=fake.random_element(staff).staff_id,
            project_id=fake.random_element(projects).project_id if random.choice([True, False]) else None,
            staff_time_description=fake.sentence(),
            staff_time_hours=random.randint(1, 8)
        )
        for _ in range(number_of_records)
    ]
    database.add_all(staff_times)
    database.commit()


def create_staff_project(database: Session, staff: list, projects: list):
    """Assign staff members to projects."""
    assignments = [
        StaffProject(
            staff_id=fake.random_element(staff).staff_id,
            project_id=fake.random_element(projects).project_id
        )
        for _ in range(len(staff))  # Assign each staff member to at least one project
    ]
    database.add_all(assignments)
    database.commit()


def create_call_logs(database: Session, number_of_records: int, clients: list, staff: list, projects: list):
    """Generate and insert call logs."""
    call_types = ['lead', 'information_request']
    call_statuses = ['follow_up', 'resolved', 'in_progress']

    call_logs = [
        CallLog(
            client_id=fake.random_element(clients).client_id,
            staff_id=fake.random_element(staff).staff_id,
            project_id=fake.random_element(projects).project_id if random.choice([True, False]) else None,
            call_log_type=fake.random_element(call_types),
            call_log_status=fake.random_element(call_statuses),
            call_log_datetime=fake.date_time_this_year(),
            call_log_description=fake.text(max_nb_chars=255)
        )
        for _ in range(number_of_records)
    ]
    database.add_all(call_logs)
    database.commit()


def create_budgets(database: Session, number_of_records: int, projects: list):
    """Generate and insert budget data."""
    budget_types = ['asset', 'liability']
    budget_statuses = ['not_invoiced', 'invoiced', 'paid', 'partially_invoiced']

    budgets = [
        Budget(
            project_id=fake.random_element(projects).project_id,
            budget_type=fake.random_element(budget_types),
            budget_status=fake.random_element(budget_statuses),
            budget_description=fake.sentence(),
            budget_estimate=round(random.uniform(1000, 50000), 2),
            budget_actual=round(random.uniform(500, 49000), 2) if random.choice([True, False]) else None
        )
        for _ in range(number_of_records)
    ]
    database.add_all(budgets)
    database.commit()


def generate_test_data(database: Session, number_of_records: int):
    """Main function to generate test data for the database."""
    try:
        # Generate base data
        addresses = create_addresses(database, number_of_records)
        contacts = create_contacts(database, number_of_records, addresses)
        clients = create_clients(database, contacts)
        projects = create_projects(database, clients, addresses)
        contractor_types = create_contractor_types(database)
        contractors = create_contractors(database, number_of_records)

        # Create staff-related data
        staff = create_staff(database, number_of_records, contacts)
        create_staff_time(database, number_of_records, staff, projects)
        create_staff_project(database, staff, projects)

        # Create other associations
        create_project_has_contractors(database, contractors, projects, contractor_types)
        create_notes(database, number_of_records, projects, clients)
        building_classes = create_building_classes(database, number_of_records)
        create_project_is_building_class(database, building_classes, projects)
        create_call_logs(database, number_of_records, clients, staff, projects)
        create_budgets(database, number_of_records, projects)

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
