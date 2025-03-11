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














// import api from './ApiConfig';


// // Registro
// export const registro = async (userData) => {
//     const response = await api.get('registro/', userData);
//     return response.data;
// };


// // Login
// export const login = async (username, password) => {
//     const response = await api.post('login/', { username, password });
//     return response.data;
// };
