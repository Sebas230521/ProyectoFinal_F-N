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
    path: '/ResetPassword',
    name: 'ResetPassword',
    component: () => import(/* webpackChunkName: "ResetPassword" */ '../views/ResetPasswordView.vue'),
    props: route => ({ token: route.query.token }) // Captura el token desde la URL
},
{
    path: '/updatepassword/:token?', // Se permite recibir un token opcional en la URL
    name: 'updatePassword',
    component: () => import(/* webpackChunkName: "updatePassword" */ '../views/UpdatePasswordview.vue'),
    props: route => ({ token: route.params.token }) // Pasa el token como prop si está en la URL
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
