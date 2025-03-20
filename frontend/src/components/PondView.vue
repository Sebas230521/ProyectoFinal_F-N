<template>
  <div class="container mt-4">
      <h3 class="text-center">Añadir nuevo estanque</h3>
      <form @submit.prevent="submitForm">
          <!-- No Estanque -->
          <div class="form-group">
              <label for="numeroEstanque">
                  <i class="fas fa-clipboard-list"></i> N° estanque
              </label>
              <input type="number" v-model="form.numeroEstanque" class="form-control" id="numeroEstanque" required/>
          </div>
  
          <!-- Tipo de Estanque -->
          <div class="form-group">
              <label for="tipoEstanque">
                  <i class="fas fa-box"></i> Tipo de estanque
              </label>
              <select v-model="form.tipoEstanque" class="form-control" id="tipoEstanque" required>
                  <option value="Seleccione">Seleccione</option>
                  <option value="Geomembrana">Geomembrana</option>
                  <option value="Tierra">Tierra</option>
              </select>
          </div>
  
          <!-- Profundidad -->
          <div class="form-group">
              <label for="profundidad">
                  <i class="fas fa-water"></i> Profundidad (m)
              </label>
              <input type="number" v-model="form.profundidad" class="form-control" id="profundidad" required/>
          </div>
  
          <!-- Ancho -->
          <div class="form-group">
              <label for="ancho">Ancho (m)</label>
              <input type="number" v-model="form.ancho" class="form-control" id="ancho" required/>
          </div>
  
          <!-- Largo -->
          <div class="form-group">
              <label for="largo">Largo (m)</label>
              <input type="number" v-model="form.largo" class="form-control" id="largo" required/>
          </div>
  
          <!-- Especie de pez -->
          <div class="form-group">
              <label for="especiePez">
                  <i class="fas fa-fish"></i> Especie de pez
              </label>
              <select v-model="form.especiePez" class="form-control" id="especiePez" required>
                  <option value="">Seleccione</option>
                  <option value="Mojarra Roja">Mojarra Roja</option>
                  <option value="Mojarra Negra">Mojarra Negra</option>
                  <option value="Cachama">Cachama</option>
              </select>
          </div>
  
          <!-- Cantidad -->
          <div class="form-group">
              <label for="cantidad">Cantidad</label>
              <input type="number" v-model="form.cantidad" class="form-control" id="cantidad" required/>
          </div>
  
          <!-- Número de alimento -->
          <div class="form-group">
              <label for="numeroAlimento">N° alimento</label>
              <input type="number" v-model="form.numeroAlimento" class="form-control" id="numeroAlimento" required/>
          </div>
  
          <!-- Fecha de sembrado -->
          <div class="form-group">
              <label for="fechaSiembra">Fecha de sembrado</label>
              <input type="date" v-model="form.fechaSiembra" class="form-control" id="fechaSiembra" required/>
          </div>
  
          <!-- Botón de Guardar -->
          <button type="submit" class="btn btn-success">Guardar</button>
      </form>

      <!-- Mensaje de Error o Éxito -->
      <div v-if="message" class="mt-3 alert" :class="messageClass">
          {{ message }}
      </div>
  </div>
</template>

<script>
import ApiPond from '../api/ApiPond'; // Asegúrate de que la ruta sea correcta

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
.form-group {
  margin-bottom: 1rem;
}
</style>
