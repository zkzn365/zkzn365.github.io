<template>
  <div>
    <!-- Banner -->
    <section class="bg-gradient-to-r from-primary to-primary/90 py-20 text-white">
      <div class="container-x text-center">
        <h1 class="text-4xl md:text-5xl font-bold mb-4">
          专业定制AI智能体·小程序·跨境电商平台
        </h1>
        <p class="text-xl opacity-90 mb-8 max-w-2xl mx-auto">
          一站式企业数字化开发服务，根据需求定制专属智能系统
        </p>
        <NuxtLink to="/contact" class="btn-primary bg-white text-primary hover:bg-gray-100 inline-block">
          获取定制方案
        </NuxtLink>
      </div>
    </section>

    <!-- 服务板块 -->
    <section class="py-16 bg-gray-50">
      <div class="container-x">
        <h2 class="text-3xl font-bold text-center mb-12">我们的核心服务</h2>
        <div class="grid md:grid-cols-3 gap-8">
          <!-- AI智能体 -->
          <div class="p-6 bg-white rounded-xl shadow-sm hover:shadow-lg transition">
            <div class="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mb-4">
              <span class="text-2xl">🤖</span>
            </div>
            <h3 class="text-xl font-bold mb-2">AI智能体定制</h3>
            <p class="text-gray-600">
              企业专属AI助手、智能客服、自动化流程AI、大模型应用开发
            </p>
          </div>

          <!-- 小程序 -->
          <div class="p-6 bg-white rounded-xl shadow-sm hover:shadow-lg transition">
            <div class="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mb-4">
              <span class="text-2xl">📱</span>
            </div>
            <h3 class="text-xl font-bold mb-2">全平台小程序</h3>
            <p class="text-gray-600">
              微信/支付宝/抖音小程序开发，商城、预约、企业展示
            </p>
          </div>

          <!-- 跨境电商 -->
          <div class="p-6 bg-white rounded-xl shadow-sm hover:shadow-lg transition">
            <div class="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mb-4">
              <span class="text-2xl">🌍</span>
            </div>
            <h3 class="text-xl font-bold mb-2">跨境电商平台</h3>
            <p class="text-gray-600">
              独立站、多语言商城、支付集成、物流对接、海外分销系统
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 为什么选择我们 -->
    <section class="py-16">
      <div class="container-x">
        <h2 class="text-3xl font-bold text-center mb-12">为什么选择我们</h2>
        <div class="grid md:grid-cols-4 gap-8">
          <div class="text-center">
            <div class="text-4xl font-bold text-primary mb-2">10+</div>
            <div class="text-gray-600">年行业经验</div>
          </div>
          <div class="text-center">
            <div class="text-4xl font-bold text-primary mb-2">200+</div>
            <div class="text-gray-600">成功项目</div>
          </div>
          <div class="text-center">
            <div class="text-4xl font-bold text-primary mb-2">50+</div>
            <div class="text-gray-600">技术团队</div>
          </div>
          <div class="text-center">
            <div class="text-4xl font-bold text-primary mb-2">24/7</div>
            <div class="text-gray-600">售后服务</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 联系我们 -->
    <section class="py-16 bg-gray-50">
      <div class="container-x text-center">
        <h2 class="text-3xl font-bold mb-4">准备好开始您的项目了吗？</h2>
        <p class="text-gray-600 mb-8">立即联系我们，获取免费咨询和报价</p>
        <NuxtLink to="/contact" class="btn-primary">联系我们</NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: '智科智能 - AI智能体·小程序·跨境电商定制开发'
})
</script>