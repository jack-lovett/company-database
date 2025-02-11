export const modalState = {
    modalStack: [],
    lastClickedAddressBtn: null,
    lastClickedContactBtn: null,

    clearAllForms: function () {
        $('#addressForm')[0].reset();
        $('#contactForm')[0].reset();
        $('#clientForm')[0].reset();
        $('#projectForm')[0].reset();
    },

    pushModal: function (fromModalId, toModalId) {
        this.stackSizeAfterOpen = this.modalStack.length;
        this.modalStack.push(toModalId);

        if (fromModalId) {
            $(`#${fromModalId}`).modal('hide');
        }

        $(`#${toModalId}`).modal('show');
    },

    popModal: function () {
        const isClosingLastModal = !this.stackSizeAfterOpen;
        const isOpeningNewModal = this.modalStack.length > this.stackSizeAfterOpen;

        if (isClosingLastModal) {
            this.modalStack.pop();
            modalState.clearAllForms();
        } else if (!isOpeningNewModal) {
            const previousModal = this.modalStack[this.modalStack.length - 2];
            $(`#${previousModal}`).modal('show');
            this.modalStack.pop();
        }
        this.stackSizeAfterOpen = this.modalStack.length;
    }
};