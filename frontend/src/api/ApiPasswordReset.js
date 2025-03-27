import api from './ApiConfig';

/**
 * Solicitar recuperación de contraseña (envía email con el enlace)
 * @param {string} email - Correo del usuario para recibir el enlace
 * @returns {Promise<object>} Respuesta del backend
 */
export async function recoveryrequest(email) {
    try {
        console.log("Enviando email para recuperación:", email);

        const response = await api.post(
            'recover_password/solicitar/', // Asegúrate de que esta ruta coincida con la del backend
            { email } 
        );

        return response.data;
    } catch (error) {
        console.error('Error al solicitar recuperación de contraseña:', error.response?.data || error.message);
        throw new Error(error.response?.data?.message || 'No se pudo procesar la solicitud.');
    }
}
