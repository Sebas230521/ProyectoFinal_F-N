<template>
    <div class="container vh-100 d-flex justify-content-center align-items-center">
        <div class="row d-flex justify-content-center align-items-center w-100">
            <div class="card col-lg-6 col-md-8 col-sm-10 p-4 shadow">
                <form @submit.prevent="submitForm">
                    <label for="email" class="mt-3 d-flex justify-content-center align-items-center form-label">
                        Correo Electronico
                    </label>
                    <div class="d-flex justify-content-center align-items-center mb-3">
                        <input 
                            type="email" 
                            class="w-50 form-control" 
                            v-model="email" 
                            placeholder="Ingrese el correo electrónico"
                            required
                        />
                    </div>
                    
                    <!-- Mensaje de error si el email no es válido -->
                    <div v-if="showEmailError" class="justify-content-center align-items-center d-flex text-danger small">
                        Por favor, ingrese un correo válido.
                    </div>

                    <!-- Mensaje de respuesta del servidor -->
                    <div v-if="serverMessage" :class="serverMessageClass" class="text-center mt-2">
                        {{ serverMessage }}
                    </div>

                    <div class="mb-3 d-grid gap-2 d-md-flex justify-content-md-center mt-4">
                        <button type="button" @click="goBack" class="btn btn-danger">
                            <i class="bi bi-arrow-left-circle"></i> Atrás
                        </button>
                        <button type="submit" class="btn btn-success" :disabled="loading">
                            <span v-if="loading">Enviando...</span>
                            <span v-else>Recuperar contraseña</span>
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { recoveryrequest } from '../api/ApiPasswordReset.js'; 

export default {
    data() {
        return {
            email: this.$route.query.email || '', 
            showEmailError: false,
            loading: false, 
            serverMessage: '', 
            serverMessageClass: 'text-danger'
        };
    },
    watch: {
        '$route.query.email'(newEmail) {
            this.email = newEmail || '';
        }
    },
    methods: {
        validateEmail(email) {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailPattern.test(email);
        },
        async submitForm() {
            if (!this.validateEmail(this.email)) {
                this.showEmailError = true;
                return;
            }

            this.showEmailError = false;
            this.loading = true;
            this.serverMessage = '';

            try {
                const response = await recoveryrequest(this.email);
                this.serverMessage = response.message;
                this.serverMessageClass = 'text-success';
            } catch (error) {
                this.serverMessage = error.response?.data?.message || 'Error al procesar la solicitud.';
                this.serverMessageClass = 'text-danger';
            } finally {
                this.loading = false;
            }
        },
        goBack() {
            this.$router.go(-1);
        },
    },
};
</script>
