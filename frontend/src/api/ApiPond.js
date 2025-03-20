import api from './ApiConfig';

export default {
  async createEstanque(data) {
    const token = localStorage.getItem('access_token');
    if (!token) {
      throw new Error("No hay token de acceso almacenado");
    }
    try {
      const response = await api.post('fish_api/create_estanque/', data, {
        headers: { Authorization: `Bearer ${token}` }
      });
      return response.data;
    } catch (error) {
      // Si se recibe error 401, puedes redirigir al login o intentar refrescar el token
      if (error.response && error.response.status === 401) {
        console.error("Token no válido o expirado.");
        // Aquí podrías implementar la lógica para refrescar el token o redirigir al usuario al login.
      }
      throw error;
    }
  },
  updateEstanque(pk, data) {
    return api.patch(`fish_api/update_estanque/${pk}/`, data);
  },
  listEstanques() {
    return api.get('fish_api/list_estanque/');
  },
  detailsEstanque(pk) {
    return api.get(`fish_api/details_estanque/${pk}/`);
  }
};
