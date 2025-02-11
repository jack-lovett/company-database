// Helper function to clean form data
function cleanFormData(formData) {
    for (let key in formData) {
        if (formData[key] === "") {
            formData[key] = null;
        }
    }
    return formData;
}

// Form submissions
$('#addressForm').submit(function (e) {
    e.preventDefault();
    const formData = cleanFormData(Object.fromEntries(new FormData(e.target)));
    const previousModal = modalState.modalStack[modalState.modalStack.length - 2];
    const jsonData = JSON.stringify(formData)

    // Store current values of both selects
    const currentBillingValue = $('#billing_address_select').val();
    const currentPostalValue = $('#postal_address_select').val();

    $.ajax({
        url: 'http://localhost:8080/addresses',
        type: 'POST',
        contentType: 'application/json',
        data: jsonData,
        success: function (response) {
            $('#addressModal').modal('hide');
            $('#data').DataTable().ajax.reload();
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
            processNextAddress(); // Process next address after save
        }
    });
});


$('#contactForm').submit(function (e) {
    e.preventDefault();
    const formData = cleanFormData(Object.fromEntries(new FormData(e.target)));


    const jsonData = JSON.stringify(formData);

    const currentPrimaryValue = $('#primary_contact_select').val();
    const currentSecondaryValue = $('#secondary_contact_select').val();

    $.ajax({
        url: 'http://localhost:8080/contacts',
        type: 'POST',
        contentType: 'application/json',
        data: jsonData,
        success: function (response) {
            $('#contactModal').modal('hide');
            $('#data').DataTable().ajax.reload();
            loadContacts().then(() => {
                $('#primary_contact_select').val(currentPrimaryValue);
                $('#secondary_contact_select').val(currentSecondaryValue);

                if (modalState.lastClickedContactBtn === 'createPrimaryContactBtn') {
                    $('#primary_contact_select').val(response.contact_id);
                } else {
                    $('#secondary_contact_select').val(response.contact_id);
                }
            });
        }
    });
});

$('#clientForm').submit(function (e) {
    e.preventDefault();
    const formData = cleanFormData(Object.fromEntries(new FormData(e.target)));

    formData.primary_contact_id = parseInt(formData.primary_contact_id);

    const jsonData = JSON.stringify(formData);

    $.ajax({
        url: 'http://localhost:8080/clients',
        type: 'POST',
        contentType: 'application/json',
        data: jsonData,
        success: function (response) {
            $('#clientModal').modal('hide');
            $('#data').DataTable().ajax.reload();
            loadClients().then(() => {
                $('#client_select').val(response.client_id);
            });
        }
    });
});

$('#projectForm').submit(function (e) {
    e.preventDefault();
    const formData = cleanFormData(Object.fromEntries(new FormData(e.target)));

    const jsonData = JSON.stringify(formData);

    $.ajax({
        url: 'http://localhost:8080/projects',
        type: 'POST',
        contentType: 'application/json',
        data: jsonData,
        success: function (response) {
            $('#projectModal').modal('hide');
            $('#data').DataTable().ajax.reload();
        }
    });
});