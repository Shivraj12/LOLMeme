import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      // Keep API prefix for backend route
      '/api/generate-memes': {
        target: 'http://localhost:5000',
        changeOrigin: true,
      },
      // But strip the prefix for static file passthroughs
      '/api/static': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  }
})
