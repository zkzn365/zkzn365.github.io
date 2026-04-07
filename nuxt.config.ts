// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  app: {
    baseURL: '/',
    head: {
      title: '中科智农（云南）科技有限责任公司 - AI智能体·小程序·跨境电商定制开发',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: '中科智农是一家专注于企业数字化定制开发的技术公司，提供AI智能体开发、小程序开发、跨境电商平台搭建等一站式解决方案' },
        { name: 'keywords', content: 'AI智能体开发,小程序开发,跨境电商,企业官网,系统定制开发,云南昆明' }
      ],
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap' }
      ]
    }
  },
  nitro: {
    prerender: {
      crawlLinks: true,
      routes: ['/', '/services', '/cases', '/about', '/contact']
    }
  }
})