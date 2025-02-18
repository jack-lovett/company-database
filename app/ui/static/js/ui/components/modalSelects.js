import {API} from '../../services/api.js';

export async function populateSelect(selectId, items, valueKey, labelKeys) {
    const select = $(`#${selectId}`);
    const currentValue = select.val();
    select.empty().append('<option value="">Select...</option>');

    items.forEach(item => {
        const label = labelKeys.map(key => item[key]).join(', ');
        select.append(`<option value="${item[valueKey]}">${label}</option>`);
    });

    if (currentValue) {
        select.val(currentValue);
    }
}

export async function initModalData() {
    $('#projectModal').on('show.bs.modal', initProjectModalData);
    $('#clientModal').on('show.bs.modal', initClientModalData);
    $('#contactModal').on('show.bs.modal', initContactModalData);
    $('#siteModal').on('show.bs.modal', initSiteModalData);
}

async function initProjectModalData() {
    const nextNumber = await API.getNextProjectNumber();
    const addresses = await API.fetchAddresses();
    const clients = await API.fetchClients();
    const sites = await API.fetchSites();

    $('#project_number_preview').val(nextNumber["project_number"]);
    await populateSelect('project_address_select', addresses, 'id', ['street', 'suburb']);
    await populateSelect('client_select', clients, 'id', ['name']);
    await populateSelect('site_select', sites, 'id', ['address']);
}

async function initClientModalData() {
    const contacts = await API.fetchContacts();
    await populateSelect('primary_contact_select', contacts, 'id', ['first_name', 'last_name']);
    await populateSelect('secondary_contact_select', contacts, 'id', ['first_name', 'last_name']);
}

async function initContactModalData() {
    const addresses = await API.fetchAddresses();
    await populateSelect('billing_address_select', addresses, 'id', ['street', 'suburb']);
    await populateSelect('postal_address_select', addresses, 'id', ['street', 'suburb']);
}

async function initSiteModalData() {
    const [addresses, windClasses, localAuthorities, soilClasses, overlays, sites] = await Promise.all([
        API.fetchAddresses(),
        API.fetchWindClasses(),
        API.fetchLocalAuthorities(),
        API.fetchSoilClasses(),
        API.fetchOverlays(),
        API.fetchSites()
    ]);

    $('#overlay_select').selectpicker('destroy');

    await populateSelect('site_address_select', addresses, 'id', ['street', 'suburb']);
    await populateSelect('wind_class_select', windClasses, 'id', ['class_']);
    await populateSelect('local_authority_select', localAuthorities, 'id', ['name']);
    await populateSelect('soil_class_select', soilClasses, 'id', ['class_', 'description']);
    await populateSelect('overlay_select', overlays, 'id', ['name']);
    await populateSelect('site_select', sites, 'id', ['address']);

    $('#overlay_select').selectpicker();
}
