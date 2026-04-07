<template>
  <div class="min-h-screen flex flex-col bg-slate-900">
    <!-- 导航栏 -->
    <header class="sticky top-0 bg-slate-900/80 backdrop-blur-md border-b border-slate-700/50 z-50">
      <div class="container-x py-4 flex justify-between items-center">
        <NuxtLink to="/" class="text-xl font-bold bg-gradient-to-r from-primary to-blue-400 bg-clip-text text-transparent">中科智农</NuxtLink>
        <nav class="hidden md:flex gap-8">
          <NuxtLink to="/" class="text-slate-300 hover:text-primary transition">首页</NuxtLink>
          <NuxtLink to="/services" class="text-slate-300 hover:text-primary transition">服务项目</NuxtLink>
          <NuxtLink to="/cases" class="text-slate-300 hover:text-primary transition">成功案例</NuxtLink>
          <NuxtLink to="/about" class="text-slate-300 hover:text-primary transition">关于我们</NuxtLink>
          <NuxtLink to="/contact" class="text-slate-300 hover:text-primary transition">联系我们</NuxtLink>
        </nav>
        <NuxtLink to="/contact" class="btn-primary hidden md:block">立即咨询</NuxtLink>
      </div>
    </header>

    <!-- 页面内容 -->
    <main class="flex-1">
      <slot />
    </main>

    <!--页脚 -->
    <footer class="bg-slate-950 text-white py-12">
      <div class="container-x">
        <div class="grid md:grid-cols-4 gap-8">
          <div>
            <h3 class="text-lg font-bold mb-4 bg-gradient-to-r from-primary to-blue-400 bg-clip-text text-transparent">中科智农（云南）科技有限责任公司</h3>
            <p class="text-slate-400">专注企业数字化定制开发</p>
          </div>
          <div>
            <h4 class="font-semibold mb-3 text-white">服务项目</h4>
            <ul class="space-y-2 text-slate-400">
              <li>AI智能体开发</li>
              <li>小程序开发</li>
              <li>跨境电商平台</li>
            </ul>
          </div>
          <div>
            <h4 class="font-semibold mb-3 text-white">联系我们</h4>
            <p class="text-slate-400">电话：0086-13997366845</p>
            <p class="text-slate-400">邮箱：wangleihd@gmail.com</p>
          </div>
        </div>
        <div class="mt-8 pt-4 border-t border-slate-800 text-center text-slate-500">
          © 2026 中科智农（云南）科技有限责任公司 版权所有
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
</script>