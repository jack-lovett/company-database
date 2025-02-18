import {API} from '../../services/api.js';
// import {validators} from '../validators.js';
import {modalState} from "../modalState.js";
import {populateSelect} from "./modalSelects.js";

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

    $('#windClassForm').submit(async function (e) {
        e.preventDefault();
        const formData = cleanFormData(new FormData(e.target));
        const response = await API.createWindClass(formData);
        if (response) {
            $('#windClassModal').modal('hide');
            await handleWindClassCreationSuccess(response);
            this.reset();
        }
    });

    $('#localAuthorityForm').submit(async function (e) {
        e.preventDefault();
        const formData = cleanFormData(new FormData(e.target));
        const response = await API.createLocalAuthority(formData);
        if (response) {
            $('#localAuthorityModal').modal('hide');
            await handleLocalAuthorityCreationSuccess(response);
            this.reset();
        }
    });

    $('#soilClassForm').submit(async function (e) {
        e.preventDefault();
        const formData = cleanFormData(new FormData(e.target));
        const response = await API.createSoilClass(formData);
        if (response) {
            $('#soilClassModal').modal('hide');
            await handleSoilClassCreationSuccess(response);
            this.reset();
        }
    });

    $('#overlayForm').submit(async function (e) {
        e.preventDefault();
        const formData = cleanFormData(new FormData(e.target));
        const response = await API.createOverlay(formData);
        if (response) {
            $('#overlayModal').modal('hide');
            await handleOverlayCreationSuccess(response);
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
    await populateSelect('project_address_select', addresses, 'id', ['street', 'suburb']);
    await populateSelect('billing_address_select', addresses, 'id', ['street', 'suburb']);
    await populateSelect('postal_address_select', addresses, 'id', ['street', 'suburb']);
    refreshDataTable();
    updateAddressSelects(response.id);
}


async function handleContactCreationSuccess(response) {
    const contacts = await API.fetchContacts();
    await populateSelect('primary_contact_select', contacts, 'id', ['first_name', 'last_name']);
    await populateSelect('secondary_contact_select', contacts, 'id', ['first_name', 'last_name']);
    refreshDataTable();
    updateContactSelects(response.id);
}


async function handleClientCreationSuccess(response) {
    const clients = await API.fetchClients();
    await populateSelect('client_select', clients, 'id', ['name']);
    refreshDataTable();
    updateClientSelect(response.id);
}

async function handleWindClassCreationSuccess(response) {
    console.log('Wind Class Response:', response);
    const windClasses = await API.fetchWindClasses();
    console.log('Fetched Wind Classes:', windClasses);
    await populateSelect('wind_class_select', windClasses, 'id', ['class_']);
    console.log('Setting select value to:', response.id);
    $('#wind_class_select').val(response.id);
}


async function handleLocalAuthorityCreationSuccess(response) {
    const localAuthorities = await API.fetchLocalAuthorities();
    await populateSelect('local_authority_select', localAuthorities, 'id', ['name']);
    $('#local_authority_select').val(response.id);
}

async function handleSoilClassCreationSuccess(response) {
    const soilClasses = await API.fetchSoilClasses();
    await populateSelect('soil_class_select', soilClasses, 'id', ['class_', 'description']);
    $('#soil_class_select').val(response.id);
}


async function handleOverlayCreationSuccess(response) {
    const overlays = await API.fetchOverlays();
    await populateSelect('overlay_select', overlays, 'id', ['name']);
    $('#overlay_select').val(response.id);
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

