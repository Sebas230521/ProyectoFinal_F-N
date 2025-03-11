import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/registro/', // URL del backend Django
    timeout: 5000, // Tiempo máximo de espera 
    headers: {
        'Content-Type': 'aplicacion/json'
    }
});

export default api;