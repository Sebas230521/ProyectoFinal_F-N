import api from './ApiConfig';

const ApiPond = {
  async listEstanques() {
    const token = localStorage.getItem('access_token');
    if (!token) {
      throw new Error("No hay token de acceso almacenado");
    }
    try {
      const response = await api.get('fish_api/list_estanque/', {
        headers: { Authorization: `Bearer ${token}` }
      });
      return response.data;
    } catch (error) {
      console.error("Error al obtener estanques:", error.response?.data || error.message);
      throw error;
    }
  },

  async detailsEstanque(id) {
    const token = localStorage.getItem('access_token');
    if (!token) {
      throw new Error("No hay token de acceso almacenado");
    }
    try {
      const response = await api.get(`fish_api/details_estanque/${id}/`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      return response.data;
    } catch (error) {
      console.error("Error al obtener detalles del estanque:", error.response?.data || error.message);
      throw error;
    }
  },

  // Otras funciones que utilicen autenticación pueden seguir el mismo patrón...
};

export default ApiPond;
