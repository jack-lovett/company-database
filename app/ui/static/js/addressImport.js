import {fillInAddress} from "./googleAutocomplete.js";

export let addressQueue = [];
export let importStats = {
    total: 0,
    accepted: 0,
    skipped: 0,
    current: 0
};

export function setAddressQueue(addresses) {
    addressQueue = addresses;
}

export function showPreviewStage() {
    $('#importStage').hide();
    $('#previewStage').show();
    $('#totalRowsCount').text(importStats.total);

    // Populate preview table
    const previewTable = $('#previewTable tbody');
    previewTable.empty();

    addressQueue.forEach(address => {
        previewTable.append(`
            <tr>
                <td>${address}</td>
                <td>Pending</td>
                <td><span class="badge bg-secondary">Waiting</span></td>
            </tr>
        `);
    });
}

export function updateImportProgress() {
    importStats.current++;
    const progress = (importStats.current / importStats.total) * 100;
    $('#importProgress').css('width', `${progress}%`);
    $('#currentProgress').text(`Reviewing address ${importStats.current} of ${importStats.total}`);
    $('#importStats').text(`Accepted: ${importStats.accepted} | Skipped: ${importStats.skipped}`);
}

export function processNextAddress() {
    if (addressQueue.length > 0) {
        const address = addressQueue[addressQueue.length - 1];
        updateImportProgress();

        const autocomplete = new google.maps.places.AutocompleteService();
        autocomplete.getPlacePredictions({
            input: address,
            componentRestrictions: {country: 'au'}
        }, handlePlacePredictions);
    } else {
        showImportSummary();
    }
}

function handlePlacePredictions(predictions, status) {
    if (status === google.maps.places.PlacesServiceStatus.OK) {
        const originalAddress = addressQueue[addressQueue.length - 1];

        const placesService = new google.maps.places.PlacesService(document.createElement('div'));
        placesService.getDetails({
            placeId: predictions[0].place_id,
            fields: ['address_components', 'geometry', 'formatted_address']
        }, function (place, status) {
            if (status === google.maps.places.PlacesServiceStatus.OK) {
                fillInAddress(place);
                $('#currentAddressPreview').html(`
                    <div class="alert alert-info">
                        <strong>Currently Processing:</strong><br>
                        <p class="mt-2">${originalAddress}</p>
                        <strong>Google Maps Suggestion:</strong><br>
                        <p class="mt-2">${place.formatted_address}</p>
                    </div>
                `);
            }
        });
    }
}

export function showImportSummary() {
    alert(`Import Complete!\nTotal Processed: ${importStats.total}\nAccepted: ${importStats.accepted}\nSkipped: ${importStats.skipped}`);
    $('.modal').modal('hide');
}