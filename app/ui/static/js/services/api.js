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
    },

    async fetchWindClasses() {
        const response = await fetch(`${this.baseUrl}/wind-classes`);
        return response.json();
    },

    async fetchLocalAuthorities() {
        const response = await fetch(`${this.baseUrl}/local-authorities`);
        return response.json();
    },

    async fetchSoilClasses() {
        const response = await fetch(`${this.baseUrl}/soil-classes`);
        return response.json();
    },

    async fetchOverlays() {
        const response = await fetch(`${this.baseUrl}/overlays`);
        return response.json();
    },

    async createWindClass(data) {
        const response = await fetch(`${this.baseUrl}/wind-classes`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        return response.json();
    },

    async createLocalAuthority(data) {
        const response = await fetch(`${this.baseUrl}/local-authorities`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        return response.json();
    },

    async createSoilClass(data) {
        const response = await fetch(`${this.baseUrl}/soil-classes`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        return response.json();
    },

    async createOverlay(data) {
        const response = await fetch(`${this.baseUrl}/overlays`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        return response.json();
    },

    async createSite(data) {
        const response = await fetch(`${this.baseUrl}/sites`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        return response.json();
    },

    async fetchSites() {
        const response = await fetch(`${this.baseUrl}/sites`);
        return response.json();
    },

    async getTableConfig() {
        const response = await fetch(`${this.baseUrl}/table-config`);
        if (!response.ok) {
            throw new Error('Failed to fetch table configuration');
        }
        return response.json();
    }

};

