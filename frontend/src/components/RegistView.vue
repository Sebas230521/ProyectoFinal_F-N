<template>
    <div>
        <h2 class="text-center mb-4"><strong>Registro de Usuario</strong></h2>
        <form @submit.prevent="register">
            <div class="mb-3 input-group input-group-sm w-50 mx-auto">
                <span class="input-group-text"><i class="fas fa-user"></i></span>
                <input type="text" placeholder="Nombre usuario" class="form-control" v-model="user.nombre" required>
            </div>
            <div class="mb-3 input-group input-group-sm w-50 mx-auto">
                <span class="input-group-text"><i class="fas fa-phone"></i></span>
                <input type="tel" placeholder="Celular" class="form-control" v-model="user.celular" required>
            </div>
            <div class="mb-3 input-group input-group-sm w-50 mx-auto">
                <span class="input-group-text"><i class="fas fa-envelope"></i></span>
                <input type="email" placeholder="Correo electrónico" class="form-control" v-model="user.email" required>
            </div>
            <div class="mb-3 input-group input-group-sm w-50 mx-auto">
                <span class="input-group-text"><i class="fas fa-lock"></i></span>
                <input :type="passwordFieldType" placeholder="Contraseña" class="form-control" v-model="user.password" required>
                <button type="button" class="btn btn-outline-light btn-sm" @click="togglePasswordVisibility">
                    <i :class="passwordFieldIcon"></i>
                </button>
            </div>
            <div class="mb-3 input-group input-group-sm w-50 mx-auto">
                <span class="input-group-text"><i class="fas fa-check"></i></span>
                <input :type="passwordFieldType" placeholder="Confirmar contraseña" class="form-control" v-model="user.confirmPassword" required>
                <button type="button" class="btn btn-outline-light btn-sm" @click="togglePasswordVisibility">
                    <i :class="passwordFieldIcon"></i>
                </button>
            </div>
            <div class="form-check mt-2 w-50 mx-auto">
                <input type="checkbox" class="form-check-input" id="tyc" v-model="user.tyc" required>
                <label class="form-check-label" for="tyc">Aceptar TyC</label>
            </div>
            <div class="d-flex justify-content-center mt-3">
                <button type="submit" class="btn btn-custom btn-sm">Registrar</button>
            </div>
        </form>
        <div class="message-container"> 
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
        };
    },
    computed: {
        passwordFieldIcon() {
            return this.passwordFieldType === 'password' ? 'fas fa-eye' : 'fas fa-eye-slash';
        }
    },
    methods: {
        register() {
            this.errorMessage = '';
            this.successMessage = '';

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
            if (this.user.password !== this.user.confirmPassword) {
                this.errorMessage = 'Las contraseñas no coinciden.';
                return;
            }

            this.successMessage = '¡Registro exitoso!';
            setTimeout(() => {
                this.resetForm();
            }, 5000);
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