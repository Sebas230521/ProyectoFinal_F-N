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
    </div>
</template>

<script>
    export default {
        data() {
            return {
                form: {
                    numeroEstanque: '',
                    tipoEstanque: 'Geomembrana',
                    profundidad: '',
                    ancho: '',
                    largo: '',
                    especiePez: 'Mojarra Roja',
                    cantidad: '',
                    numeroAlimento: '',
                    fechaSiembra: ''
                }
            };
        },
        methods: {
            submitForm() {
            // Acción al enviar el formulario, puedes manejar los datos aquí o llamar a una API
            console.log('Formulario enviado:', this.form);
            }
        }
    };
</script>

<style scoped>
.form-group {
margin-bottom: 1rem;
}

button {
width: 100%;
}
</style>
  