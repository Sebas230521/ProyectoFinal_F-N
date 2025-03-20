import api from "./ApiConfig"; 

// Registro de usuario (sin token, solo almacena los datos)
export async function register(userData) {
    try {
        const response = await api.post("registro/api/register/", userData, {
            headers: { "Content-Type": "application/json" } 
        });

        console.log("Registro exitoso:", response.data);
        return response.data;
    } catch (error) {
        console.error("Error en el registro:", error.response?.data || error.message);
        throw error;
    }
}
