import random
from datetime import datetime

from faker import Faker
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.models import Client, Contact, Address, ContractorType, Contractor, ProjectHasContractor, \
    ProjectIsBuildingClass, Budget, BuildingClass, CallLog, StaffTime, StaffProject, Note, Staff
from app.services.project_service import ProjectService

fake = Faker()


def create_addresses(database: Session, number_of_records: int):
    """Generate and insert test address data."""
    addresses = [
        Address(
            street=fake.street_address(),
            suburb=fake.city(),
            city=fake.city(),
            state=fake.state(),
            postal_code="3433",
            country=fake.country(),
            type=fake.word(
                ext_word_list=["billing_address", "postal_address", "shipping_address", "office_address"])
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
            address_id=fake.random_element(addresses).id,
            postal_address_id=fake.random_element(addresses).id,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone="0438910998",
            email=fake.email(),
            business_name=fake.company(),
            abn=str(fake.random_number(11)),
            accounts_email=fake.email(),
            website=fake.url(),
            discipline=fake.company()
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
        secondary_contact = random.choice([c for c in contacts if c.id != contact.id])

        clients.append(Client(
            primary_contact_id=contact.id,
            secondary_contact_id=secondary_contact.id
        ))

    database.add_all(clients)
    database.commit()
    return clients


def create_projects(database: Session, clients: list, addresses: list):
    """Generate and insert test project data using ProjectService."""
    project_service = ProjectService()
    project_statuses = ['lead', 'job', 'completed', 'no_sale']
    project_referral_sources = ['google', 'referral', 'repeat_client', 'jkc', 'smce', 'word_of_mouth', 'website']
    project_payment_bases = ['lump_sum', 'hourly_rate']

    projects = []
    for client in clients:
        project_dict = {
            'client_id': client.id,
            'address_id': fake.random_element(addresses).id,
            'status': fake.random_element(project_statuses),
            'description': fake.text(),
            'initial_inquiry_date': fake.date_this_decade(),
            'start_date': fake.date_this_year(),
            'end_date': fake.date_this_year(),
            'storeys': random.randint(1, 3),
            'referral_source': fake.random_element(project_referral_sources),
            'payment_basis': fake.random_element(project_payment_bases),
            'creation_datetime': datetime.now()
        }

        created_project = project_service.create(database, project_dict)
        projects.append(created_project)

    return projects


def create_contractor_types(database: Session):
    """Generate and insert contractor types."""
    contractor_types = [
        ContractorType(type="Electrician", description="Electrical work"),
        ContractorType(type="Plumber", description="Plumbing services"),
        ContractorType(type="Carpenter", description="Woodworking and carpentry"),
        ContractorType(type="Builder", description="General construction")
    ]
    database.add_all(contractor_types)
    database.commit()
    return contractor_types


def create_contractors(database: Session, number_of_records: int):
    """Generate and insert contractor data."""
    contractors = [
        Contractor(
            contact_id=fake.random_element([contact.id for contact in database.query(Contact).all()])
        )
        for _ in range(number_of_records)
    ]
    database.add_all(contractors)
    database.commit()
    return contractors


def create_project_has_contractors(database: Session, contractors: list, projects: list, contractor_types: list):
    """Associate contractors with projects."""
    project_ids = [project.id for project in projects]
    for contractor in contractors:
        project_id = fake.random_element(project_ids)  # Randomly pick a project
        contractor_type_id = fake.random_element([ct.id for ct in contractor_types])
        project_has_contractor = ProjectHasContractor(
            project_id=project_id,
            contractor_id=contractor.id,
            contractor_type_id=contractor_type_id
        )
        database.add(project_has_contractor)
    database.commit()


def create_notes(database: Session, number_of_records: int, projects: list, clients: list):
    """Generate and insert notes for projects."""
    notes = [
        Note(
            project_id=fake.random_element([project.id for project in projects]),
            client_id=fake.random_element([client.id for client in clients]),
            type=fake.random_element(['comment', 'reminder', 'follow_up']),
            content=fake.text(max_nb_chars=200),
        )
        for _ in range(number_of_records)
    ]
    database.add_all(notes)
    database.commit()


def create_building_classes(database: Session, number_of_records: int):
    """Generate and insert building class data."""
    building_classes = [
        BuildingClass(
            code=fake.state_abbr(),  # Two-letter code for building class
            description=fake.text(max_nb_chars=255)
        )
        for _ in range(number_of_records)
    ]
    database.add_all(building_classes)
    database.commit()
    return building_classes


def create_project_is_building_class(database: Session, building_classes: list, projects: list):
    """Associate building classes with projects."""
    project_ids = [project.id for project in projects]
    for building_class in building_classes:
        num_associations = random.randint(1, 5)  # Random number of associations
        selected_projects = random.sample(project_ids, num_associations)
        associations = [
            ProjectIsBuildingClass(
                building_class_id=building_class.id,
                project_id=project_id
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
            contact_id=fake.random_element(contacts).id,
            role=fake.random_element(staff_roles),
            employment_status=fake.random_element(employment_statuses),
            hire_date=fake.date_this_decade(),
            notes=fake.text(max_nb_chars=200)
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
            staff_id=fake.random_element(staff).id,
            project_id=fake.random_element(projects).id if random.choice([True, False]) else None,
            description=fake.sentence(),
            hours=random.randint(1, 8)
        )
        for _ in range(number_of_records)
    ]
    database.add_all(staff_times)
    database.commit()


def create_staff_project(database: Session, staff: list, projects: list):
    """Assign staff members to projects, ensuring no duplicates."""
    assignments = set()  # Use a set to ensure uniqueness

    # Assign each staff member to at least one project
    for _ in range(len(staff)):
        staff_member = fake.random_element(staff)
        project = fake.random_element(projects)
        staff_id = staff_member.id
        project_id = project.id

        # Only add the assignment if it's not already in the set
        if (staff_id, project_id) not in assignments:
            assignments.add((staff_id, project_id))

    # Convert the assignments set to a list of StaffProject objects
    staff_project_entries = [
        StaffProject(staff_id=staff_id, project_id=project_id)
        for staff_id, project_id in assignments
    ]

    # Insert the unique assignments
    database.add_all(staff_project_entries)
    database.commit()


def create_call_logs(database: Session, number_of_records: int, clients: list, staff: list, projects: list):
    """Generate and insert call logs."""
    call_types = ['lead', 'information_request']
    call_statuses = ['follow_up', 'resolved', 'in_progress']

    call_logs = [
        CallLog(
            client_id=fake.random_element(clients).id,
            staff_id=fake.random_element(staff).id,
            project_id=fake.random_element(projects).id if random.choice([True, False]) else None,
            type=fake.random_element(call_types),
            status=fake.random_element(call_statuses),
            datetime=fake.date_time_this_year(),
            description=fake.text(max_nb_chars=255)
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
            project_id=fake.random_element(projects).id,
            type=fake.random_element(budget_types),
            status=fake.random_element(budget_statuses),
            description=fake.sentence(),
            estimate=round(random.uniform(1000, 50000), 2),
            actual=round(random.uniform(500, 49000), 2) if random.choice([True, False]) else None
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
