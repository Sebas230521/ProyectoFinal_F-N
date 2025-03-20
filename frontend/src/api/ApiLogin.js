import api from './ApiConfig';

// Iniciar sesión (obtener token y almacenarlo)
export async function loginUser(email, password) {
    try {
        const response = await api.post('login/api/login/', { email, password });

        console.log('Respuesta del servidor:', response.data);

        // Cambiar los nombres de los tokens a los que el backend está enviando
        if (response.data.access_token && response.data.refresh_token) {
            localStorage.setItem('access_token', response.data.access_token);
            localStorage.setItem('refresh_token', response.data.refresh_token);
            console.log('Inicio de sesión exitoso, tokens almacenados.');
        } else {
            console.error('Error: No se recibieron tokens en la respuesta.');
        }

        return response.data;
    } catch (error) {
        console.error('Error en el inicio de sesión:', error.response?.data || error.message);
        throw error;
    }
}

// Cerrar sesión (eliminar token)
export function logoutUser() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    console.log('Sesión cerrada, tokens eliminados.');
}
