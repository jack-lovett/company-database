export const modalState = {
    modalStack: [],
    lastClickedAddressBtn: null,
    lastClickedContactBtn: null,
    stackSizeAfterOpen: 0,

    clearAllForms() {
        ['addressForm', 'contactForm', 'clientForm', 'projectForm'].forEach(formId => {
            $(`#${formId}`)[0].reset();
        });
    },

    pushModal(fromModalId, toModalId) {
        this.stackSizeAfterOpen = this.modalStack.length;
        this.modalStack.push(toModalId);

        if (fromModalId) {
            const fromModal = $(`#${fromModalId}`);
            fromModal.modal('hide');
            fromModal.attr('aria-hidden', 'false');
        }

        const toModal = $(`#${toModalId}`);
        toModal.modal('show');
        toModal.attr('aria-hidden', 'false');

        // Set focus to the first focusable element in new modal
        toModal.find('input:visible, select:visible').first().focus();
    },

    popModal() {
        const isClosingLastModal = !this.stackSizeAfterOpen;
        const isOpeningNewModal = this.modalStack.length > this.stackSizeAfterOpen;

        if (isClosingLastModal) {
            this.modalStack.pop();
            this.clearAllForms();
        } else if (!isOpeningNewModal) {
            const previousModal = this.modalStack[this.modalStack.length - 2];
            $(`#${previousModal}`).modal('show');
            this.modalStack.pop();
        }
        this.stackSizeAfterOpen = this.modalStack.length;
    }
};
