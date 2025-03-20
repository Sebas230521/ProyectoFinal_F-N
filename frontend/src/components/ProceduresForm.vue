<template>
    <div class="container vh-100 d-flex justify-content-center align-items-center">
      <div class="row d-flex justify-content-center align-items-center w-100">
        <div class="card col-lg-6 col-md-8 col-sm-10 p-4 shadow">
          <form @submit.prevent="submitForm">
            <div class="text-center">
              <img src="@/assets/Logo_Fish-Nexus.png" alt="Fish Nexus Logo" class="mb-4" />
              <h4>Registro de procedimientos</h4>
            </div>
  
            <!-- Campo de Nombre del Responsable -->
            <div class="mb-3">
              <label for="responsable" class="form-label">
                <i class="bi bi-person-fill"></i> Nombre del responsable
              </label>
              <input
                type="text"
                class="form-control"
                v-model="responsable"
                placeholder="Ingrese el nombre"
                @input="checkFormValidity"
              />
            </div>
  
            <!-- Campo de Selección de Estanque -->
            <div class="mb-3">
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
  
            <!-- Campo de Tipo de Concentrado -->
            <div class="mb-3">
              <label for="tipoConcentrado" class="form-label">
                <i class="bi bi-card-checklist"></i> Tipo de concentrado
              </label>
              <select v-model="tipoConcentrado" class="form-select" @change="checkFormValidity">
                <option disabled value="">Seleccione</option>
                <option value="Alevinaje">Alevinaje</option>
                <option value="Juveniles">Juveniles</option>
                <option value="Prejuveniles">Prejuveniles</option>
                <option value="Engorde">Engorde</option>
              </select>
            </div>
  
            <!-- Campo de Nombre del Procedimiento -->
            <div class="mb-3">
              <label for="nombreProcedimiento" class="form-label">
                <i class="bi bi-file-earmark-text"></i> Nombre del procedimiento
              </label>
              <input
                type="text"
                class="form-control"
                v-model="nombreProcedimiento"
                placeholder="Nombre del procedimiento"
                @input="checkFormValidity"
              />
            </div>
  
            <!-- Campo de Descripción del Procedimiento -->
            <div class="mb-3">
              <label for="descripcionProcedimiento" class="form-label">
                <i class="bi bi-file-earmark"></i> Descripción del procedimiento
              </label>
              <textarea
                class="form-control"
                v-model="descripcionProcedimiento"
                placeholder="Descripción"
                @input="checkFormValidity"
              ></textarea>
            </div>
  
            <!-- Campo de Observaciones -->
            <div class="mb-3">
              <label for="observaciones" class="form-label">
                <i class="bi bi-eye"></i> Observaciones
              </label>
              <textarea
                class="form-control"
                v-model="observaciones"
                placeholder="Observaciones"
                @input="checkFormValidity"
              ></textarea>
            </div>
  
            <!-- Botón de Guardar -->
            <div class="d-grid mt-3">
              <button type="submit" class="btn btn-success" :disabled="!isFormValid">
                Guardar
              </button>
            </div>
          </form>
  
          <!-- Mensaje de Error o Éxito -->
          <div v-if="message" class="mt-3 alert" :class="messageClass">
            {{ message }}
          </div>
        </div>
      </div>
  
      <!-- Botón de Ayuda -->
      <div class="position-fixed top-0 end-0 p-3">
        <button class="btn btn-outline-info">
          <i class="bi bi-question-circle"></i>
        </button>
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
  .form-group {
    margin-bottom: 1rem;
  }
  </style>
  