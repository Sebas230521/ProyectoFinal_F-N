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
                        <input type="text" class="form-control" v-model="responsable" placeholder="Ingrese el nombre" @input="checkFormValidity" />
                    </div>
        
                    <!-- Campo de N.o estanque -->
                    <div class="mb-3">
                        <label for="estanque" class="form-label">
                            <i class="bi bi-hash"></i> N.o estanque
                        </label>
                        <input type="number" class="form-control" v-model="estanque" placeholder="Ingrese el número de estanque" @input="checkFormValidity" />
                    </div>
        
                    <!-- Campo de Tipo de Concentrado -->
                    <div class="mb-3">
                        <label for="tipoConcentrado" class="form-label">
                            <i class="bi bi-card-checklist"></i> Tipo de concentrado
                        </label>
                        <select v-model="tipoConcentrado" class="form-select" @change="checkFormValidity">
                            <option disabled value="">Seleccione</option>
                            <option value="45">Alevinaje</option>
                            <option value="38">Juveniles</option>
                            <option value="34">Juveniles</option>
                            <option value="30">Prejuveniles</option>
                            <option value="24">Engorde</option>
                        </select>
                    </div>
        
                    <!-- Campo de Nombre del Procedimiento -->
                    <div class="mb-3">
                        <label for="nombreProcedimiento" class="form-label">
                            <i class="bi bi-file-earmark-text"></i> Nombre del procedimiento
                        </label>
                        <input type="text" class="form-control" v-model="nombreProcedimiento" placeholder="Nombre del procedimiento" @input="checkFormValidity" />
                    </div>
        
                    <!-- Campo de Descripción del Procedimiento -->
                    <div class="mb-3">
                        <label for="descripcionProcedimiento" class="form-label">
                            <i class="bi bi-file-earmark"></i> Descripción del procedimiento
                        </label>
                        <textarea class="form-control" v-model="descripcionProcedimiento" placeholder="Descripción" @input="checkFormValidity"></textarea>
                    </div>
        
                    <!-- Campo de Observaciones -->
                    <div class="mb-3">
                        <label for="observaciones" class="form-label">
                            <i class="bi bi-eye"></i> Observaciones
                        </label>
                        <textarea class="form-control" v-model="observaciones" placeholder="Observaciones" @input="checkFormValidity"></textarea>
                    </div>
        
                    <!-- Botón de Guardar -->
                    <div class="d-grid mt-3">
                        <button type="submit" class="btn btn-success" :disabled="!isFormValid">Guardar</button>
                    </div>
                </form>
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
    export default {
        data() {
            return {
                responsable: '',
                estanque: '',
                tipoConcentrado: '',
                nombreProcedimiento: '',
                descripcionProcedimiento: '',
                observaciones: '',
                isFormValid: false,  // Estado de validez del formulario
            };
        },
        methods: {
            checkFormValidity() {
                // Verifica que los campos obligatorios estén completos
                this.isFormValid =
                this.responsable.trim() !== '' &&
                this.estanque.trim() !== '' &&
                this.tipoConcentrado !== '' &&
                this.nombreProcedimiento.trim() !== '' &&
                this.descripcionProcedimiento.trim() !== '';
            },
            submitForm() {
                if (this.isFormValid) {
                console.log('Formulario enviado con los siguientes datos:', {
                    responsable: this.responsable,
                    estanque: this.estanque,
                    tipoConcentrado: this.tipoConcentrado,
                    nombreProcedimiento: this.nombreProcedimiento,
                    descripcionProcedimiento: this.descripcionProcedimiento,
                    observaciones: this.observaciones,
                });
                // Lógica para enviar los datos o hacer algo con ellos
                } else {
                alert('Por favor, complete todos los campos obligatorios.');
                }
            },
        },
    };
</script>

<style scoped>
    /* .position-fixed {
    position: fixed;
    } */
</style>
