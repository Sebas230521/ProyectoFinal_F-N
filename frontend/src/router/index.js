import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LogiView.vue'

const routes = [
  {
    path: '/',  // Redirige a login automáticamente
    redirect: '/login'
  },
  {
    path: '/login',  // Ruta principal ahora es el login
    name: 'login',
    component: LoginView
  },
  {
    path: '/registro',
    name: 'registro',
    component: () => import(/* webpackChunkName: "registro" */ '../views/HomeView.vue')
  },
  {
    path: '/reset-password',
    name: 'resetPassword',
    component: () => import(/* webpackChunkName: "resetPassword" */ '../components/ResetPassword.vue'),
  },
  {
    path: '/update-password',
    name: 'updatePassword',
    component: () => import(/* webpackChunkName: "updatePassword" */ '../components/UpdatePassword.vue'),
  },
  {
    path: '/register-procedures',
    name: 'registroProcedimiento',
    component: () => import(/* webpackChunkName: "proceduresForm" */ '../components/ProceduresForm.vue'),
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