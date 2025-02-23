<template>
    <div>
        <h2 class="text-center mb-4">Registro de Usuario</h2>
        <form @submit.prevent="register">
            <div class="mb-4">
                <input type="text" placeholder="Nombre usuario" class="form-control form-control-sm  w-50 mx-auto" v-model="user.nombre" required>
            </div>
            <div class="mb-4">
                <input type="tel" placeholder="Celular" class="form-control form-control-sm  w-50 mx-auto" v-model="user.celular" required>
            </div>
            <div class="mb-4">
                <input type="email" placeholder="Correo electrónico" class="form-control form-control-sm  w-50 mx-auto" v-model="user.email" required>
            </div>
            <div class="mb-4">
                <input type="password" placeholder="Contraseña" class="form-control form-control-sm  w-50 mx-auto" v-model="user.password" required>
            </div>
            <div class="mb-4">
                <input type="password" placeholder="Confirmar contraseña" class="form-control form-control-sm  w-50 mx-auto" v-model="user.confirmPassword" required>
            </div>
            <div class="form-check mt-3  w-50 mx-auto">
                <input type="checkbox" class="form-check-input" id="tyc" v-model="user.tyc" required>
                <label class="form-check-label" for="tyc">Aceptar TyC</label>
            </div>
            <div class="d-flex justify-content-center mt-4">
                <button type="submit" class="btn btn-custom btn-outline-warning">Registrar</button>
            </div>
        </form>
        <div class="modal fade" id="messageModal" tabindex="-1" aria-hidden="true"> <!--Mensaje-->
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Mensaje</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        {{ message }}
                    </div>
                </div>
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
        message: ''
    };
    },
    methods: {
    register() {
        if (this.user.password !== this.user.confirmPassword) {
        this.message = 'Las contraseñas no coinciden.';
        this.showModal();
        return;
        }

        setTimeout(() => {
        this.resetForm();
        }, 3000);
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
    }
    }
};
</script>

<style scoped>
h2 {
    text-align: center;
}

.btn-custom {
    background-color: #dfb3b3;
    color: white;
}

.btn-custom:hover {
    background-color: #ffc107;
    color: black;
}
</style>
