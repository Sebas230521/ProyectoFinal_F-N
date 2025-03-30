<template>
  <div class="app-container">

    <nav class="navbar">
      <div class="dropdown">
        <button class="btn-help btn btn-Secondary" @click="showHelp">
          <i class="bi bi-question-circle"></i> Ayuda
        </button>
      </div>

<!-- Botón de usuario con menú desplegable -->
<div class="dropdown"> <!--desde aqui iba para la inicial del usuario-->
        <button 
              class="btn btn-outline-secondary rounded-circle user-initial dropdown-toggle"
              type="button" 
              @click="toggleDropdown"
            >
              <span v-if="userInitial">{{ userInitial }}</span>
              <i v-else class="bi bi-person-circle"></i>
            </button>

        <!-- Menú desplegable -->
        <ul v-if="isDropdownOpen" class="dropdown-menu dropdown-menu-end show">
          <!--<li><button @click="toggleMode" class="dropdown-item">Tema</button></li>-->
          <li><button @click="logout" class="dropdown-item text-danger">Salir</button></li>
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
              <button @click="goToInformacion" class="btn btn-outline-secondary w-100">Información</button>
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
    <!-- MODAL DE AYUDA -->
      <div v-if="isHelpModalOpen" class="modal-overlay" @click.self="closeHelp">
        <div class="modal-content">
          <!-- Botón de cierre "X" -->
          <button class="close-button" @click="closeHelp">✖</button>

          <!-- Encabezado -->
          <h2 class="modal-title">¿Qué hace este Menú?</h2>
          <p>Aquí encontrarás información para navegar en la web que hemos diseñado para tu gestion en los lagos.</p>
          <p>Tenemos 3 opciones:</p>

          <!-- Contenido en lista -->
          <ul class="modal-list">
            <li><strong>Opción 1: Nuevo Estanque</strong> <br> Permite crear un nuevo estanque y administrarlo fácilmente.</li>
            <li><strong>Opción 2: Procedimientos</strong> <br> Consulta y administra los procedimientos de tus estanques.</li>
            <li><strong>Opción 3: Información</strong> <br> Visualiza estadísticas y datos sobre tu actividad.</li>
            <li><strong>Icono de perfil</strong> <br> Al hacer click en el icono puedes cerrar sesion en nuestra web que te redigirá al login.</li>
          </ul>

          <!-- Mensaje final -->
          <div class="modal-footer">
            Una vez revisadas las opciones, puedes cerrar esta ventana.
          </div>
        </div>
      </div>


  </div>
</template>

<script>
import { ref, onMounted } from "vue";
  import { useRouter } from "vue-router";
  
  export default {
    name: "MenuView",
    setup() {
      const router = useRouter();
      const userInitial = ref(null);
      const isDropdownOpen = ref(false);
      const isHelpModalOpen = ref(false); // Estado del modal de ayuda
  
      onMounted(() => {
        const userName = localStorage.getItem("userName") || "Usuario";
        userInitial.value = userName.charAt(0).toUpperCase();
      });
      
      const goToNuevoEstanque = () => {
      router.push('/nuevo-estanque');
      };

      const goToProcedimientos = () => {
      router.push('/register-procedures');
      };

      const goToInformacion = () => {
      router.push('/informacion');
    };


      const toggleDropdown = () => {
        isDropdownOpen.value = !isDropdownOpen.value;
      };
  
      const logout = () => {
        localStorage.removeItem("userName");
        router.push("/login");
      };
  
      const showHelp = () => {
        isHelpModalOpen.value = true;
      };
  
      const closeHelp = () => {
        isHelpModalOpen.value = false;
      };
  
      return {
        userInitial,
        isDropdownOpen,
        toggleDropdown,
        goToNuevoEstanque,
        goToProcedimientos,
        goToInformacion,
        logout,
        isHelpModalOpen,
        showHelp,
        closeHelp,
      };
    },
  };

// import { ref, onMounted } from "vue";
// import { useRouter } from "vue-router";

// export default {
//   name: "MenuView",
//   setup() {
//     const router = useRouter();
//     const isDarkMode = ref(false);
//     const userInitial = ref(null);
//     const isDropdownOpen = ref(false);

//     onMounted(() => {
//       const savedMode = localStorage.getItem("darkMode");
//       if (savedMode !== null) {
//         isDarkMode.value = JSON.parse(savedMode);
//       }
//       updateBodyClass();

//       const userName = localStorage.getItem("userName") || "Usuario";
//       if (userName) {
//         userInitial.value = userName.charAt(0).toUpperCase();
//       }
//     });

//     const toggleMode = () => {
//       isDarkMode.value = !isDarkMode.value;
//       localStorage.setItem("darkMode", JSON.stringify(isDarkMode.value));
//       updateBodyClass();
//     };

//     const updateBodyClass = () => {
//       if (isDarkMode.value) {
//         document.body.classList.add("bg-dark", "text-white");
//       } else {
//         document.body.classList.remove("bg-dark", "text-white");
//       }
//     };

//     const goToNuevoEstanque = () => {
//       router.push('/nuevo-estanque');
//     };

//     const goToProcedimientos = () => {
//       router.push('/register-procedures');
//     };

//     const toggleDropdown = () => {
//       isDropdownOpen.value = !isDropdownOpen.value;
//     };

//     const logout = () => {
//       localStorage.removeItem("userName");
//       router.push("/login"); // Redirigir a la página de login
//     };

//     return {
//       isDarkMode,
//       toggleMode,
//       goToNuevoEstanque,
//       goToProcedimientos,
//       userInitial,
//       isDropdownOpen,
//       toggleDropdown,
//       logout
//     };
//   },
// };
</script>


<style scoped>
/* html, body, #app {
  height: 100vh;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  overflow: hidden;
} */
 
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
  background: #201e1e;
  color: rgb(255, 253, 253);
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
  color: rgb(241, 241, 241);
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
  color: rgb(255, 247, 247);
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

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  width: 90%;
  max-width: 500px;
  text-align: left;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  position: relative;
}

.modal-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
  border-bottom: 2px solid #e0e0e0;
  padding-bottom: 5px;
}

.modal-list {
  padding-left: 20px;
}

.modal-list li {
  margin-bottom: 8px;
  font-size: 16px;
  line-height: 1.4;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 15px;
  background: none;
  border: none;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
  color: #333;
}

.close-button:hover {
  color: #ff5733;
}

.modal-footer {
  background: #ff5733;
  color: white;
  padding: 10px;
  border-radius: 5px;
  text-align: center;
  font-weight: bold;
  margin-top: 15px;
}
</style>

<!-- 
<template>
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