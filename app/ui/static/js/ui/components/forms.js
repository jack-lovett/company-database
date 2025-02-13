import {API} from '../../services/api.js';
// import {validators} from '../validators.js';
import {modalState} from "../modalState.js";
import {populateSelect} from "./modals.js";

export function initFormHandlers() {
    // Form submissions
    $('#addressForm').submit(async function (e) {
        e.preventDefault();
        const formData = cleanFormData(new FormData(e.target));
        const response = await API.createAddress(formData);

        if (response) {
            $('#addressModal').modal('hide');
            await handleAddressCreationSuccess(response);
            this.reset();
        }
    });

    $('#contactForm').submit(async function (e) {
        e.preventDefault();
        const formData = cleanFormData(new FormData(e.target));

        // if (!validators.isValidEmail(formData.email)) {
        //     return showFormError('Invalid email format');
        // }

        const response = await API.createContact(formData);
        if (response) {
            $('#contactModal').modal('hide');
            await handleContactCreationSuccess(response);
            this.reset();
        }
    });

    $('#clientForm').submit(async function (e) {
        e.preventDefault();
        const formData = cleanFormData(new FormData(e.target));
        const response = await API.createClient(formData);

        if (response) {
            $('#clientModal').modal('hide');
            await handleClientCreationSuccess(response);
            this.reset();
        }
    });

    $('#projectForm').submit(async function (e) {
        e.preventDefault();
        const formData = cleanFormData(new FormData(e.target));
        const response = await API.createProject(formData);

        if (response) {
            $('#projectModal').modal('hide');
            refreshDataTable();
            this.reset();
        }
    });
}

function cleanFormData(formData) {
    const data = Object.fromEntries(formData);
    return Object.keys(data).reduce((acc, key) => {
        acc[key] = data[key] || null;
        return acc;
    }, {});
}

async function handleAddressCreationSuccess(response) {
    const addresses = await API.fetchAddresses();
    await populateSelect('project_address_select', addresses, 'address_id', ['address_street', 'address_suburb']);
    await populateSelect('billing_address_select', addresses, 'address_id', ['address_street', 'address_suburb']);
    await populateSelect('postal_address_select', addresses, 'address_id', ['address_street', 'address_suburb']);
    refreshDataTable();
    updateAddressSelects(response.address_id);
}


async function handleContactCreationSuccess(response) {
    const contacts = await API.fetchContacts();
    await populateSelect('primary_contact_select', contacts, 'contact_id', ['contact_first_name', 'contact_last_name']);
    await populateSelect('secondary_contact_select', contacts, 'contact_id', ['contact_first_name', 'contact_last_name']);
    refreshDataTable();
    updateContactSelects(response.contact_id);
}


async function handleClientCreationSuccess(response) {
    const clients = await API.fetchClients();
    await populateSelect('client_select', clients, 'client_id', ['client_name']);
    refreshDataTable();
    updateClientSelect(response.client_id);
}


function refreshDataTable() {
    $('#data').DataTable().ajax.reload();
}

function showFormError(message) {
    // Add your error display logic here
    console.error(message);
}

// Add these functions to your existing forms.js

function updateAddressSelects(newAddressId) {
    const previousModal = modalState.modalStack[modalState.modalStack.length - 2];

    if (previousModal === 'projectModal') {
        $('#project_address_select').val(newAddressId);
    } else if (previousModal === 'contactModal') {
        if (modalState.lastClickedAddressBtn === 'createBillingAddressBtn') {
            $('#billing_address_select').val(newAddressId);
        } else {
            $('#postal_address_select').val(newAddressId);
        }
    }
}

function updateContactSelects(newContactId) {
    if (modalState.lastClickedContactBtn === 'createPrimaryContactBtn') {
        $('#primary_contact_select').val(newContactId);
    } else {
        $('#secondary_contact_select').val(newContactId);
    }
}

function updateClientSelect(newClientId) {
    $('#client_select').val(newClientId);
}

