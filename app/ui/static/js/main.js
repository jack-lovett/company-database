import {initModalHandlers} from './ui/components/modals.js';
import {initFormHandlers} from './ui/components/forms.js';
import {initGoogleAutocomplete} from './ui/components/autocomplete.js';

async function initializeApp() {
    initModalHandlers();
    initFormHandlers();
    await initGoogleAutocomplete();

    // Initialize any other UI components
}

$(document).ready(initializeApp);
