import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'bootstrap'
import '@/assets/css/bootstrap.min.css'
import '@/assets/js/bootstrap.bundle.min.js'

import '@fortawesome/fontawesome-free/css/all.css';

createApp(App).use(router).mount('#app')