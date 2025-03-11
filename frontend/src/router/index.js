import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',  // Ruta principal
    name: 'home',
    component: HomeView
  },
  {
    path: '/registro', // Ruta alternativa para el registro
    name: 'registro',
    component: HomeView
  },
  {
    path: '/login', //Ruta del login 
    name: 'login',
    component: () => import(/* webpackChunkName: "login" */ '../views/LogiView.vue') 
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

