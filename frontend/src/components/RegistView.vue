<template>
    <div class="container">
        <h2 class="text-center mb-4"><strong>Registro de Usuario</strong></h2>
        <form @submit.prevent="registro">
            <div class="row justify-content-center">
                <div class="col-12 col-md-8 col-lg-6">
                    <div class="mb-3 input-group">
                        <span class="input-group-text"><i class="fas fa-user"></i></span>
                        <input type="text" placeholder="Nombre usuario" class="form-control" v-model="user.nombre" required>
                    </div>
                    <div class="mb-3 input-group">
                        <span class="input-group-text"><i class="fas fa-phone"></i></span>
                        <input type="tel" placeholder="Celular" class="form-control" v-model="user.celular" required>
                    </div>
                    <div class="mb-3 input-group">
                        <span class="input-group-text"><i class="fas fa-envelope"></i></span>
                        <input type="email" placeholder="Correo electrónico" class="form-control" v-model="user.email" required>
                    </div>
                    <div class="mb-3 input-group">
                        <span class="input-group-text"><i class="fas fa-lock"></i></span>
                        <input :type="passwordFieldType" placeholder="Contraseña" class="form-control" v-model="user.password" required>
                        <button type="button" class="btn btn-outline-light btn-sm" @click="togglePasswordVisibility">
                            <i :class="passwordFieldIcon"></i>
                        </button>
                    </div>
                    <div class="mb-3 input-group">
                        <span class="input-group-text"><i class="fas fa-check"></i></span>
                        <input :type="passwordFieldType" placeholder="Confirmar contraseña" class="form-control" v-model="user.confirmPassword" required>
                        <button type="button" class="btn btn-outline-light btn-sm" @click="togglePasswordVisibility">
                            <i :class="passwordFieldIcon"></i>
                        </button>
                    </div>
                    <div class="form-check mt-2">
                        <input type="checkbox" class="form-check-input" id="tyc" v-model="user.tyc" required>
                        <label class="form-check-label" for="tyc">Aceptar TyC</label>
                    </div>
                </div>
            </div>

            <div class="d-flex flex-column flex-md-row justify-content-center align-items-center gap-2 mt-2">
                <div class="w-100 w-md-auto" style="max-width: 150px;">
                    <button type="submit" class="btn btn-custom btn-sm w-100 rounded-pill">Registrar</button>
                </div>
                <div class="w-100 w-md-auto" style="max-width: 150px;">
                    <button type="button" class="btn btn-outline-primary btn-sm w-100 rounded-pill" @click="goToLogin" :disabled="loading">
                        <span v-if="!loading">Iniciar sesión</span>
                        <i v-if="loading" class="fas fa-spinner fa-spin"></i>
                    </button>
                </div>
            </div>
        </form>

        <div class="message-container mt-3"> 
            <div v-if="errorMessage" class="alert alert-danger text-center">
                {{ errorMessage }}
            </div>
            <div v-if="successMessage" class="alert alert-success text-center">
                {{ successMessage }}
            </div>
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
                return;
            }

            // Validar contraseñas
            if (this.user.password !== this.user.confirmPassword) {
                this.errorMessage = 'Las contraseñas no coinciden.';
                return;
            }

            try {
                // Enviar datos al backend
                const response = await register({
                    nombre: this.user.nombre,
                    celular: this.user.celular,
                    correo_electronico: this.user.email, 
                    password1: this.user.password, 
                    password2: this.user.confirmPassword
                });

                this.successMessage = response.mensaje;
                setTimeout(() => {
                    this.resetForm();
                }, 5000);
            } catch (error) {
                this.errorMessage = error.response?.data?.error || "Error en el registro.";
            }
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
                this.$router.push('/login'); //redirige a la pagina "Is"
            },1500)
        }
    }
};
</script>

<style scoped>
.btn-custom {
    background-color: #20b0b5;
    color: white;
}

.btn-custom:hover {
    background-color: #ffc107;
    color: black;
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
</style>



