<template>
        <section class="contai">
        <div class="form-content">
            <div class="d-flex justify-content-center align-items-center mt-4">
            <img src="@/assets/Logo_Fish-Nexus.png" alt="logo" class="rounded-circle logo">
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
            <div>
                <button type="submit" class="btn btn-outline-danger text-light" style="width: 55%;">Iniciar sesión</button>
                <div id="messageBox"></div>
            </div>
            <p class="m-2">Olvidaste tu contraseña <a href="#">click aquí</a></p>
            </form>
        </div>
        </section>
</template>

<script>
    export default {
        nombre:'LoginView',
        data() {
        return {
            email: '',
            password: '',
            showPassword: false,
        };
        },
        methods: {
        togglePassword() {
            this.showPassword = !this.showPassword;
        },
        login() {
            console.log('Intentando iniciar sesión con:', this.email, this.password);
        }
        }
    };
</script>
    
<style scoped>
    
    
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
        color: #ffff;
        text-align: left;
        font-size: 13px;
        padding: 2px;
    }
    
    form p a {
        text-shadow: 0px 0px 5px rgb(255, 255, 255);
        font-weight: bolder;
        color: #080808;
        margin-left: 14px;
    }
    
    .logo {
        width: 200px;
        height: 150px;
        object-fit: cover;
    }
</style>
