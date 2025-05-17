<template>
    <div>
      <h2>Admin Dashboard</h2>
      <table>
        <tr><th>ID</th><th>Username</th><th>Email</th><th>Role</th><th>Actions</th></tr>
        <tr v-for="u in users" :key="u.id">
          <td>{{ u.id }}</td><td>{{ u.username }}</td><td>{{ u.email }}</td><td>{{ u.role }}</td>
          <td><button @click="remove(u.id)">Delete</button></td>
        </tr>
      </table>
    </div>
  </template>
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  const users = ref([])
  
  const loadUsers = async () => {
    const res = await axios.get('/admin/users')
    users.value = res.data
  }
  
  const remove = async (id) => {
    await axios.delete(`/admin/users/${id}`)
    await loadUsers()
  }
  
  onMounted(loadUsers)
  </script>
  