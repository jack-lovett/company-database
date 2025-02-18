import {modalState} from '../modalState.js';
import {handleAddressImport, handlePreviewImport, processNextAddress} from "./addressImport.js";

export function initModalButtons() {
    $('#openProjectModal').click(async () => modalState.pushModal(null, 'projectModal'));
    $('#openContactModal').click(async () => modalState.pushModal(null, 'contactModal'));
    $('#openAddressModal').click(async () => modalState.pushModal(null, 'addressModal'));
    $('#openClientModal').click(async () => modalState.pushModal(null, 'clientModal'));
    $('#openSiteModal').click(async () => modalState.pushModal(null, 'siteModal'));

    $('#createClientBtn').click(() => modalState.pushModal('projectModal', 'clientModal'));
    $('#createPrimaryContactBtn, #createSecondaryContactBtn').click(function () {
        modalState.lastClickedContactBtn = this.id;
        modalState.pushModal('clientModal', 'contactModal');
    });

    $('#createWindClassBtn').click(() => modalState.pushModal('siteModal', 'windClassModal'));
    $('#createLocalAuthorityBtn').click(() => modalState.pushModal('siteModal', 'localAuthorityModal'));
    $('#createSoilClassBtn').click(() => modalState.pushModal('siteModal', 'soilClassModal'));
    $('#createOverlayBtn').click(() => modalState.pushModal('siteModal', 'overlayModal'));
    $('#createSiteBtn').click(() => modalState.pushModal('projectModal', 'siteModal'));

    $('.btn-close').click(() => {
        modalState.modalStack = [];
        modalState.clearAllForms();
        $('.modal').modal('hide');
    });
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
    initAddressButtons();
}

function initAddressButtons() {
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
}
