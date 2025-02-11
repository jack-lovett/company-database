let addressQueue = [];

$('#importAddressForm').submit(function (e) {
    e.preventDefault();
    const fileInput = document.getElementById('csvFile');
    const file = fileInput.files[0];

    const reader = new FileReader();
    reader.onload = function (e) {
        addressQueue = e.target.result.split('\n')
            .map(line => line.trim())
            .filter(line => line.length > 0)
            .reverse(); // Process from newest to oldest

        $('#importAddressesModal').modal('hide');
        processNextAddress();
    };
    reader.readAsText(file);
});

function processNextAddress() {
    if (addressQueue.length > 0) {
        const address = addressQueue.pop();
        const autocomplete = new google.maps.places.AutocompleteService();

        autocomplete.getPlacePredictions({
            input: address,
            componentRestrictions: {country: 'au'}
        }, function (predictions, status) {
            if (status === google.maps.places.PlacesServiceStatus.OK) {
                const placesService = new google.maps.places.PlacesService(document.createElement('div'));
                placesService.getDetails({
                    placeId: predictions[0].place_id,
                    fields: ['address_components', 'geometry']
                }, function (place, status) {
                    if (status === google.maps.places.PlacesServiceStatus.OK) {
                        modalState.pushModal(null, 'addressModal');
                        fillInAddress(place);
                    }
                });
            }
        });
    }
}