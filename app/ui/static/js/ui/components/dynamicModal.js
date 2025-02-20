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
        } else if (field.type === 'select') {
            input = document.createElement('select');
            input.className = 'form-select';
            input.id = `${name}_select`;

            const defaultOption = document.createElement('option');
            defaultOption.value = '';
            defaultOption.textContent = 'Select...';
            input.appendChild(defaultOption);

            if (field.enum_values) {
                field.enum_values.forEach(value => {
                    const option = document.createElement('option');
                    option.value = value;
                    option.textContent = value;
                    input.appendChild(option);
                });
            }
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
            setTimeout(() => {
                const firstInput = $(modalElement).find('input:first:visible, select:first:visible');
                if (firstInput.length) {
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
        if (this.config.name === 'Project') {
            const response = await fetch(`${API.baseUrl}/next-number`);
            const data = await response.json();
            const numberField = document.querySelector(`#${this.config.name.toLowerCase()}Form [name="number"]`);
            if (numberField) {
                numberField.value = data.project_number;
            }
        }

        const irregularPlurals = {
            'address': 'addresses'
        };

        console.log('Initializing select fields...');
        for (const [name, field] of Object.entries(this.config.fields)) {
            if (name.endsWith('_id')) {
                const baseModelName = name.replace('_id', '').split('_').pop();
                const modelName = baseModelName.toLowerCase();
                const pluralEndpoint = irregularPlurals[modelName] || `${modelName}s`;
                console.log(`Processing field: ${name}, Model: ${modelName}`);

                try {
                    const response = await fetch(`${API.baseUrl}/${pluralEndpoint}`);
                    const items = await response.json();

                    if (items && items.length > 0) {
                        console.log(`Retrieved ${items.length} items for ${modelName}`);
                        const displayFields = Object.keys(items[0]).filter(key =>
                            !key.endsWith('_id') &&
                            key !== 'id' &&
                            !key.includes('datetime')
                        );
                        console.log(`Display fields selected: ${displayFields.join(', ')}`);
                        await populateSelect(
                            `${name}_select`,
                            items,
                            'id',
                            displayFields
                        );
                    }
                } catch (error) {
                    console.log(`Error fetching ${pluralEndpoint}:`, error);
                }
            }
        }
        console.log('Select initialization completed');
    }


}
