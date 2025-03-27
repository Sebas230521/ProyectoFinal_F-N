<template>
        <div class="container-fluid background-custom min-vh-100 d-flex flex-column align-items-start">
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
                        <PondView />
                </div>

                <!-- Modal para mostrar la ayuda -->
                <div class="modal" tabindex="-1" :class="{ 'd-block': showModal }">
                        <div class="modal-dialog">
                                <div class="modal-content">
                                        <div class="modal-header">
                                                <button type="button" class="btn-close" @click="closeHelp"></button>
                                                <h5 class="modal-title">Ayuda:</h5>
                                                <h5 class="modal-title">Nuevo estanque</h5>
                                        </div>
                                        <div class="modal-body">
                                                <p>Aquí puedes añadir un nuevo estanque de manera eficiente. Debes completar los siguientes campos:</p>
                                                <ul>
                                                        <li><strong>Número del estanque:</strong> Debes ingresar el número de identificación del estanque.</li>
                                                        <li><strong>Tipo de estanque:</strong> Seleccionar el tipo de estanque según su clasificación (natural, artificial, etc.).</li>
                                                        <li><strong>Profundidad:</strong> Especificar la profundidad del estanque en metros.</li>
                                                        <li><strong>Ancho:</strong> Ingresar el ancho del estanque en metros.</li>
                                                        <li><strong>Largo:</strong> Ingresar el largo del estanque en metros.</li>
                                                        <li><strong>Especie de pez:</strong> Indicar la especie de pez que está siendo cultivada en el estanque.</li>
                                                        <li><strong>Cantidad de peces:</strong> Seleccione la cantidad de peces que hay en el estanque.</li>
                                                        <li><strong>Número de alimento:</strong> Ingresar el número o tipo de alimento utilizado en el estanque.</li>
                                                        <li><strong>Fecha de siembra:</strong> Indicar la fecha en la que se sembraron los peces en el estanque.</li>
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
import PondView from '@/components/PondView.vue';

export default {
        components: {
                PondView,
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
padding-bottom: 3rem;
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