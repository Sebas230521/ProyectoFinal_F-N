<template>
    <div class="container ">
        <div class="card-register text-center mb-4">
            <h1>Crea una cuenta</h1>
            <p><strong>Empieza a disfrutar de nuestros servicios hoy mismo.</strong></p>
        </div>
        <form @submit.prevent="registro">
            <div class="row justify-content-center ">
                <div class="col-10 col-md-8 col-lg-10 col-sm-8">
                    <div class="mb-3 input-group rounded-pill overflow-hidden">
                        <span class="input-group-text"><i class="fas fa-user"></i></span>
                        <input type="text" placeholder="Nombre usuario" class="form-control " v-model="user.nombre" required>
                    </div>
                    <div class="mb-3 input-group rounded-pill overflow-hidden">
                        <span class="input-group-text"><i class="fas fa-phone"></i></span>
                        <input type="tel" placeholder="Celular" class="form-control" v-model="user.celular" required>
                    </div>
                    <div class="mb-3 input-group rounded-pill overflow-hidden">
                        <span class="input-group-text"><i class="fas fa-envelope"></i></span>
                        <input type="email" placeholder="Correo electrónico" class="form-control" v-model="user.email" required>
                    </div>
                    <div class="mb-3 input-group rounded-pill overflow-hidden">
                        <span class="input-group-text"><i class="fas fa-lock"></i></span>
                        <input :type="passwordFieldType" placeholder="Contraseña" class="form-control" v-model="user.password" required>
                        <button type="button" class="btn btn-outline-light btn-sm" @click="togglePasswordVisibility">
                            <i :class="passwordFieldIcon"></i>
                        </button>
                    </div>
                    <div class="mb-3 input-group rounded-pill overflow-hidden">
                        <span class="input-group-text"><i class="fas fa-check"></i></span>
                        <input :type="passwordFieldType" placeholder="Confirmar contraseña" class="form-control" v-model="user.confirmPassword" required>
                        <button type="button" class="btn btn-outline-light btn-sm" @click="togglePasswordVisibility">
                            <i :class="passwordFieldIcon"></i>
                        </button>
                    </div>
                    <div class="form-check mt-2">
                        <input type="checkbox" class="form-check-input" id="tyc" v-model="user.tyc" required>
                        <label class="form-check-label" for="tyc"><h6>Terminos y Condiciones</h6></label>
                    </div>
                </div>
            </div>

            <div class="d-flex flex-column flex-md-row justify-content-center align-items-center gap-2 mt-3" id="bot">
                <div class="w-100 w-md-auto" style="max-width: 150px;">
                    <button type="submit" class="btn btn-danger btn-sm w-100 rounded-pill p-2">Registrar</button>
                </div>
                <div class="w-100 w-md-auto" style="max-width: 150px;">
                    <button type="button" class="btn btn-light btn-sm w-100 rounded-pill p-2" @click="goToLogin" :disabled="loading">
                        <span v-if="!loading">Iniciar sesión</span>
                        <i v-if="loading" class="fas fa-spinner fa-spin"></i>
                    </button>
                </div>
            </div>
        </form>

        <div class="floating-message-container mt-3">
            <Transition name="fade">
                <div v-if="errorMessage" class="alert alert-danger text-center">
                    <span class="error-icon">❌</span>{{ errorMessage }}
                </div>
            </Transition>
            <Transition>
                <div v-if="successMessage" class="alert alert-success text-center">
                    {{ successMessage }}
                </div>
            </Transition> 
        </div>
    </div>
</template>


<script>
import { register } from '../api/AuthService';

export default {
    data() {
        return {
            user: {
                nombre: '',
                celular: '',
                email: '',
                password: '',
                confirmPassword: '',
                tyc: false
            },
            passwordFieldType: 'password',
            errorMessage: '',
            successMessage: '',
            loading:false //para animacion de carga
        };
    },
    computed: {
        passwordFieldIcon() {
            return this.passwordFieldType === 'password' ? 'fas fa-eye' : 'fas fa-eye-slash';
        }
    },
    methods: {
        async registro() {
            this.errorMessage = '';
            this.successMessage = '';

            // Validar celular
            if (!/^\d+$/.test(this.user.celular)) {
                this.errorMessage = 'El número de celular solo debe contener dígitos.';
                return;
            }
            if (this.user.celular.length !== 10) {
                this.errorMessage = this.user.celular.length < 10
                    ? 'El número de celular debe tener 10 dígitos.'
                    : 'El número de celular tiene más de 10 dígitos.';
                    setTimeout(() => {
                    this.errorMessage = '';
                }, 2000); // 2 segundos antes de borrar el mensaje
                return;
            }

            // En la validación de contraseñas dentro del método registro()
            if (this.user.password !== this.user.confirmPassword) {
                this.errorMessage = 'Las contraseñas no coinciden.';
                setTimeout(() => {
                    this.errorMessage = '';
                }, 2000); // 2 segundos antes de borrar el mensaje
                return;
            }
            

            try {
                // Enviar datos al backend
                const response = await register({
                    nombre: this.user.nombre,
                    celular: this.user.celular,
                    email: this.user.email, 
                    password: this.user.password,  
                    confirmPassword: this.user.confirmPassword  
});

            this.showSuccess(response.mensaje);
            } catch (error) {
                this.showError(error.response?.data?.error || "Error en el registro.");
            }
        },
        showError(message) {
            this.errorMessage = message;
            setTimeout(() => {
                this.errorMessage = '';
                this.resetForm();
            }, 2000); // Espera 5s antes de borrar mensaje y formulario
        },
        showSuccess(message) {
            this.successMessage = message;
            setTimeout(() => {
                this.successMessage = '';
                this.resetForm();
            }, 2000); // Espera 5s antes de borrar mensaje y formulario
        },
        resetForm() {
            this.user = {
                nombre: '',
                celular: '',
                email: '',
                password: '',
                confirmPassword: '',
                tyc: false
            };
        },
        togglePasswordVisibility() {
            this.passwordFieldType = this.passwordFieldType === 'password' ? 'text' : 'password';
        },
        goToLogin(){
            this.loading = true //aqui activa la animacion
            setTimeout(() =>{
                this.loading = false;
                this.$router.push('/login'); //redirige a la pagina 
            },1500)
        }
    }
};
</script>

<style scoped>
/* .btn-custom {
    background-color: #20b0b5;
    color: white;
} */



/* .btn-custom:hover {
    background-color: #ffc107;
    color: black;
} */

#tyc {
    border-color: #007bff !important;
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.7);
}

.message-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 10px;
}

.alert {
    padding: 2px;
    font-size: 10px;
    width: 30%;
    text-align: center;
    margin: 2px;
}

.floating-message-container {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 1050;
    width: 40%;
    max-width: 400px;
}

/* Estilos de alertas */
.alert {
    padding: 12px;
    font-size: 16px;
    width: 100%;
    text-align: center;
    font-weight: bold; /* Texto más grueso */
    position: relative;
    box-shadow: 0px 4px 8px rgba(255, 255, 255, 0.2);
}

/* Ícono de error "❌" */
.error-icon {
    font-size: 20px;
    margin-right: 8px;
    color: white;
}

/* Animación de temblor para los errores */
@keyframes shake {
    0%, 100% { transform: translateX(0); }
    20% { transform: translateX(-5px); }
    40% { transform: translateX(5px); }
    60% { transform: translateX(-5px); }
    80% { transform: translateX(5px); }
}

/* Aplicar la animación a los mensajes de error */
.alert-danger {
    background-color:#e87650; /* Rojo fuerte */
    color: rgb(0, 0, 0);
    border: 3px solid #b30000;
    box-shadow: 0 0 12px rgba(255, 0, 0, 0.7);
    animation: shake 0.4s ease-in-out;

}

/* Animación fade para entrada y salida */
.fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
    opacity: 0;
}
</style>