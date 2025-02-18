import {initModalHandlers} from './ui/components/modalHandlers.js';
import {initModalButtons} from './ui/components/modalButtons.js';
import {initModalData} from './ui/components/modalSelects.js';
import {initFormHandlers} from './ui/components/forms.js';
import {DynamicModal} from './ui/components/dynamicModal.js';

async function initialiseApp() {
    // Get modal configurations from backend
    const response = await fetch('http://localhost:8080/modal-configs');
    const modalConfigs = await response.json();

    // Create dynamic modals
    modalConfigs.forEach(config => {
        new DynamicModal(config);
    });

    // Initialize existing functionality
    initModalHandlers();
    initModalButtons();
    await initModalData();
    initFormHandlers();
}

$(document).ready(initialiseApp);
