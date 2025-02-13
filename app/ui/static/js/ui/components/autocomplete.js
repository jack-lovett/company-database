export async function initGoogleAutocomplete() {
    const {Autocomplete} = await google.maps.importLibrary("places");
    const addressField = document.querySelector("#address-autocomplete");

    const autocomplete = new Autocomplete(addressField, {
        componentRestrictions: {country: ["au"]},
        fields: ["address_components", "geometry"],
        types: ["address"],
    });

    google.maps.event.addListener(autocomplete, 'place_changed', () => {
        const place = autocomplete.getPlace();
        if (!place.geometry) {
            window.alert(`No details available for input: '${place.name}'`);
            return;
        }
        updateAddressFields(place.address_components);
    });

    return autocomplete;
}

export function updateAddressFields(addressComponents) {
    // Clear existing values first
    ['address_street', 'address_suburb', 'address_city', 'address_state', 'address_postal_code', 'address_country']
        .forEach(fieldId => $(`#${fieldId}`).val(''));

    // Get street number and name separately
    let streetNumber = '';
    let streetName = '';

    addressComponents.forEach(component => {
        const type = component.types[0];
        switch (type) {
            case 'street_number':
                streetNumber = component.long_name;
                break;
            case 'route':
                streetName = component.long_name;
                break;
            case 'locality':
                $('#address_suburb, #address_city').val(component.long_name);
                break;
            case 'administrative_area_level_1':
                $('#address_state').val(component.short_name);
                break;
            case 'postal_code':
                $('#address_postal_code').val(component.long_name);
                break;
            case 'country':
                $('#address_country').val(component.long_name);
                break;
        }
    });

    // Combine street number and name
    $('#address_street').val(`${streetNumber} ${streetName}`.trim());

    // Set default country if not found in components
    if (!$('#address_country').val()) {
        $('#address_country').val('Australia');
    }
}
