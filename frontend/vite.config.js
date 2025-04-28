import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    port: 3000, // Garante que rode na porta 3000 conforme docker-compose
    host: true, // Necessário para expor dentro do Docker
    // Proxy para a API Django (opcional, útil se não configurar CORS no backend)
    // proxy: {
    //   '/api': {
    //     target: 'http://api:8000', // 'api' é o nome do serviço no docker-compose
    //     changeOrigin: true,
    //     // rewrite: (path) => path.replace(/^\/api/, ''), // Remove /api se não estiver no backend
    //   }
    // }
  },
  test: {
    // Configuração básica do Vitest (se estiver usando)
    globals: true,
    environment: 'jsdom',
  },
}) 