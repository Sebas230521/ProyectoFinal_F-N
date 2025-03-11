import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',  // Ruta principal
    name: 'home',
    component: HomeView
  },
  {
    path: '/register', // Ruta alternativa para el registro
    name: 'register',
    component: HomeView
  },
  {
    path: '/login', //Ruta del login 
    name: 'login',
    component: () => import(/* webpackChunkName: "login" */ '../views/LogiView.vue') 
  },
  {
    path: '/reset-password',
    name: 'ResetPassword',
    component: () => import (/* webpackChunKName: "ResetPassword" */ '../components/ResetPassword.vue'),
  },
  {
    path: '/update-password',
    name: 'UpdatePassword',
    component: () => import (/* webpackChunKName: "UpdatePassword" */ '../components/UpdatePassword.vue'),
  },
  {
    path: '/register-procedures',   // La URL que mostrará el formulario
    name: 'RegistroProcedimiento',
    component: () => import (/* webpackChunKName: "UpdatePassword" */'../components/ProceduresForm.vue'),
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router;



// Para que los usuarios puedan acceder al formulario, asegúrate de tener un 
// enlace en la UI de tu aplicación que dirija a la nueva ruta que has creado

// <template>
//   <nav>
//     <router-link to="/registro-procedimiento">Registrar procedimiento</router-link>
//   </nav>
//   <router-view />
// </template>

// Esto creará un enlace en tu aplicación para que los usuarios puedan acceder 
// a la página de registro de procedimientos.