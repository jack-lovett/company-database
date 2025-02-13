import {API} from "../../services/api.js";
import {updateAddressFields} from "./autocomplete.js";

let addressQueue = [];
let importStats = {
    total: 0,
    accepted: 0,
    skipped: 0,
    current: 0
};
let currentPlaceData = null;

export function handleAddressImport(action) {
    if (action === 'accept' && currentPlaceData) {
        const addressData = {
            street: $('#street').val(),
            suburb: $('#suburb').val(),
            city: $('#city').val(),
            state: $('#state').val(),
            postal_code: $('#postal_code').val(),
            country: $('#country').val(),
            type: $('#type').val()
        };

        API.createAddress(addressData).then(() => {
            importStats.accepted++;
            addressQueue.pop();
            currentPlaceData = null;
            $('#data').DataTable().ajax.reload();
            processNextAddress();
        });
    } else if (action === 'skip') {
        importStats.skipped++;
        addressQueue.pop();
        currentPlaceData = null;
        processNextAddress();
    }
}


export function handlePreviewImport(e) {
    e.preventDefault();
    const fileInput = document.getElementById('csvFile');
    const file = fileInput.files[0];

    const reader = new FileReader();
    reader.onload = function (e) {
        addressQueue = e.target.result.split('\n')
            .map(line => line.trim())
            .filter(line => line.length > 0)
            .reverse();

        importStats.total = addressQueue.length;
        showPreviewStage();
    };
    reader.readAsText(file);
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
            fields: ['components', 'geometry', 'formatted_address']
        }, function (place, status) {
            if (status === google.maps.places.PlacesServiceStatus.OK) {
                currentPlaceData = place;
                updateAddressFields(place.components);
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

function updateImportProgress() {
    importStats.current++;
    const progress = (importStats.current / importStats.total) * 100;
    $('#importProgress').css('width', `${progress}%`);
    $('#currentProgress').text(`Reviewing address ${importStats.current} of ${importStats.total}`);
    $('#importStats').text(`Accepted: ${importStats.accepted} | Skipped: ${importStats.skipped}`);
}

function showPreviewStage() {
    $('#importStage').hide();
    $('#previewStage').show();
    $('#totalRowsCount').text(importStats.total);

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

function showImportSummary() {
    alert(`Import Complete!\nTotal Processed: ${importStats.total}\nAccepted: ${importStats.accepted}\nSkipped: ${importStats.skipped}`);
    $('.modal').modal('hide');
}
