<template>
  <div class="min-h-screen flex flex-col">
    <!-- 导航栏 -->
    <header class="sticky top-0 bg-white shadow-sm z-50">
      <div class="container-x py-4 flex justify-between items-center">
        <NuxtLink to="/" class="text-xl font-bold text-primary">智科智能</NuxtLink>
        <nav class="hidden md:flex gap-6">
          <NuxtLink to="/" class="hover:text-primary transition">首页</NuxtLink>
          <NuxtLink to="/services" class="hover:text-primary transition">服务项目</NuxtLink>
          <NuxtLink to="/cases" class="hover:text-primary transition">成功案例</NuxtLink>
          <NuxtLink to="/about" class="hover:text-primary transition">关于我们</NuxtLink>
          <NuxtLink to="/contact" class="hover:text-primary transition">联系我们</NuxtLink>
        </nav>
        <NuxtLink to="/contact" class="btn-primary hidden md:block">立即咨询</NuxtLink>
      </div>
    </header>

    <!-- 页面内容 -->
    <main class="flex-1">
      <slot />
    </main>

    <!-- 页脚 -->
    <footer class="bg-dark text-white py-10">
      <div class="container-x">
        <div class="grid md:grid-cols-4 gap-8">
          <div>
            <h3 class="text-lg font-bold mb-4">智科智能</h3>
            <p class="text-gray-300">专注企业数字化定制开发</p>
          </div>
          <div>
            <h4 class="font-semibold mb-3">服务项目</h4>
            <ul class="space-y-2 text-gray-300">
              <li>AI智能体开发</li>
              <li>小程序开发</li>
              <li>跨境电商平台</li>
            </ul>
          </div>
          <div>
            <h4 class="font-semibold mb-3">联系我们</h4>
            <p class="text-gray-300">电话：138xxxx8888</p>
            <p class="text-gray-300">邮箱：contact@zkzn365.com</p>
          </div>
        </div>
        <div class="mt-8 pt-4 border-t border-gray-700 text-center text-gray-400">
          © 2026 智科智能 版权所有
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
</script>