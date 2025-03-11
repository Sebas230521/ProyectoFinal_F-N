<template>
    <div class="container vh-100 d-flex justify-content-center align-items-center">
        <div class="row d-flex justify-content-center align-items-center w-100">
            <div class="card col-lg-6 col-md-8 col-sm-10 p-4 shadow">
                <form @submit.prevent="submitForm">
                    <h4 class="text-center mb-4">CAMBIO DE CONTRASEÑA</h4>
                    
                    <!-- Campo de nueva contraseña -->
                    <label for="newPassword" class="form-label">Contraseña</label>
                    <input type="password" class="form-control" v-model="newPassword" placeholder="******"/>
                    <!-- Campo de repetir contraseña -->
                    <label for="repeatPassword" class="form-label mt-3">Verificar contraseña</label>
                    <input type="password" class="form-control" v-model="repeatPassword" :class="{ 'border border-danger': showPasswordError }" placeholder="******"/>

                    <!-- Mensaje de error -->
                    <div v-if="showPasswordError" class="alert alert-danger mt-3 d-flex justify-content-between align-items-center">
                        <span><strong>Error:</strong> Contraseña no coinciden</span>
                        <button type="button" class="btn-close" aria-label="Close" @click="showPasswordError = false"></button>
                    </div>
        
                    <!-- Botones -->
                    <div class="mb-3 d-grid gap-2 d-md-flex justify-content-md-center mt-4">
                        <button type="button" class="btn btn-danger" @click="goBack">Cancelar</button>
                        <button type="submit" class="btn btn-success">Actualizar contraseña</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                newPassword: '',
                repeatPassword: '',
                showPasswordError: false,
            };
        },
        methods: {
            submitForm() {
                if (this.newPassword !== this.repeatPassword) {
                    this.showPasswordError = true;
                } else {
                    this.showPasswordError = false;
                    // Aquí puedes manejar el proceso de cambio de contraseña o redirigir a una vista de éxito
                    this.$router.push('');
                }
            },
            goBack() {
            this.$router.go(-1); // Volver a la página anterior
            },
        },
    };
</script>

<style scoped>

</style>
