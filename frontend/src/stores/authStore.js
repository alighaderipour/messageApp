import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore("auth", {
  state: () => ({ token: null }),
  actions: {
    async login(username, password) {
      const res = await axios.post("/api/login", { username, password });
      this.token = res.data.access_token;
      axios.defaults.headers.common["Authorization"] = `Bearer ${this.token}`;
    },
  },
});
