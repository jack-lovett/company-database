let autocomplete;

const SHORT_NAME_ADDRESS_COMPONENT_TYPES = new Set(['street_number', 'administrative_area_level_1', 'postal_code']);

export async function initAutocomplete() {
    const {Autocomplete} = await google.maps.importLibrary("places");
    const addressField = document.querySelector("#address-autocomplete");

    autocomplete = new Autocomplete(addressField, {
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
        fillInAddress(place);
    });
}


function fillInAddress(place) {
    function getComponentName(componentType) {
        for (const component of place.address_components || []) {
            if (component.types[0] === componentType) {
                return SHORT_NAME_ADDRESS_COMPONENT_TYPES.has(componentType) ?
                    component.short_name :
                    component.long_name;
            }
        }
        return '';
    }

    // Clear existing values
    $('#address_street').val('');
    $('#address_suburb').val('');
    $('#address_city').val('');
    $('#address_state').val('');
    $('#address_postal_code').val('');
    $('#address_country').val('');

    // Set new values
    $('#address_street').val(`${getComponentName('street_number')} ${getComponentName('route')}`.trim());
    $('#address_suburb').val(getComponentName('locality'));
    $('#address_city').val(getComponentName('locality'));
    $('#address_state').val(getComponentName('administrative_area_level_1'));
    $('#address_postal_code').val(getComponentName('postal_code'));
    $('#address_country').val('Australia');
}