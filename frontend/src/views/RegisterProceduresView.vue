<template>
        <div class="container-fluid background-custom max-vh-100 d-flex flex-column align-items-start">
                <!-- Botones de "Salir" y "Ayuda" -->
                <div class="w-100 d-flex justify-content-between align-items-center mt-3 p-2">
                        <button class="btn btn-danger" @click="goToMenu">
                                <i class="bi bi-box-arrow-left"></i> Atras
                        </button>
                        <button class="btn-help btn btn-Secondary" @click="showHelp">
                                <i class="bi bi-question-circle"></i> Ayuda
                        </button>
                </div>

                <!-- Contenido principal -->
                <div class="col-12 d-flex justify-content-center mt-2">
                        <img src="../assets/logoMenuLBlanca.png" alt="Logo" class="img-fluid logo-responsive">
                </div>
                <div class="w-100 px-3 mt-4">
                        <ProceduresForm />
                </div>

                <!-- Modal para mostrar la ayuda -->
                <div class="modal" tabindex="-1" :class="{ 'd-block': showModal }">
                        <div class="modal-dialog">
                                <div class="modal-content">
                                        <div class="modal-header">
                                                <button type="button" class="btn-close" @click="closeHelp"></button>
                                                <h5 class="modal-title">Ayuda:</h5>
                                                <h5 class="modal-title">Registro de Procedimientos</h5>
                                        </div>
                                        <div class="modal-body">
                                                <p>Aquí puedes registrar los procedimientos de manera eficiente. Debes completar los siguientes campos:</p>
                                                <ul>
                                                        <li><strong>Nombre del responsable:</strong> Debes escribir el nombre completo de la persona que esta realizando el procedimiento.</li>
                                                        <li><strong>Descripción del procedimiento:</strong> Incluir una breve descripción del procedimiento.</li>
                                                        <li><strong>Estanque:</strong> seleccionar el estanque al cual le esta realizando el procedimiento.</li>
                                                        <li><strong>Nombre del procedimiento:</strong> Poner un nombre al procedimiento realizado ya sea alimentación, limpieza, recambio, etc.</li>
                                                        <li><strong>Observaciones en el estanque:</strong> Hacer una breve descripción de que irregularidad vio en el estanque, tales como peces muertos, agua de coloración muy oscura, desbordamiento del lago, etc.</li>
                                                        <li><strong>Tipo de concentrado:</strong> Seleccionar el tipo de concentrado que esta utilizando el estanque seleccionado en el registro.</li>
                                                </ul>
                                                <div class="container_info d-flex justify-content-center">
                                                        <p class="text-center"><strong>Una vez completados todos los campos, presiona el botón "Guardar" para registrar el procedimiento.</strong></p>
                                                </div>
                                        </div>
                                </div>
                        </div>
                </div>
        </div>
</template>

<script>
import ProceduresForm from '@/components/ProceduresForm.vue';

export default {
        components: {
                ProceduresForm,
        },
        data() {
                return {
                        showModal: false, // Controla la visibilidad del modal
                };
        },
        methods: {
                goToMenu() {
                        this.$router.push({ name: 'menu' });
                },
                showHelp() {
                        this.showModal = true; // Muestra el modal cuando se presiona el botón de ayuda
                },
                closeHelp() {
                        this.showModal = false; // Cierra el modal
                }
        },
};
</script>

<style scoped>
.background-custom {
padding-top: -2rem;

background: linear-gradient(to bottom, #033450, #F56217);
}

.logo-responsive {
max-width: 90%;
height: auto;
max-height: 150px;
}

.mt-2 {
margin-top: 0.5rem;
}

.mt-4 {
margin-top: 1.5rem;
}

/* Estilos para el modal */
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

.btn-help {
        background-color: #D9D9D9;
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

.text-center {
        color: #fff;
}
</style>