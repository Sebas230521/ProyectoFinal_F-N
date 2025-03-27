<template>
  <div class="app-container">
    <nav class="navbar">
      <div class="dropdown">
        <router-link to="/interes" class="btn btn-outline-secondary btn-sm">?</router-link>
      </div>

      <!-- Botón de usuario con menú desplegable -->
      <div class="dropdown">
        <button
          class="btn btn-outline-secondary rounded-circle user-initial"
          type="button"
          @click="toggleDropdown"
        >
          <span v-if="userInitial">{{ userInitial }}</span>
          <i v-else class="bi bi-person-circle"></i>
        </button>

        <!-- Menú desplegable -->
        <ul v-if="isDropdownOpen" class="dropdown-menu dropdown-menu-end show">
          <!--<li><button @click="toggleMode" class="dropdown-item">Tema</button></li>-->
          <li><button @click="logout" class="dropdown-item text-danger">Cerrar Sesión</button></li>
        </ul>
      </div>
    </nav>

    <main class="content">
      <div class="card-container">
        <div class="card shadow-sm text-center semi-transparent-card">
          <div class="mb-3">
            <img src="@/assets/logoMenuLBlanca.png" alt="Fish-Nexus Logo" class="img-fluid w-50" />
          </div>

          <div class="d-flex flex-column align-items-center gap-3 w-100">
            <div class="d-flex align-items-center gap-3 w-75">
              <i class="bi bi-capslock fs-5"></i>
              <button @click="goToNuevoEstanque" class="btn btn-outline-secondary w-100">Nuevo Estanque</button>
            </div>
            <div class="d-flex align-items-center gap-3 w-75">
              <i class="bi bi-calendar4 fs-5"></i>
              <button @click="goToProcedimientos" class="btn btn-outline-secondary w-100">Procedimientos</button>
            </div>
            <div class="d-flex align-items-center gap-3 w-75">
              <i class="bi bi-bar-chart fs-5"></i>
              <button class="btn btn-outline-secondary w-100">Información</button>
            </div>
          </div>
        </div>
      </div>
    </main>

    <footer class="container-fluid text-center py-2">
      <div class="row d-flex justify-content-center align-items-end">
        <div class="col-12 col-md-5 d-flex flex-column align-items-center">
          <h6 class="mb-2">Redes Sociales</h6>
          <div class="d-flex gap-2">
            <a href="https://www.instagram.com/escobar_sebas303?igsh=MWdpMHRlNjVsbTZrcQ==" class="btn btn-outline-dark btn-sm">
              <i class="bi bi-instagram"></i>
            </a>
            <a href="https://youtu.be/rscOXVuaCGw?si=3zk9Afp2va_KMetw" class="btn btn-outline-dark btn-sm">
              <i class="bi bi-youtube"></i>
            </a>
          </div>
          <div class="mt-1">
            <p class="mb-1">Ubicación</p>
            <a href="https://maps.app.goo.gl/yjLfgUtXxhNU2CcU9" class="btn btn-outline-dark btn-sm">
              <i class="bi bi-geo-alt"></i>
            </a>
          </div>
        </div>

        <div class="col-12 col-md-5 d-flex flex-column align-items-center">
          <h6 class="mb-2">Contactos</h6>
          <div class="d-flex gap-2">
            <a href="mailto:correo@gmail.com" class="btn btn-outline-dark btn-sm">
              <i class="bi bi-envelope"></i>
            </a>
            <a href="tel:+57001360000" class="btn btn-outline-dark btn-sm">
              <i class="bi bi-telephone"></i>
            </a>
          </div>
          <p class="mt-1 mb-0">Correo@gmail.com</p>
          <p class="mt-1">+57 3137581122</p>
        </div>
      </div>
      <p class="mt-2 text-center w-100">© 2024 copyright: FISH-NEXUS</p>
    </footer>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "MenuView",
  setup() {
    const router = useRouter();
    const isDarkMode = ref(false);
    const userInitial = ref(null);
    const isDropdownOpen = ref(false);

    onMounted(() => {
      const savedMode = localStorage.getItem("darkMode");
      if (savedMode !== null) {
        isDarkMode.value = JSON.parse(savedMode);
      }
      updateBodyClass();

      const userName = localStorage.getItem("userName") || "Usuario";
      if (userName) {
        userInitial.value = userName.charAt(0).toUpperCase();
      }
    });

    const toggleMode = () => {
      isDarkMode.value = !isDarkMode.value;
      localStorage.setItem("darkMode", JSON.stringify(isDarkMode.value));
      updateBodyClass();
    };

    const updateBodyClass = () => {
      if (isDarkMode.value) {
        document.body.classList.add("bg-dark", "text-white");
      } else {
        document.body.classList.remove("bg-dark", "text-white");
      }
    };

    const goToNuevoEstanque = () => {
      router.push('/nuevo-estanque');
    };

    const goToProcedimientos = () => {
      router.push('/register-procedures');
    };

    const toggleDropdown = () => {
      isDropdownOpen.value = !isDropdownOpen.value;
    };

    const logout = () => {
      localStorage.removeItem("userName");
      router.push("/login"); // Redirigir a la página de login
    };

    return {
      isDarkMode,
      toggleMode,
      goToNuevoEstanque,
      goToProcedimientos,
      userInitial,
      isDropdownOpen,
      toggleDropdown,
      logout
    };
  },
};
</script>


<style scoped>
html, body, #app {
  height: 100vh;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.user-initial {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 18px;
  background-color: #f0a500;
  color: white;
  border-radius: 50%;
  border: none;
}

.content {
  flex: 1; 
  display: flex;
  justify-content: center;
  align-items: center;
  background-image: url(../assets/lagoFondoMed.jpg);
  background-size: cover;
}

.footer {
  background-color: #121212; 
  color: white;
  padding: 10px;
  text-align: center;
  flex-shrink: 0;
}

.navbar {
  background: #121212;
  color: white;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-content {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}

.container-fluid {
  background: #121212;
  color: white;
}

.card-container {
  max-width: 600px;
  width: 90%;
}

.semi-transparent-card {
  background: #121212;
  backdrop-filter: blur(3px);
  border: 2px solid rgba(0, 0, 0, 0.6);
  border-radius: 15px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  width: 90%;
}

.btn {
  background-color: rgb(212, 101, 26);
  margin-bottom: 3px;
  color: black;
  border: 2px;
}

.bi {
  color: aliceblue;
}

.bg-dark {
  background-color: #121212;
}

.text-white {
  color: white;
}

.bg-light {
  background-color: white;
}

.dropdown-menu {
  position: absolute;
  top: 50px;
  right: 10px;
  background: white;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 5px 0;
}

.dropdown-item {
  padding: 8px 15px;
  cursor: pointer;
}

.dropdown-item:hover {
  background-color: #f8f9fa;
}

.text-danger {
  color: red;
}
</style>


<!-- <template>
  <div class="app-container">
    <nav class="navbar">
      <div class="dropdown">
        <router-link to="/interes" class="btn btn-outline-secondary btn-sm">?</router-link>
      </div>
      <button
        class="btn btn-outline-secondary rounded-circle"
        type="button"
        id="dropdownMenuButton"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        <i class="bi bi-person-circle"></i>
      </button>
      <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuButton">
        <li><button @click="toggleMode" class="dropdown-item">Tema</button></li>
        <li><a class="dropdown-item text-muted" href="#">Salir</a></li>
      </ul>
    </nav>

    <main class="content">
      <div class="card-container">
        <div class="card shadow-sm text-center semi-transparent-card">
          <div class="mb-3">
            <img src="@/assets/logoMenuLBlanca.png" alt="Fish-Nexus Logo" class="img-fluid w-50" />
          </div>

          <div class="d-flex flex-column align-items-center gap-3 w-100">
            <div class="d-flex align-items-center gap-3 w-75">
              <i class="bi bi-capslock fs-5"></i>
              <button @click="goToNuevoEstanque" class="btn btn-outline-secondary w-100">Nuevo Estanque</button>
            </div>
            <div class="d-flex align-items-center gap-3 w-75">
              <i class="bi bi-calendar4 fs-5"></i>
              <button @click="goToProcedimientos" class="btn btn-outline-secondary w-100">Procedimientos</button>
            </div>
            <div class="d-flex align-items-center gap-3 w-75">
              <i class="bi bi-bar-chart fs-5"></i>
              <button class="btn btn-outline-secondary w-100">Información</button>
            </div>
          </div>
        </div>
      </div>
    </main>

    <footer class="container-fluid text-center py-2">
      <div class="row d-flex justify-content-center align-items-end">
        <div class="col-12 col-md-5 d-flex flex-column align-items-center">
          <h6 class="mb-2">Redes Sociales</h6>
          <div class="d-flex gap-2">
            <a href="https://www.instagram.com/escobar_sebas303?igsh=MWdpMHRlNjVsbTZrcQ==" class="btn btn-outline-dark btn-sm">
              <i class="bi bi-instagram"></i>
            </a>
            <a href="https://youtu.be/rscOXVuaCGw?si=3zk9Afp2va_KMetw" class="btn btn-outline-dark btn-sm">
              <i class="bi bi-youtube"></i>
            </a>
          </div>
          <div class="mt-1">
            <p class="mb-1">Ubicación</p>
            <a href="https://maps.app.goo.gl/yjLfgUtXxhNU2CcU9" class="btn btn-outline-dark btn-sm">
              <i class="bi bi-geo-alt"></i>
            </a>
          </div>
        </div>

        <div class="col-12 col-md-5 d-flex flex-column align-items-center">
          <h6 class="mb-2">Contactos</h6>
          <div class="d-flex gap-2">
            <a href="mailto:correo@gmail.com" class="btn btn-outline-dark btn-sm">
              <i class="bi bi-envelope"></i>
            </a>
            <a href="tel:+57001360000" class="btn btn-outline-dark btn-sm">
              <i class="bi bi-telephone"></i>
            </a>
          </div>
          <p class="mt-1 mb-0">Correo@gmail.com</p>
          <p class="mt-1">+57 3137581122</p>
        </div>
      </div>
      <p class="mt-2 text-center w-100">© 2025 copyright: FISH-NEXUS</p>
    </footer>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "MenuView",
  setup() {
    const router = useRouter();
    const isDarkMode = ref(false);

    onMounted(() => {
      const savedMode = localStorage.getItem("darkMode");
      if (savedMode !== null) {
        isDarkMode.value = JSON.parse(savedMode);
      }
      updateBodyClass();
    });

    const toggleMode = () => {
      isDarkMode.value = !isDarkMode.value;
      localStorage.setItem("darkMode", JSON.stringify(isDarkMode.value));
      updateBodyClass();
    };

    const updateBodyClass = () => {
      if (isDarkMode.value) {
        document.body.classList.add("bg-dark", "text-white");
        document.body.classList.remove("bg-light");
      } else {
        document.body.classList.remove("bg-dark", "text-white");
        document.body.classList.add("bg-light");
      }
    };

    const goToNuevoEstanque = () => {
      router.push('/nuevo-estanque');
    };

    const goToProcedimientos = () => {
      router.push('/register-procedures');
    };

    return { isDarkMode, toggleMode, goToNuevoEstanque, goToProcedimientos };
  },
};
</script>

<style scoped>
html, body, #app {
  height: 100vh;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.content {
  flex: 1; 
  display: flex;
  justify-content: center;
  align-items: center;
  background-image: url(../assets/lagoFondoMed.jpg);
  background-size: cover;
}

.footer {
  background-color: #121212; 
  color: white;
  padding: 10px;
  text-align: center;
  flex-shrink: 0;
}

.navbar {
  background: #121212;
  color: white;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-content {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}

.container-fluid {
  background: #121212;
  color: white;
}

.card-container {
  max-width: 600px;
  width: 90%;
}

.semi-transparent-card {
  background: #121212;
  backdrop-filter: blur(3px);
  border: 2px solid rgba(0, 0, 0, 0.6);
  border-radius: 15px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  width: 90%;
}

.btn {
  background-color: rgb(212, 101, 26);
  margin-bottom: 3px;
  color: black;
  border: 2px;
}

.bi {
  color: aliceblue;
}

.bg-dark {
  background-color: #121212;
}

.text-white {
  color: white;
}

.bg-light {
  background-color: white;
}
</style>


 -->





















