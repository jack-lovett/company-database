import {modalState} from '../modalState.js';
import {handleAddressImport, handlePreviewImport, processNextAddress} from './addressImport.js';
import {API} from "../../services/api.js";

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

export function initModalHandlers() {
    // Modal open handlers
    $('#openProjectModal').click(async () => modalState.pushModal(null, 'projectModal'));
    $('#openContactModal').click(async () => modalState.pushModal(null, 'contactModal'));
    $('#openAddressModal').click(async () => modalState.pushModal(null, 'addressModal'));
    $('#openClientModal').click(async () => modalState.pushModal(null, 'clientModal'));

    // Open modal triggers
    $('#projectModal').on('show.bs.modal', async () => {
        const nextNumber = await API.getNextProjectNumber();
        const addresses = await API.fetchAddresses();
        const clients = await API.fetchClients();

        $('#project_number_preview').val(nextNumber["project_number"]);
        await populateSelect('project_address_select', addresses, 'address_id', ['address_street', 'address_suburb']);
        await populateSelect('client_select', clients, 'client_id', ['client_name']);

    });

    $('#clientModal').on('show.bs.modal', async () => {
        const contacts = await API.fetchContacts();
        await populateSelect('primary_contact_select', contacts, 'contact_id', ['contact_first_name', 'contact_last_name']);
        await populateSelect('secondary_contact_select', contacts, 'contact_id', ['contact_first_name', 'contact_last_name']);
    });


    $('#contactModal').on('show.bs.modal', async () => {
        const addresses = await API.fetchAddresses();
        await populateSelect('billing_address_select', addresses, 'address_id', ['address_street', 'address_suburb']);
        await populateSelect('postal_address_select', addresses, 'address_id', ['address_street', 'address_suburb']);
    });


    // Navigation between modals
    $('#createClientBtn').click(() => modalState.pushModal('projectModal', 'clientModal'));
    $('#createPrimaryContactBtn, #createSecondaryContactBtn').click(function () {
        modalState.lastClickedContactBtn = this.id;
        modalState.pushModal('clientModal', 'contactModal');
    });

    // Modal close handlers
    $('#exitModal').click(() => {
        modalState.modalStack = [];
        modalState.clearAllForms();
        $('.modal').modal('hide');
    });

    ['projectModal', 'contactModal', 'clientModal', 'addressModal'].forEach(modalId => {
        $(`#${modalId}`).on('hidden.bs.modal', () => modalState.popModal());
    });

    // Import address handlers
    $('#openImportModal').click(() => {
        $('#importStage').show();
        $('#previewStage, #reviewStage').hide();
        modalState.pushModal(null, 'importAddressesModal');
    });

    $('#previewImportBtn').click(handlePreviewImport);
    $('#beginImport').click(() => {
        $('#previewStage').hide();
        $('#reviewStage').show();
        processNextAddress();
    });

    $('#skipAddress').click(() => handleAddressImport('skip'));
    $('#acceptAddress').click(() => handleAddressImport('accept'));
    $('#cancelRemaining, #cancelImport').click(() => {
        if (confirm('Are you sure you want to cancel the import?')) {
            $('.modal').modal('hide');
        }
    });

    $('#createBillingAddressBtn, #createPostalAddressBtn').click(function () {
        modalState.lastClickedAddressBtn = this.id;
        modalState.pushModal('contactModal', 'addressModal');
    });

    $('#createProjectAddressBtn').click(function () {
        modalState.lastClickedAddressBtn = this.id;
        modalState.pushModal('projectModal', 'addressModal');
    });


}
