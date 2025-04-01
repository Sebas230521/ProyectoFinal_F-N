<template>
  <div class="container form-container">
    <h3 class="text-center">Registro de procedimientos</h3>
    <form @submit.prevent="submitForm" class="needs-validation" novalidate>
      <div class="row g-3">
        <div class="col-md-6">
          <!-- Nombre de la finca -->
          <div class="form-group mt-3">
            <label for="finca" class="form-label">Nombre de la finca</label>
            <select
              v-model="finca"
              class="form-select rounded-pill overflow-hidden"
              id="finca"
              @change="checkFormValidity"
              required
            >
              <option disabled value="">Seleccione</option>
              <option v-for="f in fincas" :key="f.nombre" :value="f.nombre">
                {{ f.nombre }}
              </option>
            </select>
          </div>
  
          <!-- Campo de Selección de Estanque -->
          <div class="form-group mt-3">
            <label for="estanque" class="form-label">Estanque</label>
            <select
              v-model="estanque"
              class="form-select rounded-pill overflow-hidden"
              id="estanque"
              @change="checkFormValidity"
              required
            >
              <option disabled value="">Seleccione</option>
              <option v-for="pond in estanquesFiltrados" :key="pond.numero_estanque" :value="pond.numero_estanque">
                {{ pond.numero_estanque }} - {{ pond.tipo_estanque }}
              </option>
            </select>
          </div>
  
          <!-- Campo de Observaciones -->
          <div class="form-group mt-3">
            <label for="observaciones" class="form-label">Observaciones en el estanque</label>
            <textarea
              class="form-control"
              id="Textarea-mensaje"
              v-model="observaciones"
              placeholder="Deje un comentario aquí"
              style="height: 130px"
              @change="checkFormValidity"
            ></textarea>
          </div>
        </div>
        
        <div class="col-md-6">
          <!-- Campo de Descripción del Procedimiento -->
          <div class="form-group mt-3">
            <label for="descripcionProcedimiento" class="form-label">Descripción del procedimiento</label>
            <input
              class="form-control rounded-pill overflow-hidden"
              v-model="descripcionProcedimiento"
              placeholder="Descripción"
              @change="checkFormValidity"
            />
          </div>
  
          <!-- Campo de Nombre del Procedimiento -->
          <div class="form-group mt-3">
            <label for="nombreProcedimiento" class="form-label">Nombre del procedimiento</label>
            <input
              type="text"
              class="form-control rounded-pill overflow-hidden"
              v-model="nombreProcedimiento"
              placeholder="Nombre del procedimiento"
              @change="checkFormValidity"
            />
          </div>
  
          <!-- Campo de Tipo de Concentrado -->
          <div class="form-group mt-3">
            <label for="tipoConcentrado" class="form-label">Tipo de concentrado</label>
            <select
              v-model="tipoConcentrado"
              class="form-select rounded-pill overflow-hidden"
              @change="checkFormValidity"
            >
              <option disabled value="">Seleccione</option>
              <option value="Alevinaje-45%">Alevinaje 45%</option>
              <option value="PreJuveniles-38%">PreJuveniles 38%</option>
              <option value="Juveniles-34%">Juveniles 34%</option>
              <option value="PreEngorde-30%">PreEngorde 30%</option>
              <option value="Engorde-24%">Engorde 24%</option>
            </select>
          </div>
        </div>
      </div>
  
      <!-- Botón Guardar -->
      <div class="d-flex justify-content-center align-items-center mt-4">
        <button type="submit" class="btn btn-danger w-50 rounded-pill overflow-hidden">Guardar</button>
      </div>
    </form>
  
    <!-- Mensaje de Error o Éxito -->
    <div v-if="message" class="mt-3 alert" :class="messageClass">
      {{ message }}
    </div>
  </div>
</template>
  
<script>
import ApiProcedure from '../api/ApiProcedure';
import ApiPond from '../api/ApiPond';
  
export default {
  data() {
    return {
      finca: '',
      estanque: '',
      tipoConcentrado: '',
      nombreProcedimiento: '',
      descripcionProcedimiento: '',
      observaciones: '',
      fincas: [],
      ponds: [], // Lista de estanques obtenida del backend
      isFormValid: false,
      message: '',
      messageClass: ''
    };
  },
  created() {
    this.fetchPonds();
  },
  computed: {
    // Filtrar estanques según la finca seleccionada
    estanquesFiltrados() {
      return this.ponds.filter(pond => pond.nombre_finca === this.finca);
    },
    // Obtener el objeto completo del estanque seleccionado
    selectedPond() {
      const id = parseInt(this.estanque, 10);
      console.log("mostrar id", this.estanque);
      return this.ponds.find(p => Number(p.numero_estanque) === id);
    }
  },
  methods: {
    async fetchPonds() {
      try {
        const response = await ApiPond.listEstanques();
        console.log("Estanques recibidos:", response);
        this.ponds = response;
        // Extraer las fincas únicas de los estanques
        this.fincas = [...new Map(response.map(pond => [pond.nombre_finca, { nombre: pond.nombre_finca }])).values()];
      } catch (error) {
        console.error("Error al obtener estanques:", error);
      }
    },
    checkFormValidity() {
      this.isFormValid =
        this.finca !== '' &&
        this.estanque !== '' &&
        this.tipoConcentrado !== '' &&
        this.nombreProcedimiento.trim() !== '' &&
        this.descripcionProcedimiento.trim() !== '';
    },
    async submitForm() {
      // Actualizar validación justo antes de enviar
      this.checkFormValidity();
      if (!this.isFormValid) {
        alert('Por favor, complete todos los campos obligatorios.');
        return;
      }
  
      console.log("Valor de 'estanque' antes de enviar:", this.estanque, typeof this.estanque);
  
      const parsedEstanque = Array.isArray(this.estanque)
        ? Number(this.estanque[0])
        : Number(this.estanque);
  
      if (!parsedEstanque) {
        alert('Por favor, seleccione un estanque.');
        return;
      }
      const procedureData = {
        nombre_finca: this.finca,
        // Se envía el id del estanque, que es la ForeignKey
        estanque: parsedEstanque,
        tipoConcentrado: this.tipoConcentrado,
        nombreProcedimiento: this.nombreProcedimiento,
        descripcionProcedimiento: this.descripcionProcedimiento,
        observaciones: this.observaciones
      };
  
      console.log("Datos enviados:", procedureData);
      console.log("Estanque seleccionado:", this.selectedPond);
  
      try {
        const response = await ApiProcedure.crearProcedimiento(procedureData);
        console.log('Procedimiento creado:', response);
        this.message = 'Procedimiento creado exitosamente!';
        this.messageClass = 'alert-success';
        // Reiniciar los campos del formulario
        this.finca = '';
        this.estanque = '';
        this.tipoConcentrado = '';
        this.nombreProcedimiento = '';
        this.descripcionProcedimiento = '';
        this.observaciones = '';
        this.isFormValid = false;
      } catch (error) {
        console.error('Error al crear procedimiento:', error.response?.data || error.message);
        this.message = 'Error al crear procedimiento: ' + (error.response?.data?.detail || error.message);
        this.messageClass = 'alert-danger';
      }
    }
  }
};
</script>
  
<style scoped>
.container {
  max-width: 60%;
  max-height: 30%;
  background-color: #f0f0f0c1;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 10px;
}
  
h3 {
  font-family: 'Arial', sans-serif;
  font-weight: bold;
  font-size: 2rem;
  margin-bottom: 1rem;
}
  
.form-label {
  font-size: 1.2rem;
  font-weight: bold;
}
</style>
