<template>
    <section class="contai">
      <div class="form-content">
        <div class="d-flex justify-content-center align-items-center mt-4">
          <img src="@/assets/Fond.png" alt="logo" class="logo">
        </div>
        <form class="text-center" @submit.prevent="login">
          <div class="input-group">
            <div class="input-field">
              <i class="fas fa-envelope"></i>
              <input type="email" class="form-control" v-model="email" placeholder="Correo" required>
            </div>
          </div>
          <div class="input-group mb-3">
            <div class="input-field">
              <i class="fa-solid fa-lock"></i>
              <input :type="showPassword ? 'text' : 'password'" class="form-control" v-model="contraseña" placeholder="Contraseña" required>
              <button type="button" id="togglePassword" @click="togglePassword">
                <i :class="showPassword ? 'fa-solid fa-eye-slash' : 'fa-solid fa-eye'"></i>
              </button>
            </div>
          </div>
          <div class="row g-2">
            <div class="col-12 col-md-6">
              <button type="submit" class="btn btn-danger w-100 rounded-pill" :disabled="loading">
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
          <p class="p-4">
            <router-link :to="{ path: '/ResetPassword', query: { email: email } }">¿Has olvidado la contraseña?</router-link>
          </p>
        </form>
      </div>
    </section>
  </template>
  
  <script>
  import { loginUser } from '../api/ApiLogin'; // Importa la función para iniciar sesión
  
  export default {
    name: 'LoginView',
    data() {
      return {
        email: '',
        contraseña: '',
        showPassword: false,
        loading: false,
        loadingRegister: false,
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
          // Llamamos a la API de inicio de sesión
          const response = await loginUser(this.email, this.contraseña);
          
          // Verificamos que se hayan recibido los tokens
          if (response.access_token && response.refresh_token) {
            // Almacenamos el nombre del usuario para usarlo en el menú
            localStorage.setItem('userName', response.nombre);
            
            console.log("Inicio de sesión exitoso. Redirigiendo...");
            this.$router.push('/menu');
          } else {
            this.showError("No se pudo iniciar sesión. Verifica tus credenciales.");
          }
        } catch (error) {
          this.showError(error.response?.data?.error || "Error en el inicio de sesión.");
        } finally {
          this.loading = false;
        }
      },
      goToRegister() {
        this.loadingRegister = true;
        setTimeout(() => {
          this.loadingRegister = false;
          this.$router.push('/home');
        }, 1500);
      },
      showError(message) {
        this.errorMessage = message;
        setTimeout(() => {
          this.errorMessage = '';
        }, 2000);
      }
    }
  };
  </script>
  
  <style scoped>
  .form-content {
    width: 100%;
    max-width: 380px;
    padding: 50px 60px 80px;
    border-radius: 20px;
    background-color: rgba(255, 255, 255, 0.575);
    box-shadow: 0px 4px 10px rgba(253, 156, 0, 0.962);
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
    color: #000000;
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
    text-shadow: 0px 0px 5px rgb(255, 255, 255);
    font-weight: bolder;
    color: #0a0a0a;
    margin-left: 10px;
    font-size: 14px;
    font-family: Arial, Helvetica, sans-serif;
  }
  
  .logo {
    width: 200px;
    height: 150px;
    object-fit: cover;
  }
  
  /* Estilos para mensajes y animaciones */
  .floating-message-container {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 1050;
    width: 40%;
    max-width: 400px;
  }
  
  .alert {
    padding: 12px;
    font-size: 16px;
    width: 100%;
    text-align: center;
    font-weight: bold;
    position: relative;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
  }
  
  .error-icon {
    font-size: 20px;
    margin-right: 8px;
    color: rgb(11, 11, 11);
  }
  
  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    20% { transform: translateX(-5px); }
    40% { transform: translateX(5px); }
    60% { transform: translateX(-5px); }
    80% { transform: translateX(5px); }
  }
  
  .alert-danger {
    background-color: #e87650;
    color: rgb(0, 0, 0);
    border: 3px solid #b30000;
    box-shadow: 0 0 12px rgba(255, 0, 0, 0.7);
    animation: shake 0.4s ease-in-out;
  }
  
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
  </style>
  