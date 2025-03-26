<template>
  <div class="container form-container">
    <h3 class="text-center">Registro de procedimientos</h3>
    <form @submit.prevent="submitForm" class="needs-validation" novalidate>
      <div class="row g-3">
        <div class="col-md-6">
          <!-- Campo de Nombre del Responsable -->
          <div class="form-group">
            <label for="responsable" class="form-label">
              <i class="bi bi-person-fill"></i> Nombre del responsable
            </label>
            <input type="text" class="form-control" v-model="responsable" placeholder="Ingrese el nombre" @input="checkFormValidity" />
          </div>
  
          <!-- Campo de Selección de Estanque -->
          <div class="form-group">
            <label for="estanque" class="form-label">
              <i class="bi bi-hash"></i> Estanque
            </label>
            <select v-model="estanque" class="form-select" id="estanque" required @change="checkFormValidity">
              <option disabled value="">Seleccione</option>
              <option v-for="pond in ponds" :key="pond.id" :value="pond.id">
                {{ pond.numero_estanque }} - {{ pond.nombre }}
              </option>
            </select>
          </div>

          <!-- Campo de Observaciones -->
          <div class="form-group">
            <label for="observaciones" class="form-label">
              <i class="bi bi-eye"></i> Observaciones en el estanque
            </label>
            <input class="form-control" v-model="observaciones" placeholder="Observaciones" @input="checkFormValidity" />
          </div>
        </div>
        
        <div class="col-md-6">
          <!-- Campo de Descripción del Procedimiento -->
          <div class="form-group">
            <label for="descripcionProcedimiento" class="form-label">
              <i class="bi bi-file-earmark"></i> Descripción del procedimiento
            </label>
            <input class="form-control" v-model="descripcionProcedimiento" placeholder="Descripción" @input="checkFormValidity" />
          </div>

          <!-- Campo de Nombre del Procedimiento -->
          <div class="form-group">
            <label for="nombreProcedimiento" class="form-label">
              <i class="bi bi-file-earmark-text"></i> Nombre del procedimiento
            </label>
            <input type="text" class="form-control" v-model="nombreProcedimiento" placeholder="Nombre del procedimiento" @input="checkFormValidity" />
          </div>

          <!-- Mostrar si el nombre del procedimiento es "comida" -->
          <div class="form-group" v-if="nombreProcedimiento.toLowerCase() === 'comida'">
            <label for="tipoConcentrado" class="form-label">
              <i class="bi bi-card-checklist"></i> Tipo de concentrado
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

          <!-- Mostrar si el nombre del procedimiento NO es "comida" -->
          <div class="form-group" v-else>
            <label for="otroProcedimiento" class="form-label">
              <i class="bi bi-file-earmark-text"></i> Otro tipo de procedimiento
            </label>
            <input type="text" class="form-control" v-model="otroProcedimiento" placeholder="Escribe otro tipo de procedimiento" @input="checkFormValidity" />
          </div>



        </div>
      </div>

      <!-- Botón Guardar -->
      <div class="d-flex justify-content-center align-items-center mt-2">
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
  import ApiPond from '../api/ApiPond'; // Suponiendo que ApiPond tiene el método para listar estanques
  
  export default {
    data() {
      return {
        responsable: '',
        estanque: '', // Este campo ahora almacenará el ID del estanque seleccionado
        tipoConcentrado: '',
        nombreProcedimiento: '',
        descripcionProcedimiento: '',
        observaciones: '',
        ponds: [], // Lista de estanques obtenida del backend
        isFormValid: false,
        message: '',
        messageClass: ''
      };
    },
    created() {
      this.fetchPonds();
    },
    methods: {
      async fetchPonds() {
        try {
          const response = await ApiPond.listEstanques();
          this.ponds = response; // Se espera que sea un arreglo de objetos con { id, numero_estanque, nombre, ... }
        } catch (error) {
          console.error("Error al obtener estanques:", error);
        }
      },
      checkFormValidity() {
        // Se verifica que los campos obligatorios estén completos
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
        
        // Preparamos los datos del procedimiento
        const procedureData = {
          responsable: this.responsable,
          estanque: this.estanque, // Enviamos el ID del estanque seleccionado
          tipo_concentrado: this.tipoConcentrado,
          nombre_procedimiento: this.nombreProcedimiento,
          descripcion_procedimiento: this.descripcionProcedimiento,
          observaciones: this.observaciones
        };
  
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
max-height: 40%;
background-color: #f0f0f0;
padding: 2rem;
border-radius: 8px;
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
margin: auto;
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

i {
  font-weight: bold;
}
</style>
