// @ts-check
import { defineConfig } from 'astro/config';
import path from 'path';
import { fileURLToPath } from 'url';

import tailwindcss from '@tailwindcss/vite';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// https://astro.build/config
export default defineConfig({
  site: 'https://zkzn365.com',
  base: '/',
  vite: {
    plugins: [tailwindcss()],
    resolve: {
      alias: {
        '@': path.resolve(__dirname, './src')
      }
    }
  }
});