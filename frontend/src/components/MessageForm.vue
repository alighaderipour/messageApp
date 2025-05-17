<template>
    <form @submit.prevent="send">
      <input v-model="receiverId" placeholder="Receiver ID" type="number" />
      <textarea v-model="content" placeholder="Message..."></textarea>
      <button type="submit">Send</button>
    </form>
  </template>
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  
  const receiverId = ref('')
  const content = ref('')
  
  const send = async () => {
    await axios.post('/api/messages', { receiver_id: receiverId.value, content: content.value })
    content.value = ''
  }
  </script>