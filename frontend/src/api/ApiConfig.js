import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/', 
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json'
    },
    withCredentials: true // Asegúrate de que el backend permita cookies y sesiones si usas esto
});

export default api;
