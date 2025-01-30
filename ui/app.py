# app.py
from flask import Flask, render_template, g, request, jsonify

from database import SessionLocal
from models import Project
from services.address import AddressService
from services.client import ClientService
from services.contact import ContactService
from services.project import ProjectService

app = Flask(__name__)


def get_database():
    """Create a new database session."""
    database = SessionLocal()
    return database


@app.before_request
def before_request():
    """Run new session before each request."""
    g.database = get_database()


@app.after_request
def after_request(response):
    """Close each session after response is sent."""
    database_session = g.pop("database", None)
    if database_session:
        database_session.close()
    return response


# Home route
@app.route('/')
def index():
    return render_template('index.html', )


@app.route('/projects')
def projects():
    session = g.database
    project_service = ProjectService()
    projects = project_service.get_enriched_projects(session)
    clients_service = ClientService()

    return render_template('projects.html', projects=projects)


@app.route("/clients")
def clients():
    session = g.database  # Ensure you get a valid DB session
    client_service = ClientService()
    clients = client_service.get_enriched_clients(session)
    return render_template("clients.html", clients=clients)


@app.route("/contacts")
def contacts():
    session = g.database
    contact_service = ContactService()
    enriched_contacts = contact_service.get_enriched_contacts(session)
    return render_template("contacts.html", contacts=enriched_contacts)


@app.route("/addresses")
def addresses():
    session = g.database
    address_service = AddressService()
    enriched_addresses = address_service.get_enriched_addresses(session)
    return render_template("addresses.html", addresses=enriched_addresses)


@app.route('/projects/create', methods=['POST'])
def create_project():
    data = request.form
    new_project = Project(
        client_id=data['client_id'],
        address_id=data['address_id'],
        project_status=data['project_status'],
        project_description=data.get('project_description'),
        project_start_date=data.get('project_start_date'),
        project_end_date=data.get('project_end_date'),
        project_storeys=data.get('project_storeys'),
        project_referral_source=data.get('project_referral_source'),
        project_payment_basis=data.get('project_payment_basis')
    )
    # db.session.add(new_project)
    # db.session.commit()
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
