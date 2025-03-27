import api from './ApiConfig';

/**
 * Restablecer la contraseña con token
 * @param {string} newPassword - Nueva contraseña del usuario
 * @param {string} token - Token de recuperación
 * @returns {Promise<object>} Respuesta del backend
 */
export async function restablecerContraseña(newPassword, token) {
    try {
        console.log("Restableciendo contraseña...");

        const response = await api.post(
            'recover_password/restablecer/', 
            { 
                nueva_contraseña: newPassword, 
                confirmar_contraseña: newPassword, // ← Ahora enviamos también confirmar_contraseña
                token: token 
            }
        );

        return response.data;
    } catch (error) {
        console.error('Error al restablecer la contraseña:', error.response?.data || error.message);
        throw new Error(error.response?.data?.message || 'No se pudo cambiar la contraseña.');
    }
}
