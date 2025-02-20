import {API} from '../../services/api.js';
import {populateSelect} from './modalSelects.js';

export class DynamicModal {
    constructor(config) {
        this.config = config;
        this.modal = this.createModal();
        this.setupEventListeners();
    }

    createModal() {
        const template = document.getElementById('dynamic-modal-template');
        const modal = template.content.cloneNode(true);

        const modalElement = modal.querySelector('.modal');
        modalElement.id = `${this.config.name.toLowerCase()}Modal`;

        const form = modal.querySelector('form');
        form.id = `${this.config.name.toLowerCase()}Form`;

        modal.querySelector('.modal-title').textContent = this.config.title;

        this.populateFields(modal);

        document.body.appendChild(modal);
        return new bootstrap.Modal(modalElement);
    }

    createFieldElement(name, field) {
        const wrapper = document.createElement('div');
        wrapper.className = 'mb-3';

        const label = document.createElement('label');
        label.className = 'form-label';
        label.textContent = field.label;
        wrapper.appendChild(label);

        let input;

        if (field.type === 'textarea') {
            input = document.createElement('textarea');
            input.className = 'form-control';
        } else if (field.type === 'select' && field.enum_values) {
            input = document.createElement('select');
            input.className = 'form-select';
            field.enum_values.forEach(value => {
                const option = document.createElement('option');
                option.value = value;
                option.textContent = value;
                input.appendChild(option);
            });
        } else {
            input = document.createElement('input');
            input.className = 'form-control';
            input.setAttribute('type', field.type || 'text');
        }

        input.name = name;
        if (field.required) input.required = true;

        wrapper.appendChild(input);
        return wrapper;
    }

    populateFields(modal) {
        const container = modal.querySelector('#modal-fields');

        Object.entries(this.config.fields).forEach(([name, field]) => {
            const col = document.createElement('div');
            col.className = 'col-md-6';
            col.appendChild(this.createFieldElement(name, field));
            container.appendChild(col);
        });
    }

    setupEventListeners() {
        const modalElement = document.getElementById(`${this.config.name.toLowerCase()}Modal`);
        const form = modalElement.querySelector('form');

        modalElement.addEventListener('shown.bs.modal', () => {
            this.initialiseSelects();
            // Use setTimeout to ensure DOM is ready
            setTimeout(() => {
                const firstInput = modalElement.querySelector('input:visible, select:visible');
                if (firstInput) {
                    firstInput.focus();
                }
            }, 100);
        });


        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const response = await API.create(this.config.name.toLowerCase(), formData);
            if (response) {
                this.modal.hide();
                $('#data').DataTable().ajax.reload();
                form.reset();
            }
        });
    }

    async initialiseSelects() {
        for (const [name, field] of Object.entries(this.config.fields)) {
            if (field.type === 'select' && field.related_model) {
                const items = await API.fetch(field.related_model.toLowerCase());
                await populateSelect(
                    `${name}_select`,
                    items,
                    'id',
                    ['name']
                );
            }
        }
    }
}
