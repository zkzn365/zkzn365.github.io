<template>
  <div class="py-16">
    <div class="container-x">
      <h1 class="text-3xl font-bold mb-8 text-center">联系我们</h1>
      <div class="max-w-xl mx-auto bg-white shadow-sm p-8 rounded-xl">
        <div class="mb-6 p-4 bg-gray-50 rounded-lg">
          <p class="text-gray-700"><strong>电话：</strong>0086-13997366845</p>
          <p class="text-gray-700"><strong>邮箱：</strong>wangleihd@gmail.com</p>
          <p class="text-gray-700"><strong>地址：</strong>中国(云南)自由贸易试验区昆明片区经开区顺通大道31号国际珠宝城6栋4层F407-22</p>
        </div>
        <form class="space-y-4" @submit.prevent="handleSubmit">
          <div>
            <label class="block mb-2 font-medium">公司/姓名</label>
            <input v-model="form.name" type="text" class="w-full border border-gray-300 p-3 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none" placeholder="请输入您的姓名或公司名称" required />
          </div>
          <div>
            <label class="block mb-2 font-medium">联系电话</label>
            <input v-model="form.phone" type="tel" class="w-full border border-gray-300 p-3 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none" placeholder="请输入您的联系电话" required />
          </div>
          <div>
            <label class="block mb-2 font-medium">电子邮箱</label>
            <input v-model="form.email" type="email" class="w-full border border-gray-300 p-3 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none" placeholder="请输入您的电子邮箱" />
          </div>
          <div>
            <label class="block mb-2 font-medium">需求描述</label>
            <textarea v-model="form.message" rows="4" class="w-full border border-gray-300 p-3 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none" placeholder="请描述您的需求：AI智能体/小程序/跨境电商/其他开发"></textarea>
          </div>
          <button type="submit" class="btn-primary w-full">提交需求</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const form = ref({
  name: '',
  phone: '',
  email: '',
  message: ''
})

const handleSubmit = () => {
  alert('感谢您的提交！我们将尽快与您联系。')
  form.value = { name: '', phone: '', email: '', message: '' }
}

useHead({
  title: '联系我们 - 中科智农'
})
</script>