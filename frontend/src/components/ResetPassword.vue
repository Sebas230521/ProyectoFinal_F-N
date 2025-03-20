<template>
    <div class="container vh-100 d-flex justify-content-center align-items-center">
        <div class="row d-flex justify-content-center align-items-center w-100">
            <div class="card col-lg-6 col-md-8 col-sm-10 p-4 shadow">
                <form @submit.prevent="submitForm">
                    <label for="email" class="mt-3 d-flex justify-content-center align-items-center form-label">Email</label>
                    <div class="d-flex justify-content-center align-items-center mb-3">
                        <input type="email" class="w-50 form-control" v-model="email" placeholder="Ingrese el correo electrónico"/>
                    </div>
                    <div v-if="showEmailError" class="justify-content-center align-items-center d-flex text-danger small">
                        Por favor, ingrese un correo válido.
                    </div>
                    <div class="mb-3 d-grid gap-2 d-md-flex justify-content-md-center mt-4">
                        <button type="button" @click="goBack" class="btn btn-danger">
                            <i class="bi bi-arrow-left-circle"></i> Atrás
                        </button>
                        <button type="submit" class="btn btn-success">Cambiar contraseña</button>
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
                email: '',
                showEmailError: false,
            };
        },
        methods: {
            validateEmail(email) {
                const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return emailPattern.test(email);
            },
            submitForm() {
                if (this.validateEmail(this.email)) {
                this.showEmailError = false;
                // Ocultar formulario o redirigir a una página de éxito
                this.$router.push(''); // Redirige a una vista de éxito (que se configurará en el router)
                } else {
                this.showEmailError = true;
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
