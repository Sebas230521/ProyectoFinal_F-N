import { createRouter, createWebHistory } from 'vue-router';

// Importación de vistas
import LogiView from '@/views/LogiView.vue'; // Corregido el nombre del archivo
import HomeView from '@/views/HomeView.vue';

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'login',
    component: LogiView
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/reset-password',
    name: 'resetPassword',
    component: () => import(/* webpackChunkName: "resetPassword" */ '../views/ResetPasswordView.vue')
  },
  {
    path: '/update-password',
    name: 'updatePassword',
    component: () => import(/* webpackChunkName: "updatePassword" */ '../views/UpdatePasswordview.vue')
  },
  {
    path: '/menu',
    name: 'menu',
    component: () => import(/* webpackChunkName: "menu" */ '../views/menuView.vue')
  },
  {
    path: '/nuevo-estanque',
    name: 'NuevoEstanque',
    component: () => import(/* webpackChunkName: "NuevoEstanque" */ '../views/PondView.vue')
  },
  {
    path: '/register-procedures',
    name: 'registroProcedimiento',
    component: () => import(/* webpackChunkName: "registroProcedimiento" */ '../views/RegisterProceduresView.vue')
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
