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
    $('#openSiteModal').click(async () => modalState.pushModal(null, 'siteModal'));

    // Open modal triggers
    $('#projectModal').on('show.bs.modal', async () => {
        const nextNumber = await API.getNextProjectNumber();
        const addresses = await API.fetchAddresses();
        const clients = await API.fetchClients();

        $('#project_number_preview').val(nextNumber["project_number"]);
        await populateSelect('project_address_select', addresses, 'id', ['street', 'suburb']);
        await populateSelect('client_select', clients, 'id', ['name']);

    });

    $('#clientModal').on('show.bs.modal', async () => {
        const contacts = await API.fetchContacts();
        await populateSelect('primary_contact_select', contacts, 'id', ['first_name', 'last_name']);
        await populateSelect('secondary_contact_select', contacts, 'id', ['first_name', 'last_name']);
    });


    $('#contactModal').on('show.bs.modal', async () => {
        const addresses = await API.fetchAddresses();
        await populateSelect('billing_address_select', addresses, 'id', ['street', 'suburb']);
        await populateSelect('postal_address_select', addresses, 'id', ['street', 'suburb']);
    });

    $('#siteModal').on('show.bs.modal', async () => {
        const [addresses, windClasses, localAuthorities, soilClasses, overlays] = await Promise.all([
            API.fetchAddresses(),
            API.fetchWindClasses(),
            API.fetchLocalAuthorities(),
            API.fetchSoilClasses(),
            API.fetchOverlays()
        ]);

        // Destroy work around as refreshing caused duplicate select entries
        $('#overlay_select').selectpicker('destroy');

        await populateSelect('site_address_select', addresses, 'id', ['street', 'suburb']);
        await populateSelect('wind_class_select', windClasses, 'id', ['class_']);
        await populateSelect('local_authority_select', localAuthorities, 'id', ['name']);
        await populateSelect('soil_class_select', soilClasses, 'id', ['class_', 'description']);
        await populateSelect('overlay_select', overlays, 'id', ['name']);

        // Reinitialise selectpicker
        $('#overlay_select').selectpicker();
    });


    // Navigation between modals
    $('#createClientBtn').click(() => modalState.pushModal('projectModal', 'clientModal'));
    $('#createPrimaryContactBtn, #createSecondaryContactBtn').click(function () {
        modalState.lastClickedContactBtn = this.id;
        modalState.pushModal('clientModal', 'contactModal');
    });

    $('#createWindClassBtn').click(() => modalState.pushModal('siteModal', 'windClassModal'));
    $('#createLocalAuthorityBtn').click(() => modalState.pushModal('siteModal', 'localAuthorityModal'));
    $('#createSoilClassBtn').click(() => modalState.pushModal('siteModal', 'soilClassModal'));
    $('#createOverlayBtn').click(() => modalState.pushModal('siteModal', 'overlayModal'));

    // Modal close handlers
    $('.btn-close').click(() => {
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

    $('#createSiteAddressBtn').click(function () {
        modalState.lastClickedAddressBtn = this.id;
        modalState.pushModal('siteModal', 'addressModal');
    });

    // Update modal stack handling
    ['projectModal', 'contactModal', 'clientModal', 'addressModal', 'siteModal',
        'windClassModal', 'localAuthorityModal', 'soilClassModal', 'overlayModal'].forEach(modalId => {
        $(`#${modalId}`)
            .on('hidden.bs.modal', () => modalState.popModal())
            .on('shown.bs.modal', function () {
                $(this).find('input:visible, select:visible').first().focus();
            });
    });


}
