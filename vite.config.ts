import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    proxy: {
      '/python-runner': {
        target: 'http://127.0.0.1:8765',
        rewrite: path => path.replace(/^\/python-runner/, ''),
      },
    },
  },
})
