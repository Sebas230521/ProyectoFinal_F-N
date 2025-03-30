<template>
  <div class="container form-container">
    <h3 class="text-center">Añadir nuevo estanque</h3>
    <form @submit.prevent="submitForm" class="needs-validation" novalidate>
      <div class="row g-3">
        <div class="col-md-4">
          <!-- N° estanque -->
          <div class="form-group">
            <label for="numeroEstanque" class="form-label">N° estanque</label>
            <input type="number" v-model="form.numeroEstanque" class="form-control" id="numeroEstanque" required />
          </div>

          <!-- Tipo de estanque -->
          <div class="form-group">
            <label for="tipoEstanque" class="form-label">Tipo de estanque</label>
            <select v-model="form.tipoEstanque" class="form-control" id="tipoEstanque" required>
              <option value="Seleccione">Seleccione</option>
              <option value="Geomembrana">Geomembrana</option>
              <option value="Tierra">Tierra</option>
            </select>
          </div>

          <!-- Profundidad -->
          <div class="form-group">
            <label for="profundidad" class="form-label">Profundidad (m)</label>
            <input type="number" v-model="form.profundidad" class="form-control" id="profundidad" required />
          </div>
        </div>

        <div class="col-md-4">
          <!-- Ancho -->
          <div class="form-group">
            <label for="ancho" class="form-label">Ancho (m)</label>
            <input type="number" v-model="form.ancho" class="form-control" id="ancho" required />
          </div>

          <!-- Largo -->
          <div class="form-group">
            <label for="largo" class="form-label">Largo (m)</label>
            <input type="number" v-model="form.largo" class="form-control" id="largo" required />
          </div>

          <!-- Especie de pez -->
          <div class="form-group">
            <label for="especiePez" class="form-label">Especie de pez</label>
            <select v-model="form.especiePez" class="form-control" id="especiePez" required>
              <option value="">Seleccione</option>
              <option value="Mojarra Roja">Mojarra Roja</option>
              <option value="Mojarra Negra">Mojarra Negra</option>
              <option value="Cachama">Cachama</option>
            </select>
          </div>
        </div>

        <div class="col-md-4">
          <!-- Cantidad -->
          <div class="form-group">
            <label for="cantidad" class="form-label">Cantidad de peces</label>
            <input type="number" v-model="form.cantidad" class="form-control" id="cantidad" required />
          </div>

          <!-- N° alimento -->
          <div class="form-group">
            <label for="numeroAlimento" class="form-label">N° alimento</label>
            <input type="number" v-model="form.numeroAlimento" class="form-control" id="numeroAlimento" required />
          </div>

          <!-- Fecha de sembrado -->
          <div class="form-group">
            <label for="fechaSiembra" class="form-label">Fecha de sembrado</label>
            <input type="date" v-model="form.fechaSiembra" class="form-control" id="fechaSiembra" required />
          </div>
        </div>
      </div>

      <!-- Botón Guardar -->
      <div class="d-flex justify-content-center align-items-center mt-3">
        <button type="submit" class="btn btn-danger w-50">Guardar</button>
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
      messageClass: '' // Clase de estilo para el mensaje
    };
  },
  methods: {
    async submitForm() {
      try {
        // Transformamos los datos para que tengan nombres en snake_case
        const transformedData = {
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

        await ApiPond.createEstanque(transformedData); // Llamamos a la API con los datos transformados

        this.message = 'Estanque creado exitosamente!';
        this.messageClass = 'alert-success'; // Estilo de éxito

        // Limpiamos el formulario después de la creación
        this.form = {
          numeroEstanque: '',
          tipoEstanque: '',
          profundidad: '',
          ancho: '',
          largo: '',
          especiePez: '',
          cantidad: '',
          numeroAlimento: '',
          fechaSiembra: ''
        };
      } catch (error) {
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
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);

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
</style>