<template>
                <div class="container-fluid background-custom min-vh-100 d-flex flex-column align-items-start">
                        <!-- Contenedor de botones e imagen -->
                        <div class="w-100 d-flex justify-content-between align-items-center mt-3 p-2">
                                <button class="btn btn-danger" @click="goToMenu">
                                <i class="bi bi-box-arrow-left"></i> Atrás
                                </button>
                
                                <button class="btn btn-secondary" @click="showHelp">
                                <i class="bi bi-question-circle"></i>
                                </button>
                        </div>
                
                        <div class="w-100 px-3 mt-5">
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
                                                <li><strong>Nombre de la finca:</strong> Seleccionar el nombre de la finca que registro en el nuevo estanque.</li>
                                                <li><strong>Descripción del procedimiento:</strong> Incluir una breve descripción del procedimiento.</li>
                                                <li><strong>Estanque:</strong> Seleccionar el estanque al cual le va a realizar el procedimiento.</li>
                                                <li><strong>Nombre del procedimiento:</strong> Ingrese el nombre con el cual identifique el procedimiento realizado ya sea alimentación, limpieza, recambio, etc.</li>
                                                <li><strong>Observaciones en el estanque:</strong> Ingresar una breve descripción de qué irregularidades vio en el estanque, tales como peces muertos, agua de coloración muy oscura, desbordamiento del lago, etc.</li>
                                                <li><strong>Tipo de concentrado:</strong> Seleccionar el tipo de concentrado que está utilizando el estanque seleccionado en el registro.</li>
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
        background-color: #434343;
}

/* Imagen centrada correctamente */
/* .logo-centered {
position: absolute;
left: 50%;
transform: translateX(-50%);
max-width: 100px; /* Ajusta el tamaño según necesidad */
/* height: auto; */
/* }*/ 


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
background-color: #e2d5bd;
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

.modal-body {
        font-family: 'Roboto', sans-serif;
        font-size: 16px;
}
</style>