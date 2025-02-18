import {initModalHandlers} from './ui/components/modalHandlers.js';
import {initModalButtons} from './ui/components/modalButtons.js';
import {initModalData} from './ui/components/modalSelects.js';
import {initFormHandlers} from './ui/components/forms.js';
import {initGoogleAutocomplete} from './ui/components/autocomplete.js';

async function initializeApp() {
    initModalHandlers();
    initModalButtons();
    await initModalData();
    initFormHandlers();
    await initGoogleAutocomplete();
}

$(document).ready(initializeApp);
