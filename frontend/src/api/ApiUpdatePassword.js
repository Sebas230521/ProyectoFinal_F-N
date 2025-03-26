import api from './ApiConfig';

// Restablecer la contraseña con el token
export async function resetPassword(token, nueva_contraseña, confirmar_contraseña) {
        try {
        const response = await api.post('recover_password/restablecer/', {
                token,
                nueva_contraseña,
                confirmar_contraseña
        });
        return response.data;
        } catch (error) {
        console.error('Error al restablecer la contraseña:', error.response?.data || error.message);
        throw new Error(error.response?.data?.message || 'No se pudo actualizar la contraseña.');
        }
}
