import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      // Keep API prefix for backend route
      '/api/generate-memes': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      },
      // Strip the prefix for static file passthroughs
      '/api/static': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
})
