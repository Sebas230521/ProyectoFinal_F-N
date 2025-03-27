<template>
    <div class="container vh-100 d-flex justify-content-center align-items-center">
        <div class="row d-flex justify-content-center align-items-center w-100">
            <div class="card col-lg-6 col-md-8 col-sm-10 p-4 shadow">
                <form @submit.prevent="submitForm">
                    <h4 class="text-center mb-4">CAMBIO DE CONTRASEÑA</h4>
                    
                    <label for="newPassword" class="form-label">Nueva Contraseña</label>
                    <input 
                        type="password" 
                        id="newPassword" 
                        class="form-control" 
                        v-model="newPassword" 
                        required
                    />

                    <label for="repeatPassword" class="form-label mt-3">Verificar Contraseña</label>
                    <input 
                        type="password" 
                        id="repeatPassword" 
                        class="form-control" 
                        v-model="repeatPassword" 
                        :class="{ 'border border-danger': showPasswordError }" 
                        required
                    />

                    <div v-if="showPasswordError" class="alert alert-danger mt-3">
                        <strong>Error:</strong> Las contraseñas no coinciden.
                    </div>
                    <div v-if="serverMessage" :class="serverMessageClass" class="alert mt-3">
                        {{ serverMessage }}
                    </div>
        
                    <div class="mb-3 d-grid gap-2 d-md-flex justify-content-md-center mt-4">
                        <button type="button" class="btn btn-danger" @click="goBack">Cancelar</button>
                        <button type="submit" class="btn btn-success" :disabled="loading">
                            <span v-if="loading">Procesando...</span>
                            <span v-else>Actualizar Contraseña</span>
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { restablecerContraseña } from '../api/ApiUpdatePassword'; 
import { useRoute,  } from 'vue-router';

export default {
    data() {
        return {
            newPassword: '',
            repeatPassword: '',
            showPasswordError: false,
            serverMessage: '',
            serverMessageClass: 'alert-danger',
            loading: false,
            token: '' // Guardar el token
        };
    },
    created() {
        const route = useRoute();
        this.token = route.query.token || ''; // Obtener el token de la URL
    },
    methods: {
        async submitForm() {
            if (this.newPassword !== this.repeatPassword) {
                this.showPasswordError = true;
                return;
            }

            if (!this.token) {
                this.serverMessage = "El token no es válido o ha expirado.";
                this.serverMessageClass = 'alert-danger';
                return;
            }

            this.showPasswordError = false;
            this.loading = true;
            this.serverMessage = '';

            try {
                // Ahora enviamos el token también
                const response = await restablecerContraseña(this.newPassword, this.token);
                this.serverMessage = response.message;
                this.serverMessageClass = 'alert-success';

                setTimeout(() => {
                    this.$router.push('/login'); // Redirigir después de éxito
                }, 2000);
            } catch (error) {
                this.serverMessage = error.response?.data?.error || "Error al actualizar la contraseña.";
                this.serverMessageClass = 'alert-danger';
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

<style scoped>
.alert {
    text-align: center;
}
</style>
