import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
// import router from './router' // Descomente se usar vue-router

// Importe CSS global ou Tailwind aqui (se não for feito no App.vue)
import './assets/main.css' // TODO: Crie este arquivo se necessário (ex: para Tailwind)

const app = createApp(App)

app.use(createPinia())
// app.use(router) // Descomente se usar vue-router

app.mount('#app') 