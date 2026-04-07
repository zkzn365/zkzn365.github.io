<template>
  <div>
    <!-- Banner -->
    <section class="relative py-24 md:py-32 text-white overflow-hidden">
      <div class="absolute inset-0 bg-gradient-to-br from-slate-900 via-slate-800 to-primary/80"></div>
      <div class="absolute inset-0 opacity-20" style="background-image: url('/hero-bg.jpg'); background-size: cover; background-position: center;"></div>
      <div class="absolute inset-0 bg-gradient-to-t from-slate-900/90 via-slate-900/50 to-transparent"></div>
      <div class="relative container-x text-center">
        <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold mb-6 bg-gradient-to-r from-white via-blue-200 to-blue-300 bg-clip-text text-transparent">
          专业定制AI智能体·小程序·跨境电商平台
        </h1>
        <p class="text-xl md:text-2xl text-blue-200 mb-8 max-w-3xl mx-auto">
          一站式企业数字化开发服务，根据需求定制专属智能系统
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <NuxtLink to="/contact" class="btn-primary bg-white text-primary hover:bg-blue-50 px-8 py-4 text-lg">
            获取定制方案
          </NuxtLink>
          <NuxtLink to="/services" class="px-8 py-4 text-lg border border-white/30 text-white rounded-lg hover:bg-white/10 transition">
            查看服务
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- 服务板块 -->
    <section class="py-20 bg-slate-900">
      <div class="container-x">
        <h2 class="text-3xl md:text-4xl font-bold text-center mb-4 text-white">我们的核心服务</h2>
        <p class="text-center text-slate-400 mb-16 max-w-2xl mx-auto">专注于为企业提供数字化转型解决方案，助力业务快速增长</p>
        <div class="grid md:grid-cols-3 gap-8">
          <!-- AI智能体 -->
          <div class="group p-8 bg-slate-800/50 border border-slate-700 rounded-2xl hover:border-primary/50 hover:bg-slate-800 transition-all duration-300 hover:-translate-y-1">
            <div class="w-16 h-16 bg-gradient-to-br from-primary to-blue-600 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
              <span class="text-3xl">🤖</span>
            </div>
            <h3 class="text-xl font-bold mb-3 text-white">AI智能体定制</h3>
            <p class="text-slate-400">
              企业专属AI助手、智能客服、自动化流程AI、大模型应用开发
            </p>
          </div>

          <!-- 小程序 -->
          <div class="group p-8 bg-slate-800/50 border border-slate-700 rounded-2xl hover:border-primary/50 hover:bg-slate-800 transition-all duration-300 hover:-translate-y-1">
            <div class="w-16 h-16 bg-gradient-to-br from-primary to-blue-600 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
              <span class="text-3xl">📱</span>
            </div>
            <h3 class="text-xl font-bold mb-3 text-white">全平台小程序</h3>
            <p class="text-slate-400">
              微信/支付宝/抖音小程序开发，商城、预约、企业展示
            </p>
          </div>

          <!-- 跨境电商 -->
          <div class="group p-8 bg-slate-800/50 border border-slate-700 rounded-2xl hover:border-primary/50 hover:bg-slate-800 transition-all duration-300 hover:-translate-y-1">
            <div class="w-16 h-16 bg-gradient-to-br from-primary to-blue-600 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
              <span class="text-3xl">🌍</span>
            </div>
            <h3 class="text-xl font-bold mb-3 text-white">跨境电商平台</h3>
            <p class="text-slate-400">
              独立站、多语言商城、支付集成、物流对接、海外分销系统
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 为什么选择我们 -->
    <section class="py-20 bg-gradient-to-br from-slate-800 to-slate-900">
      <div class="container-x">
        <h2 class="text-3xl md:text-4xl font-bold text-center mb-16 text-white">为什么选择我们</h2>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
          <div class="text-center p-6">
            <div class="text-5xl font-bold bg-gradient-to-r from-primary to-blue-400 bg-clip-text text-transparent mb-2">10+</div>
            <div class="text-slate-400">年行业经验</div>
          </div>
          <div class="text-center p-6">
            <div class="text-5xl font-bold bg-gradient-to-r from-primary to-blue-400 bg-clip-text text-transparent mb-2">200+</div>
            <div class="text-slate-400">成功项目</div>
          </div>
          <div class="text-center p-6">
            <div class="text-5xl font-bold bg-gradient-to-r from-primary to-blue-400 bg-clip-text text-transparent mb-2">50+</div>
            <div class="text-slate-400">技术团队</div>
          </div>
          <div class="text-center p-6">
            <div class="text-5xl font-bold bg-gradient-to-r from-primary to-blue-400 bg-clip-text text-transparent mb-2">24/7</div>
            <div class="text-slate-400">售后服务</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 联系我们 -->
    <section class="py-20 bg-slate-900">
      <div class="container-x text-center">
        <h2 class="text-3xl md:text-4xl font-bold mb-4 text-white">准备好开始您的项目了吗？</h2>
        <p class="text-slate-400 mb-8">立即联系我们，获取免费咨询和报价</p>
        <NuxtLink to="/contact" class="btn-primary px-8 py-4 text-lg">联系我们</NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: '中科智农 - AI智能体·小程序·跨境电商定制开发'
})
</script>