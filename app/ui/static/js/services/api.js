export const API = {
    baseUrl: 'http://localhost:8080',

    async fetchAddresses() {
        const response = await fetch(`${this.baseUrl}/addresses`);
        return response.json();
    },

    async fetchContacts() {
        const response = await fetch(`${this.baseUrl}/contacts`);
        return response.json();
    },

    async fetchClients() {
        const response = await fetch(`${this.baseUrl}/clients`);
        return response.json();
    },

    async getNextProjectNumber() {
        const response = await fetch(`${this.baseUrl}/projects/next-number`);
        return response.json();
    },

    async createAddress(data) {
        const response = await fetch(`${this.baseUrl}/addresses`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        return response.json();
    },

    async createContact(data) {
        const response = await fetch(`${this.baseUrl}/contacts`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        return response.json();
    },

    async createClient(data) {
        const response = await fetch(`${this.baseUrl}/clients`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        return response.json();
    },

    async createProject(data) {
        const response = await fetch(`${this.baseUrl}/projects`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        return response.json();
    },

    async importAddresses(addresses) {
        const response = await fetch(`${this.baseUrl}/addresses/import`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(addresses)
        });
        return response.json();
    }
};

