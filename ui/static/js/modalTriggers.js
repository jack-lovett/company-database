import {modalState} from "./modalState.js";
import {loadAddresses, loadClients, loadContacts} from './dataLoading.js';
import {initAutocomplete} from './googleAutocomplete.js'

export function initModalTriggers() {
    // Create project button trigger
    $('#openProjectModal').click(async function () {
        await loadClients()
        await loadAddresses();
        modalState.pushModal(null, 'projectModal');
    });

    // Get latest project number for preview
    $('#projectModal').on('show.bs.modal', function () {
        $.get('http://localhost:8080/projects/next-number', function (data) {
            $('#project_number_preview').val(data.project_number);
        });
    });

    // Create address button trigger
    $('#openAddressModal').click(function () {
        modalState.pushModal(null, 'addressModal');
    });

    // Create client button trigger
    $('#openClientModal').click(function () {
        modalState.pushModal(null, 'clientModal');
    });

    // Import addresses button trigger
    $('#openImportModal').click(function () {
        modalState.pushModal(null, 'importAddressesModal');
    })

    // Exit modal button trigger
    $(document).on('click', '#exitModal', function () {
        console.log("Clicked exit");
        modalState.modalStack = [];
        modalState.clearAllForms();
        $('.modal').modal('hide');
    });

    // Modal close handlers
    $('#projectModal, #contactModal, #clientModal').on('hidden.bs.modal', function () {
        modalState.popModal();
    });

    $('#addressModal')
        .on('hidden.bs.modal', function () {
            modalState.popModal();
            processNextAddress(); // Process next address after close
        })
        .on('shown.bs.modal', async function () {
            await initAutocomplete();
        });

    $('#createClientBtn').click(async function () {
        await loadContacts();
        modalState.pushModal('projectModal', 'clientModal');
    });

    $('#createPrimaryContactBtn, #createSecondaryContactBtn').click(async function () {
        modalState.lastClickedContactBtn = this.id;
        await loadAddresses();
        modalState.pushModal('clientModal', 'contactModal');
    });

    $('#createBillingAddressBtn, #createPostalAddressBtn').click(function () {
        modalState.lastClickedAddressBtn = this.id;
        modalState.pushModal('contactModal', 'addressModal');

    });

    $('#createProjectAddressBtn').click(function () {
        modalState.pushModal('projectModal', 'addressModal');
    });
}


