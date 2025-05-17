<template>
    <form @submit.prevent="onSubmit">
      <input v-model="username" placeholder="Username" />
      <input type="password" v-model="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useAuthStore } from '../stores/authStore'
  
  const username = ref('')
  const password = ref('')
  const authStore = useAuthStore()
  
  const onSubmit = () => {
    authStore.login(username.value, password.value)
  }
  </script>
  