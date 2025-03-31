<template>
  <div class="container form-container">
    <h3 class="text-center">Registro de procedimientos</h3>
    <form @submit.prevent="submitForm" class="needs-validation" novalidate>
      <!-- Nombre de la finca -->
      <div class="d-flex justify-content-center align-items-center mt-3">
        <div class="text-center w-50 form-group mt-3">
          <label for="finca" class="form-label">Nombre de la finca</label>
          <select v-model="finca" class="form-select" required>
            <option disabled value="">Seleccione</option>
            <option v-for="f in fincas" :key="f.id" :value="f.nombre">
              {{ f.nombre }}
            </option>
          </select>
        </div>
      </div>
      <div class="row g-3">
        <div class="col-md-6">
          <!-- Campo de Nombre del Responsable -->
          <div class="form-group mt-3">
            <label for="responsable" class="form-label">
              Nombre del responsable
            </label>
            <input type="text" class="form-control" v-model="responsable" placeholder="Ingrese el nombre" @input="checkFormValidity" />
          </div>
  
          <!-- Campo de Selección de Estanque -->
          <div class="form-group mt-3">
            <label for="estanque" class="form-label">
              Estanque
            </label>
            <select v-model="estanque" class="form-select" id="estanque" required @change="checkFormValidity">
              <option disabled value="">Seleccione</option>
              <option v-for="pond in ponds" :key="pond.id" :value="pond.id">
                {{ pond.numero_estanque }} - {{ pond.nombre }}
              </option>
            </select>
          </div>

          <!-- Campo de Observaciones -->
          <div class="form-group mt-3">
            <label for="observaciones" class="form-label">
              Observaciones en el estanque
            </label>
            <input class="form-control" v-model="observaciones" placeholder="Observaciones" @input="checkFormValidity" />
          </div>
        </div>
        
        <div class="col-md-6">
          <!-- Campo de Descripción del Procedimiento -->
          <div class="form-group mt-3">
            <label for="descripcionProcedimiento" class="form-label">
              Descripción del procedimiento
            </label>
            <input class="form-control" v-model="descripcionProcedimiento" placeholder="Descripción" @input="checkFormValidity" />
          </div>

          <!-- Campo de Nombre del Procedimiento -->
          <div class="form-group mt-3">
            <label for="nombreProcedimiento" class="form-label">
              Nombre del procedimiento
            </label>
            <input type="text" class="form-control" v-model="nombreProcedimiento" placeholder="Nombre del procedimiento" @input="checkFormValidity" />
          </div>

          <!-- Campo de Tipo de Concetrado -->
          <div class="form-group mt-3">
            <label for="tipoConcentrado" class="form-label">
              Tipo de concentrado
            </label>
            <select v-model="tipoConcentrado" class="form-select" @change="checkFormValidity">
              <option disabled value="">Seleccione</option>
              <option value="Alevinaje">Alevinaje 45%</option>
              <option value="PreJuveniles">PreJuveniles 38%</option>
              <option value="Juveniles">Juveniles 34%</option>
              <option value="PreEngorde">PreEngorde 30%</option>
              <option value="Engorde">Engorde 24%</option>
            </select>
          </div>

        </div>
      </div>

      <!-- Botón Guardar -->
      <div class="d-flex justify-content-center align-items-center mt-4">
        <button type="submit" class="btn btn-danger w-50">Guardar</button>
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
import ApiPond from '../api/ApiPond'; // Método para listar estanques

export default {
  data() {
    return {
      finca: '', // Nuevo campo
      responsable: '',
      // Inicialmente vacío, pero se llenará con el valor de pond.numero_estanque
      estanque: '',
      tipoConcentrado: '',
      nombreProcedimiento: '',
      descripcionProcedimiento: '',
      observaciones: '',
      fincas: [], // Lista de fincas obtenidas de ApiPond
      ponds: [], // Lista de estanques obtenida del backend
      isFormValid: false,
      message: '',
      messageClass: ''
    };
  },
  created() {
    this.fetchPonds();
  },
  watch: {
    // Para depuración: observa los cambios en 'estanque'
    estanque(newVal) {
      console.log("Watcher - nuevo valor de 'estanque':", newVal, typeof newVal);
    }
  },
  computed: { 
    // Retorna el objeto completo seleccionado basado en numero_estanque
    selectedPond() { //La propiedad computada selectedPond busca el objeto en ponds 
      const id = parseInt(this.estanque, 10);//parametro denomina radix y especifica que la cadena se debe interpretar en base 10 (decimal).
      console.log("mostrar id"+this.estanque);
      return this.ponds.find(p => Number(p.numero_estanque) === id);
    }
  },
  methods: {
    async fetchPonds() {
      try {
        const response = await ApiPond.listEstanques();
        console.log("Estanques recibidos:", response);
        this.ponds = response;

        // Extraer fincas únicas de la lista de estanques
        this.fincas = [...new Set(response.map(pond => pond.nombre_finca))];
      } catch (error) {
        console.error("Error al obtener estanques:", error);
      }
    },
    checkFormValidity() {
      this.isFormValid =
        this.responsable.trim() !== '' &&
        this.estanque !== '' &&
        this.tipoConcentrado !== '' &&
        this.nombreProcedimiento.trim() !== '' &&
        this.descripcionProcedimiento.trim() !== '';
    },
    async submitForm() {
      if (!this.isFormValid) {
        alert('Por favor, complete todos los campos obligatorios.');
        return;
      }
      
      console.log("Valor de 'estanque' antes de enviar:", this.estanque, typeof this.estanque);
      
      // Convertimos el valor seleccionado a entero. Si fuese un array (no debería ocurrir), tomamos el primer elemento.
      const parsedEstanque = Array.isArray(this.estanque)
        ? Number(this.estanque[0])
        : Number(this.estanque);
      
      if (!parsedEstanque) {
        alert("Seleccione un estanque válido.");
        return;
      }
      
      const procedureData = {
        responsable: this.responsable,
        // Enviamos el ID (que ahora es el numero_estanque) como valor
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
        // Reiniciamos los campos del formulario
        this.responsable = '';
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
background-color: #f0f0f0;
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

