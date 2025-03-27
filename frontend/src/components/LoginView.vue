<template>
    <section class="contai">
        <div class="form-content">
            <div class="d-flex justify-content-center align-items-center mt-4">
                <img src="@/assets/Fond.png" alt="logo" class="rounded-circle logo">
            </div>
            <form class="text-center" @submit.prevent="login">
                <div class="input-group">
                    <div class="input-field">
                        <i class="fa-solid fa-envelope"></i>
                        <input type="email" class="form-control" v-model="email" placeholder="Correo" required>
                    </div>
                </div>
                <div class="input-group mb-3">
                    <div class="input-field">
                        <i class="fa-solid fa-lock"></i>
                        <input :type="showPassword ? 'text' : 'password'" class="form-control" v-model="password" placeholder="Contraseña" required>
                        <button type="button" id="togglePassword" @click="togglePassword">
                            <i :class="showPassword ? 'fa-solid fa-eye-slash' : 'fa-solid fa-eye'"></i>
                        </button>
                    </div>
                </div>

                <div class="row g-2">
                    <div class="col-12 col-md-6">
                        <button type="submit" class="btn btn-danger w-100 rounded-pill"  :disabled="loading">
                            <span v-if="!loading">Iniciar sesión</span>
                            <i v-if="loading" class="fas fa-spinner fa-spin"></i>
                        </button>
                    </div>
                    <div class="col-12 col-md-6">
                        <button type="button" class="btn btn-light w-100 rounded-pill" :disabled="loadingRegister" @click="goToRegister">
                            <span v-if="!loadingRegister">Registro</span>
                            <i v-if="loadingRegister" class="fas fa-spinner fa-spin"></i>
                        </button>
                    </div>
                </div>

                <div id="messageBox">
                    <p v-if="errorMessage" class="text-danger">{{ errorMessage }}</p>
                </div>
                <!--enviará el email como un parámetro en la URL-->
                <!--componente ResetPassword podrá capturarlo con this.$route.query.email.-->
                <p class="p-4">
                    <router-link :to="{ path: '/ResetPassword', query: { email: email } }">
                    ¿Has olvidado la contraseña?
                    </router-link>
                </p>
            </form>
        </div>
    </section>
</template>

<script>
import { loginUser } from '../api/ApiLogin'; // Importamos la función para iniciar sesión 

export default {
    name: 'LoginView',
    data() {
        return {
            email: '',
            password: '',
            showPassword: false,
            loading: false, 
            loadingRegister: false, // Estado para el botón de registro
            errorMessage: ''
        };
    },
    methods: {
        togglePassword() {
            this.showPassword = !this.showPassword;
        },
        async login() {
            this.loading = true;
            this.errorMessage = '';

            try {
                // Llamamos a la API de login
                const response = await loginUser(this.email, this.password);

                // Verificamos los tokens con los nombres correctos (access_token y refresh_token)
                if (response.access_token && response.refresh_token) {
                    console.log("Inicio de sesión exitoso. Redirigiendo...");
                    this.$router.push('/menu'); // Redirigir al menú
                } else {
                    this.errorMessage = "No se pudo iniciar sesión. Verifica tus credenciales.";
                }
            } catch (error) {
                this.errorMessage = error.response?.data?.error || "Error en el inicio de sesión.";
            } finally {
                this.loading = false;
            }
        },
        goToRegister() {
            this.loadingRegister = true; // Activa la animación del botón de registro
            setTimeout(() => {
                this.loadingRegister = false;
                this.$router.push('/home'); // Redirige después de la animación
            }, 1500);
        },
        goToLogin(){
            this.loading = true; // Activa la animación de inicio de sesión
            setTimeout(() =>{
                this.loading = false;
                this.$router.push('/Login'); 
            }, 1500);
        }
    }
};
</script>


<style scoped>
/* Estilos para el componente */
.form-content {
    width: 100%;
    max-width: 380px;
    background-color: rgba(247, 152, 0, 0.401);
    padding: 50px 60px 80px;
    border-radius: 20px;
}

.input-field {
    background-color: #ffffff;
    margin: 10px;
    border-radius: 20px;
    display: flex;
    align-items: center;
    padding: 8px;
}

.input-field i {
    margin: 5px;
    color: #eeb328;
}

#togglePassword {
    background: none;
    border: none;
    cursor: pointer;
}

#togglePassword:focus {
    outline: none;
}

form p {
    color: #ffffff;
    text-align: left;
    font-size: 13px;
    padding: 2px;
}

form p a {
    text-shadow: 0px 0px 5px rgb(12, 6, 6);
    font-weight: bolder;
    color: #ffffff;
    margin-left: 14px;
}

.logo {
    width: 200px;
    height: 150px;
    object-fit: cover;
}
</style>
