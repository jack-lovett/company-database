export function loadAddresses() {
    return new Promise((resolve) => {
        $.get('http://localhost:8080/addresses', function (data) {
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

export function loadContacts() {
    return new Promise((resolve) => {
        $.get('http://localhost:8080/contacts', function (data) {
            const primarySelect = $('#primary_contact_select');
            const secondarySelect = $('#secondary_contact_select');

            [primarySelect, secondarySelect].forEach(select => {
                select.empty();
                select.append('<option value="">Select Contact...</option>');
                data.forEach(contact => {
                    select.append(`<option value="${contact.contact_id}">${contact.contact_first_name} ${contact.contact_last_name}</option>`);
                });
            });
            resolve();
        });
    });
}

export function loadClients() {
    return new Promise((resolve) => {
        $.get('http://localhost:8080/clients', function (data) {
            const select = $('#client_select');
            select.empty();
            select.append('<option value="">Select Client...</option>');
            data.forEach(client => {
                select.append(`<option value="${client.client_id}">${client.client_name}</option>`);
            });
            resolve();
        });
    });
}