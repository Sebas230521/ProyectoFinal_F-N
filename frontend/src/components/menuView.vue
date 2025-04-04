<template>
  <div class="app-container">

    <nav class="navbar">
      <!-- Logo -->
      <div class="logo">
        <img src="../assets/logoMenuLBlanca.png" alt="Logo">
      </div>
      <!-- Botón de usuario con menú desplegable -->
      <div class="dropdown">
        <button 
          class="btn btn-outline-secondary rounded-circle user-initial dropdown-toggle"
          type="button" 
          @click="toggleDropdown"
        >
          <span v-if="userInitial">{{ userInitial }}</span>
          <i v-else class="bi bi-person-circle"></i>
        </button>

        <!-- Menú desplegable -->
        <ul v-if="isDropdownOpen" class="dropdown-menu dropdown-menu show">
          <li><button @click="logout" class="dropdown-item text-danger">Cerrar sesión</button></li>
        </ul>
      </div>
    </nav>

    <main class="content">
      <div class="card-container">
        <div class="cards-wrapper">
          <div class="custom-card" @click="goToNuevoEstanque">
            <img src="../assets/nuevoEstanqueF.jpg" alt="Nuevo Estanque" class="card-img">
            <h3>Nuevo Estanque</h3>
            <p>Registra y administra tus estanques de manera eficiente.</p>
          </div>
          <div class="custom-card" @click="goToProcedimientos">
            <img src="../assets/imgProcedimientos.jpg" alt="Procedimientos" class="card-img">
            <h3>Procedimientos</h3>
            <p>Consulta y gestiona los procedimientos realizados.</p>
          </div>
          <div class="custom-card" @click="goToInformacion">
            <img src="../assets/imginforme.jpg" alt="Información" class="card-img">
            <h3>Información</h3>
            <p>Visualiza consumo y datos relevantes de los estanques.</p>
          </div>
        </div>
      </div>
    </main>

    <!-- Botón de ayuda flotante -->
    <button class="help-floating-btn" @click="showHelp">
      <i class="bi bi-question-circle"></i>
    </button>

    <footer class="footer">
      <p>© 2025 FISH-NEXUS - Todos los derechos reservados</p>
    </footer>

    <!-- MODAL DE AYUDA -->
    <div v-if="isHelpModalOpen" class="modal-overlay" @click.self="closeHelp">
      <div class="modal-content">
        <button class="close-button" @click="closeHelp">✖</button>
        <h2 class="modal-title">¿Qué hace este Menú?</h2>
        <ul class="modal-list">
          <li><strong>Nuevo Estanque:</strong> Crea y administra nuevos estanques.</li>
          <li><strong>Procedimientos:</strong> Consulta y organiza los procedimientos.</li>
          <li><strong>Información:</strong> Revisa estadísticas y datos de tu actividad.</li>
          <li><strong>Icono de perfil:</strong> Cierra sesión desde aquí.</li>
        </ul>
        <div class="modal-footer">Puedes cerrar esta ventana cuando lo necesites.</div>
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
</script>

<style scoped>
/* General */
.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-color: #3f4142; /* Fondo gris claro */
}

.navbar {
  display: flex;
  justify-content: space-between; /* Distribuye elementos a los extremos */
  align-items: center;
  padding: 10px 20px;
  background-color: #3a3a3a; /* Color del navbar */
}

.logo {
  width: 70px;
  height: 80px;
  display: flex;
  justify-content: center;
}

/* Usuario */
.user-initial {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 18px;
  background-color: #ff5733;
  color: white;
  border-radius: 50%;
  border: none;
}

/* Contenido Principal */
.content {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Tarjetas personalizadas */
.cards-wrapper {
  display: flex;
  gap: 100px;
  flex-wrap: wrap;
  justify-content: center;
  max-width: 1000px;
}

.custom-card {
  background: rgba(255, 255, 255, 0.979);
  border-radius: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  border: 2px solid transparent; 
  box-shadow: 0px 0px 15px 3px rgba(223, 93, 7, 0.808);
  text-align: center;
  padding: 12px;
  cursor: pointer;
  transition: transform 0.2s;
  width: 250px; 
}


.custom-card:hover {
  transform: scale(1.05);
}

.card-img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 8px;
}

.custom-card h3 {
  color: #3a3a3a;
  margin-top: 10px;
}

.custom-card p {
  font-size: 14px;
  color: #020202;
}

/* Botón de Ayuda Flotante */
.help-floating-btn {
  position: fixed;
  bottom: 60px;
  right: 20px;
  background: #ff5733;
  color: white;
  border: none;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 24px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: background 0.3s;
}

.help-floating-btn:hover {
  background: #ff5733;
}

/* Footer */
.footer {
  background: #3a3a3a;
  color: white;
  text-align: center;
  padding: 10px;
  font-size: 14px;
}

/* Modal */
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

.modal-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
}

.modal-list {
  padding-left: 20px;
}

.modal-list li {
  margin-bottom: 8px;
  font-size: 16px;
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
