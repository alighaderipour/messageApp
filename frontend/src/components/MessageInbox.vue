<template>
    <div v-for="msg in messages" :key="msg.id">{{ msg.content }}</div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  const messages = ref([])
  
  onMounted(async () => {
    const res = await axios.get('/api/messages')
    messages.value = res.data
  })
  </script>
  