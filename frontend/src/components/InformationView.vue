<template>
  <div class="container">
    <h1 class="my-4 text-center">Información del Estanque</h1>

    <!-- Mostrar mensaje de carga -->
    <p v-if="loading">Cargando estanques...</p>
    <p v-if="error" class="text-danger">{{ error }}</p>

    <!-- Select de estanques -->
    <div v-if="!loading" class="form-group">
      <label for="estanqueSelect">Seleccione un estanque:</label>
      <select id="estanqueSelect" v-model="selectedEstanque" @change="fetchInforme" class="form-control">
        <option disabled value="">Seleccione un estanque</option>
        <option v-for="estanque in estanques" :key="estanque.id" :value="estanque.id">
          {{ estanque.nombre_finca }} - {{ estanque.numero_estanque }}
        </option>
      </select>
    </div>

    <!-- Mostrar informe -->
    <div v-if="selectedEstanque">
      <div v-if="htmlInforme" v-html="htmlInforme" class="mt-4"></div>
      <p v-else>No hay datos de informe.</p>
      <button @click="descargarPDF" class="btn btn-primary mt-3">Descargar PDF</button>
    </div>
  </div>
</template>

<script>
import ApiEstanques from "../api/Apiinformation";

export default {
  name: "EstanquesSelectComponent",
  data() {
    return {
      estanques: [],
      selectedEstanque: "",
      htmlInforme: "",
      loading: true,
      error: null
    };
  },
  async mounted() {
    await this.fetchEstanques();
  },
  methods: {
    async fetchEstanques() {
      try {
        const response = await ApiEstanques.fetchEstanquesPorUsuario();
        this.estanques = Array.isArray(response) ? response : [];
      } catch (error) {
        this.error = "Error al cargar los estanques.";
        console.error(error);
      } finally {
        this.loading = false;
      }
    },
    async fetchInforme() {
      if (!this.selectedEstanque) {
        this.htmlInforme = "";
        return;
      }
      try {
        const response = await ApiEstanques.fetchDetalleEstanque(this.selectedEstanque, "html");
        this.htmlInforme = response;
      } catch (error) {
        this.error = "Error al cargar el informe.";
        console.error(error);
      }
    },
    descargarPDF() {
      if (this.selectedEstanque) {
        ApiEstanques.descargarInformePDF(this.selectedEstanque);
      }
    }
  }
};
</script>

<style scoped>
.container {
  padding-top: 20px;
}
</style>
