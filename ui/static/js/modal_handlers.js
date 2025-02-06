const modalState = {
    modalStack: [],
    lastClickedAddressBtn: null,

    clearAllForms: function () {
        $('#addressForm')[0].reset();
        $('#contactForm')[0].reset();
        $('#clientForm')[0].reset();
        $('#projectForm')[0].reset();
    },

    pushModal: function (fromModalId, toModalId) {
        this.stackSizeAfterOpen = this.modalStack.length;
        this.modalStack.push(toModalId);

        if (fromModalId) {
            $(`#${fromModalId}`).modal('hide');
        }

        $(`#${toModalId}`).modal('show');
    },

    popModal: function () {
        const isClosingLastModal = !this.stackSizeAfterOpen;
        const isOpeningNewModal = this.modalStack.length > this.stackSizeAfterOpen;

        if (isClosingLastModal) {
            this.modalStack.pop();
            modalState.clearAllForms();
        } else if (!isOpeningNewModal) {
            const previousModal = this.modalStack[this.modalStack.length - 2];
            $(`#${previousModal}`).modal('show');
            this.modalStack.pop();
        }
        this.stackSizeAfterOpen = this.modalStack.length;
    }
};


$(document).ready(function () {
    // Load functions for select dropdowns
    function loadAddresses() {
        return new Promise((resolve) => {
            $.get('http://192.168.15.15:8080/addresses', function (data) {
                const billingSelect = $('#billing_address_select');
                const postalSelect = $('#postal_address_select');
                const projectSelect = $('#project_address_select');

                [billingSelect, postalSelect, projectSelect].forEach(select => {
                    select.empty();
                    select.append('<option value="">Select Address...</option>');
                    data.forEach(address => {
                        select.append(`<option value="${address.address_id}">${address.address_street}, ${address.address_suburb}</option>`);
                    });
                });
                resolve();
            });
        });
    }

    function loadContacts() {
        $.get('http://192.168.15.15:8080/contacts', function (data) {
            const primarySelect = $('#primary_contact_select');
            const secondarySelect = $('#secondary_contact_select');

            [primarySelect, secondarySelect].forEach(select => {
                select.empty();
                select.append('<option value="">Select Contact...</option>');
                data.forEach(contact => {
                    select.append(`<option value="${contact.contact_id}">${contact.contact_first_name} ${contact.contact_last_name}</option>`);
                });
            });
        });
    }

    function loadClients() {
        $.get('http://192.168.15.15:8080/clients', function (data) {
            const select = $('#client_select');
            select.empty();
            select.append('<option value="">Select Client...</option>');
            data.forEach(client => {
                select.append(`<option value="${client.client_id}">${client.client_name}</option>`);
            });
        });
    }

    // Modal trigger buttons
    $('#openProjectModal').click(function () {
        modalState.pushModal(null, 'projectModal');
    });


    $('#createClientBtn').click(function () {
        modalState.pushModal('projectModal', 'clientModal');
    });

    $('#createPrimaryContactBtn, #createSecondaryContactBtn').click(function () {
        modalState.pushModal('clientModal', 'contactModal');
    });

    $('#createBillingAddressBtn, #createPostalAddressBtn').click(function () {
        modalState.lastClickedAddressBtn = this.id;
        modalState.pushModal('contactModal', 'addressModal');
    });

    $('#createProjectAddressBtn').click(function () {
        modalState.pushModal('projectModal', 'addressModal');
    });

    $(document).on('click', '#exitModal', function () {
        console.log("Clicked exit");
        modalState.modalStack = [];
        modalState.clearAllForms();
        $('.modal').modal('hide');
    });


    // Modal close handlers
    $('#projectModal, #contactModal, #clientModal, #addressModal').on('hidden.bs.modal', function () {
        modalState.popModal();
    });


    // Form submissions
    $('#addressForm').submit(function (e) {
        e.preventDefault();
        const formData = JSON.stringify(Object.fromEntries(new FormData(e.target)));
        const previousModal = modalState.modalStack[modalState.modalStack.length - 2];

        // Store current values of both selects
        const currentBillingValue = $('#billing_address_select').val();
        const currentPostalValue = $('#postal_address_select').val();

        $.ajax({
            url: 'http://192.168.15.15:8080/addresses',
            type: 'POST',
            contentType: 'application/json',
            data: formData,
            success: function (response) {
                $('#addressModal').modal('hide');
                loadAddresses().then(() => {
                    let selectId;
                    if (previousModal === 'projectModal') {
                        selectId = '#project_address_select';
                        $(selectId).val(response.address_id);
                    } else if (previousModal === 'contactModal') {
                        // Restore previous values and update only the relevant select
                        $('#billing_address_select').val(currentBillingValue);
                        $('#postal_address_select').val(currentPostalValue);

                        if (modalState.lastClickedAddressBtn === 'createBillingAddressBtn') {
                            $('#billing_address_select').val(response.address_id);
                        } else {
                            $('#postal_address_select').val(response.address_id);
                        }
                    }
                });
            }
        });
    });


    $('#contactForm').submit(function (e) {
        e.preventDefault();
        const formData = JSON.stringify(Object.fromEntries(new FormData(e.target)));

        $.ajax({
            url: 'http://192.168.15.15:8080/contacts',
            type: 'POST',
            contentType: 'application/json',
            data: formData,
            success: function (response) {
                $('#contactModal').modal('hide');
                loadContacts();
            }
        });
    });

    $('#clientForm').submit(function (e) {
        e.preventDefault();
        const formData = JSON.stringify(Object.fromEntries(new FormData(e.target)));

        $.ajax({
            url: 'http://192.168.15.15:8080/clients',
            type: 'POST',
            contentType: 'application/json',
            data: formData,
            success: function (response) {
                $('#clientModal').modal('hide');
                loadClients();
            }
        });
    });

    $('#projectForm').submit(function (e) {
        e.preventDefault();
        const formData = JSON.stringify(Object.fromEntries(new FormData(e.target)));

        $.ajax({
            url: 'http://192.168.15.15:8080/projects',
            type: 'POST',
            contentType: 'application/json',
            data: formData,
            success: function (response) {
                $('#projectModal').modal('hide');
                window.location.reload();
            }
        });
    });

    // Initial load of all dropdowns
    loadAddresses();
    loadContacts();
    loadClients();
});
