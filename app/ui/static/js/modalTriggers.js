import {modalState} from "./modalState.js";
import {loadAddresses, loadClients, loadContacts} from './dataLoading.js';
import {initAutocomplete} from './googleAutocomplete.js'
import {
    addressQueue,
    importStats,
    processNextAddress,
    setAddressQueue,
    showPreviewStage,
    updateImportProgress
} from './addressImport.js'


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

    // Modified address modal handlers for import mode
    $('#addressModal')
        .on('hidden.bs.modal', function () {
            modalState.popModal();
            if (modalState.importMode) {
                processNextAddress();
            }
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

    // Import addresses button trigger
    $('#openImportModal').click(function () {
        modalState.importMode = true;
        $('#importStage').show();
        $('#previewStage, #reviewStage').hide();
        modalState.pushModal(null, 'importAddressesModal');
    });

    $('#previewImportBtn').click(function (e) {
        e.preventDefault();
        const fileInput = document.getElementById('csvFile');
        const file = fileInput.files[0];

        const reader = new FileReader();
        reader.onload = function (e) {
            const addresses = e.target.result.split('\n')
                .map(line => line.trim())
                .filter(line => line.length > 0)
                .reverse();

            setAddressQueue(addresses);
            importStats.total = addresses.length;
            showPreviewStage();
        };
        reader.readAsText(file);
    });


    $('#beginImport').click(function () {
        $('#previewStage').hide();
        $('#reviewStage').show();
        processNextAddress();
    });

    $('#skipAddress').click(function () {
        importStats.skipped++;
        updateImportProgress();
        addressQueue.pop();
        processNextAddress();
    });

    $('#acceptAddress').click(function () {
        const addressData = {
            address_street: $('#address_street').val(),
            address_suburb: $('#address_suburb').val(),
            address_city: $('#address_city').val(),
            address_state: $('#address_state').val(),
            address_postal_code: $('#address_postal_code').val(),
            address_country: $('#address_country').val(),
            address_type: $('#address_type').val()
        };

        $.ajax({
            url: 'http://localhost:8080/addresses/',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(addressData),
            success: function () {
                importStats.accepted++;
                addressQueue.pop();
                $('#data').DataTable().ajax.reload();
                processNextAddress();
            }
        });
    });


    $('#cancelRemaining').click(function () {
        if (confirm('Are you sure you want to cancel the remaining imports?')) {
            addressQueue = [];
            $('.modal').modal('hide');
        }
    });

    $('#cancelImport').click(function () {
        if (confirm('Are you sure you want to cancel the import?')) {
            addressQueue = [];
            $('.modal').modal('hide');
        }
    });

}


