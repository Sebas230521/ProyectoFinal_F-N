import api from './ApiConfig';

export default {
        async crearProcedimiento(data) {
        const token = localStorage.getItem('access_token');
        if (!token) {
        throw new Error("No hay token de acceso almacenado");
        }
        try {
        const response = await api.post('procedimientos/create_procedimiento/', data, {
                headers: { Authorization: `Bearer ${token}` }
        });
        return response.data;
        } catch (error) {
        if (error.response && error.response.status === 401) {
                console.error("Token no válido o expirado.");
                // Aquí podrías implementar lógica para refrescar el token o redirigir al usuario al login.
        }
        throw error;
        }
        },
        async actualizarProcedimiento(id, data) {
        const token = localStorage.getItem('access_token');
        if (!token) {
        throw new Error("No hay token de acceso almacenado");
        }
        try {
        const response = await api.patch(`procedimientos/actualizar_procedimiento/${id}/`, data, {
                headers: { Authorization: `Bearer ${token}` }
        });
        return response.data;
        } catch (error) {
        if (error.response && error.response.status === 401) {
                console.error("Token no válido o expirado.");
                // Lógica para refrescar el token o redirigir al login puede ir aquí.
        }
        throw error;
        }
        },
        async listarProcedimientos() {
        const token = localStorage.getItem('access_token');
        if (!token) {
        throw new Error("No hay token de acceso almacenado");
        }
        try {
        const response = await api.get('procedimientos/listar_procedimientos/', {
                headers: { Authorization: `Bearer ${token}` }
        });
        return response.data;
        } catch (error) {
        if (error.response && error.response.status === 401) {
                console.error("Token no válido o expirado.");
                // Lógica para refrescar el token o redirigir al login puede ir aquí.
        }
        throw error;
        }
        },
        async detallesProcedimiento(id) {
        const token = localStorage.getItem('access_token');
        if (!token) {
        throw new Error("No hay token de acceso almacenado");
        }
        try {
        const response = await api.get(`procedimientos/detalles_procedimiento/${id}/`, {
                headers: { Authorization: `Bearer ${token}` }
        });
        return response.data;
        } catch (error) {
        if (error.response && error.response.status === 401) {
                console.error("Token no válido o expirado.");
                // Lógica para refrescar el token o redirigir al login puede ir aquí.
        }
        throw error;
        }
        }
};
