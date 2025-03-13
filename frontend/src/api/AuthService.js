import api from './ApiConfig'; 

export const register = async (userData) => {
    try {
        const response = await api.post('registro/', userData);
        return response.data; // Devuelve la respuesta del backend
    } catch (error) {
        console.error("Error en el registro:", error.response?.data || error);
        throw error;
    }
};
