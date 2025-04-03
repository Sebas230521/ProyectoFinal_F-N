<template>
  <div class="container form-container">
    <!-- Modal de Sugerencia de Peces -->
<div :class="['modal', { 'd-block': mostrarModalSugerencia }]">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="btn-close" @click="cerrarModalSugerencia"></button>
        <div class="container_info">
          <h5 class="text-modal text-center">Sugerencia de peces</h5>
        </div>
      </div>
      <div class="modal-body">
        <p>Basado en las dimensiones del estanque, puedes sembrar entre <strong>{{ sugerenciaMin }}</strong> y <strong>{{ sugerenciaMax }}</strong> peces.</p>
      </div>
    </div>
  </div>
</div>

<!-- Modal de Advertencia por Exceso -->
<div :class="['modal', { 'd-block': mostrarModalExceso }]">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="btn-close" @click="cerrarModalExceso"></button>
        <div class="container_info">
          <h5 class="text-modal text-center">⚠️ Advertencia</h5>
        </div>
      </div>
      <div class="modal-body">
        <p>Has ingresado una cantidad superior a la recomendada. El máximo recomendado es <strong>{{ sugerenciaMax }}</strong> peces.</p>
      </div>
    </div>
  </div>
</div>

<!-- Modal de Advertencia por Cantidad Insuficiente -->
<div :class="['modal', { 'd-block': mostrarModalInsuficiente }]">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="btn-close" @click="cerrarModalInsuficiente"></button>
        <div class="container_info">
          <h5 class="text-modal text-center">⚠️ Advertencia</h5>
        </div>
      </div>
      <div class="modal-body">
        <p>La cantidad ingresada es menor a la recomendada. El mínimo recomendado es <strong>{{ sugerenciaMin }}</strong> peces.</p>
      </div>
    </div>
  </div>
</div>

    <h3 class="text-center">Añadir nuevo estanque</h3>
    <form @submit.prevent="submitForm" class="needs-validation" novalidate>
      <!-- Nombre de la finca -->
      <div class="d-flex justify-content-center align-items-center mt-3">
        <div class="container-finca text-center form-group">
          <label for="nombreFinca" class="form-label">Nombre de la finca</label>
          <input type="text" v-model="form.nombreFinca" class="form-control  rounded-pill overflow-hidden" id="nombreFinca" required />
        </div>
      </div>
      <div class="row g-3">
        <div class="col-md-4">
          <!-- N° estanque -->
          <div class="form-group">
            <label for="numeroEstanque" class="form-label">N° estanque</label>
            <input type="number" v-model="form.numeroEstanque" class="form-control  rounded-pill overflow-hidden" id="numeroEstanque" required />
          </div>

          <!-- Ancho -->
          <div class="form-group">
            <label for="ancho" class="form-label">Ancho (m)</label>
            <input type="number" v-model="form.ancho" class="form-control rounded-pill overflow-hidden" id="ancho" required />
          </div>

          <!-- Cantidad -->
          <div class="form-group">
            <label for="cantidad" class="form-label">Cantidad de peces</label>
            <input type="number" v-model="form.cantidad" class="form-control  rounded-pill overflow-hidden" id="cantidad" required />
          </div>
        </div>

        <div class="col-md-4">
          <!-- Tipo de estanque -->
          <div class="form-group">
            <label for="tipoEstanque" class="form-label">Tipo de estanque</label>
            <select v-model="form.tipoEstanque" class="form-control  rounded-pill overflow-hidden" id="tipoEstanque" required>
              <option value="Seleccione">Seleccione</option>
              <option value="Geomembrana">Geomembrana</option>
              <option value="Tierra">Tierra</option>
            </select>
          </div>

          <!-- Largo -->
          <div class="form-group">
            <label for="largo" class="form-label">Largo (m)</label>
            <input type="number" v-model="form.largo" class="form-control rounded-pill overflow-hidden" id="largo" required />
          </div>

          <!-- N° alimento -->
          <div class="form-group">
            <label for="numeroAlimento" class="form-label">N° alimento</label>
            <input type="number" v-model="form.numeroAlimento" class="form-control  rounded-pill overflow-hidden" id="numeroAlimento" required />
          </div>
        </div>

        <div class="col-md-4">
          <!-- Especie de pez -->
          <div class="form-group">
            <label for="especiePez" class="form-label">Especie de pez</label>
            <select v-model="form.especiePez" class="form-control rounded-pill overflow-hidden" id="especiePez" required>
              <option value="">Seleccione</option>
              <option value="Mojarra Roja">Mojarra Roja</option>
              <option value="Mojarra Negra">Mojarra Negra</option>
              <option value="Cachama">Cachama</option>
            </select>
          </div>

          <!-- Profundidad -->
          <div class="form-group">
            <label for="profundidad" class="form-label">Profundidad (m)</label>
            <input type="number" v-model="form.profundidad" class="form-control rounded-pill overflow-hidden" id="profundidad" required />
          </div>

          <!-- Fecha de sembrado -->
          <div class="form-group">
            <label for="fechaSiembra" class="form-label">Fecha de sembrado</label>
            <input type="date" v-model="form.fechaSiembra" class="form-control  rounded-pill overflow-hidden" id="fechaSiembra" required />
          </div>
        </div>
      </div>

      <!-- Botón Guardar -->
      <div class="d-flex justify-content-center align-items-center mt-3">
        <button type="submit" class="btn btn-danger w-50  rounded-pill overflow-hidden">Guardar</button>
      </div>
    </form>

    <!-- Mensaje de Éxito o Error -->
    <div v-if="message" class="mt-3 alert" :class="messageClass">
      {{ message }}
    </div>
  </div>
</template>

<script>
import ApiPond from '../api/ApiPond';

export default {
  data() {
    return {
      form: {
        nombreFinca: '', // Nuevo campo
        numeroEstanque: '',
        tipoEstanque: '',
        profundidad: '',
        ancho: '',
        largo: '',
        especiePez: '',
        cantidad: '',
        numeroAlimento: '',
        fechaSiembra: ''
      },
      message: '', // Mensaje de éxito o error
      messageClass: '', // Clase de estilo para el mensaje
      mostrarModalSugerencia: false, // Modal para sugerencias
      mostrarModalExceso: false, // Modal para cantidad mayor a la recomendada
      mostrarModalInsuficiente: false, // Modal para cantidad menor a la recomendada
      sugerenciaMin: 0, // Cantidad mínima sugerida
      sugerenciaMax: 0, // Cantidad máxima sugerida
    };
  },
  watch: {
    form: {
      handler() {
        this.calcularSugerencia();
        this.validarCantidad();
      },
      deep: true,
    },
  },
  methods: {
    calcularSugerencia() {
      const { largo, ancho, profundidad, especiePez } = this.form;

      const l = parseFloat(largo) || 0;
      const a = parseFloat(ancho) || 0;
      const p = parseFloat(profundidad) || 0;

      if (!l || !a || !p || !especiePez) {
        this.mostrarModalSugerencia = false;
        return;
      }

      const volumen = l * a * p;

      if (especiePez === 'Cachama') {
        this.sugerenciaMin = Math.floor(volumen * 10);
        this.sugerenciaMax = Math.floor(volumen * 20);
      } else if (especiePez === 'Mojarra Roja' || especiePez === 'Mojarra Negra') {
        this.sugerenciaMin = Math.floor(volumen * 20);
        this.sugerenciaMax = Math.floor(volumen * 50);
      } else {
        this.sugerenciaMin = 0;
        this.sugerenciaMax = 0;
      }

      if (this.sugerenciaMin > 0) {
        this.mostrarModalSugerencia = true;
      }
    },
    validarCantidad() {
      const cantidadIngresada = parseInt(this.form.cantidad) || 0;

      if (cantidadIngresada === 0 || this.sugerenciaMin === 0) {
        this.mostrarModalExceso = false;
        this.mostrarModalInsuficiente = false;
        return;
      }

      if (cantidadIngresada > this.sugerenciaMax) {
        this.mostrarModalExceso = true;
        this.mostrarModalInsuficiente = false;
      } else if (cantidadIngresada < this.sugerenciaMin) {
        this.mostrarModalInsuficiente = true;
        this.mostrarModalExceso = false;
      } else {
        this.mostrarModalExceso = false;
        this.mostrarModalInsuficiente = false;
      }
    },
    cerrarModalSugerencia() {
      this.mostrarModalSugerencia = false;
    },
    cerrarModalExceso() {
      this.mostrarModalExceso = false;
    },
    cerrarModalInsuficiente() {
      this.mostrarModalInsuficiente = false;
    },
    async submitForm() {
      console.log("Intentando guardar el estanque...");
      try {
        // Transformamos los datos para que tengan nombres en snake_case
        const transformedData = {
          nombre_finca: this.form.nombreFinca.trim(), // Elimina espacios extra
          numero_estanque: this.form.numeroEstanque,
          tipo_estanque: this.form.tipoEstanque,
          profundidad: this.form.profundidad,
          ancho: this.form.ancho,
          largo: this.form.largo,
          especie_pez: this.form.especiePez,
          cantidad: this.form.cantidad,
          numero_alimento: this.form.numeroAlimento,
          fecha_siembra: this.form.fechaSiembra
        };

        console.log("Datos enviados a la API:", transformedData);

        await ApiPond.createEstanque(transformedData); // Llamamos a la API con los datos transformados

        this.message = 'Estanque creado exitosamente!';
        this.messageClass = 'alert-success'; // Estilo de éxito
      } catch (error) {
        console.error("Error en la API:", error);
        this.message = 'Error al crear el estanque, Ya existe un estanque con ese número: ' + (error.response?.data?.detail || error.message);
        this.messageClass = 'alert-danger';
      }
    }
  }
};
</script>


<style scoped>
.container {
  max-width: 80%;
  max-height: 50%;
  background-color: #f0f0f0;
  padding: 2rem;
  border-radius: 8px;
  background-color: #f0f0f0c1;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: auto;
}

h3 {
  font-family: 'Arial', sans-serif;
  font-weight: bold;
  font-size: 2rem;
  margin-bottom: 1rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-label {
  font-size: 1.2rem;
  font-weight: bold;
}

button {
  max-width: 25%;
  font-size: 1.2rem;
  border-radius: 10px;
  font-weight: bold;
}

@media (max-width: 768px) {
  .container {
    max-width: 95%;
  }
  
  h3 {
    font-size: 1.5rem;
  }

  .form-group {
    margin-bottom: 0.5rem;
  }

  button {
    font-size: 1rem;
  }
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: none;
  align-items: center;
  justify-content: center;
}

.modal.d-block {
  display: flex;
}

.modal-dialog {
  max-width: 500px;
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
}

.modal-header {
  display: flex;
  flex-direction: column;
}

.container_info {
  padding: 10px 10px 0px 10px;
  border-radius: 10px;
  background-color: #df5814;
}

.text-modal {
  color: #fff;
}


.modal-body {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
}

.container-finca {
  width: 35%;
}
</style>