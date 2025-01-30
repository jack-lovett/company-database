# app.py
from flask import Flask, render_template, request, g

from database import SessionLocal
from services.address import AddressService
from services.client import ClientService
from services.contact import ContactService
from services.project import ProjectService
from services.table_service import GenericTableService

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

    }

    model = model_map.get(table_name.lower())
    if not model:
        return "Table not found", 404

    columns = service.get_table_columns(model)
    data = service.get_enriched_data(model)

    return render_template("dynamic_table.html", table_name=table_name, columns=columns, data=data)


# Other routes for adding/editing projects, etc.
@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        # Logic to add a project
        pass
    return render_template('add_project.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
