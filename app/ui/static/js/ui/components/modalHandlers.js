import {modalState} from '../modalState.js';

export function initModalHandlers() {
    ['projectModal', 'contactModal', 'clientModal', 'addressModal', 'siteModal',
        'windClassModal', 'localAuthorityModal', 'soilClassModal', 'overlayModal'].forEach(modalId => {
        $(`#${modalId}`)
            .on('hidden.bs.modal', () => modalState.popModal())
            .on('shown.bs.modal', function () {
                $(this).find('input:visible, select:visible').first().focus();
            });
    });
}
