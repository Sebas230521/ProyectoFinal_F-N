<template>
  <div class="container mt-4" >
    <h3 class="b text-center" style="font-size: 2rem; font-family: 'Arial', sans-serif; font-weight: bold;" >Añadir nuevo estanque</h3>
    <form @submit.prevent="submitForm" class="needs-validation" novalidate>
      <div class="form-group row">
        <div class="col-md-4">

          <!-- No Estanque -->
          <div class="form-group">
              <label for="numeroEstanque" style="font-size: 1.2rem; font-weight: bold;">
                  <i class="fas fa-clipboard-list"></i> N° estanque
              </label>
              <input type="number" v-model="form.numeroEstanque" class="form-control" id="numeroEstanque" required />
          </div>

          <!-- Tipo de Estanque -->
          <div class="form-group">
              <label for="tipoEstanque" style="font-size: 1.2rem; font-weight: bold;">
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
              <label for="profundidad" style="font-size: 1.2rem; font-weight: bold;">
                  <i class="fas fa-water"></i> Profundidad (m)
              </label>
              <input type="number" v-model="form.profundidad" class="form-control" id="profundidad" required />
          </div>

        </div>
        
        <div class="col-md-4">
          <!-- Ancho -->
          <div class="form-group">
              <label for="ancho" style="font-size: 1.2rem; font-weight: bold;">Ancho (m)</label>
              <input type="number" v-model="form.ancho" class="form-control" id="ancho" required />
          </div>
          
          <!-- Largo -->
          <div class="form-group">
              <label for="largo" style="font-size: 1.2rem; font-weight: bold;">Largo (m)</label>
              <input type="number" v-model="form.largo" class="form-control" id="largo" required />
          </div>

          <!-- Especie de pez -->
          <div class="form-group">
              <label for="especiePez" style="font-size: 1.2rem; font-weight: bold;">
                  <i class="fas fa-fish"></i> Especie de pez
              </label>
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
              <label for="cantidad" style="font-size: 1.2rem; font-weight: bold;">Cantidad de peces</label>
              <input type="number" v-model="form.cantidad" class="form-control" id="cantidad" required />
          </div>
    
          <!-- Número de alimento -->
          <div class="form-group">
              <label for="numeroAlimento" style="font-size: 1.2rem; font-weight: bold;">N° alimento</label>
              <input type="number" v-model="form.numeroAlimento" class="form-control" id="numeroAlimento" required />
          </div>
    
          <!-- Fecha de sembrado -->
          <div class="form-group">
              <label for="fechaSiembra" style="font-size: 1.2rem; font-weight: bold;">Fecha de sembrado</label>
              <input type="date" v-model="form.fechaSiembra" class="form-control" id="fechaSiembra" required />
          </div>

        </div>
      </div>
      
      <!-- Botón de Guardar -->
      <div class="d-flex justify-content-center align-items-center mb-3 form-group">
        <button type="submit" class="btn btn-danger  w-50">
          Guardar
        </button> 
      </div>
      
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
  head() {
    return {
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: 'true' },
        { href: 'https://fonts.googleapis.com/css2?family=Boldonse&display=swap', rel: 'stylesheet' }
      ]
    };
  },
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
  max-width: 60%;
  background-color: #f0f0f0;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.form-control {
  font-size: 1rem;
  border-radius: 4px;
  padding: 10px;
}

button {
  max-width: 30%;
  border-radius: 10px;
  font-size: 1.2rem;
  font-weight: bold;
}

h3 {
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

b {
  color: #e67e22,
}
</style>

