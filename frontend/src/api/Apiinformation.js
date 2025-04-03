import api from './ApiConfig';

export default {
  // 1️⃣ Obtener la lista de estanques del usuario autenticado
  async fetchEstanquesPorUsuario() {
    const token = localStorage.getItem('access_token');
    if (!token) throw new Error("No hay token de acceso almacenado");

    try {
      const response = await api.get('informacion/estanques/', {
        headers: { Authorization: `Bearer ${token}` },
      });
      return response.data;
    } catch (error) {
      console.error("Error al obtener estanques:", error.response?.data || error);
      throw error;
    }
  },

  // 2️⃣ Obtener el detalle del estanque en JSON
  async fetchDetalleEstanque(pk, formato = 'json') {
    const token = localStorage.getItem('access_token');
    if (!token) throw new Error("No hay token de acceso almacenado");

    try {
      const response = await api.get(`informacion/detalle_estanque/${pk}/`, {
        headers: { Authorization: `Bearer ${token}` },
        params: { formato },
      });
      return response.data;
    } catch (error) {
      console.error("Error al obtener detalle del estanque:", error.response?.data || error);
      throw error;
    }
  },

  // 3️⃣ Descargar informe en PDF directamente
  async descargarInformePDF(pk) {
    const token = localStorage.getItem('access_token');
    if (!token) throw new Error("No hay token de acceso almacenado");

    try {
      const response = await api.get(`informacion/detalle_estanque/${pk}/?formato=pdf`, {
        headers: { Authorization: `Bearer ${token}` },
        responseType: 'blob', // Importante para manejar archivos binarios
      });

      // Crear un objeto URL para el archivo
      const blob = new Blob([response.data], { type: 'application/pdf' });
      const url = window.URL.createObjectURL(blob);

      // Crear un enlace de descarga y simular el clic
      const a = document.createElement('a');
      a.href = url;
      a.download = `Informe_Estanque_${pk}.pdf`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);

      // Liberar memoria
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error("Error al descargar el informe PDF:", error.response?.data || error);
      throw error;
    }
  },

  // 4️⃣ Obtener informe en HTML
  async fetchInformeHTML(pk) {
    const token = localStorage.getItem('access_token');
    if (!token) throw new Error("No hay token de acceso almacenado");

    try {
      const response = await api.get(`informacion/detalle_estanque/${pk}/?formato=html`, {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'text/html',
        },
      });
      return response.data;
    } catch (error) {
      console.error("Error al obtener informe HTML:", error);
      throw error;
    }
  },
};
