<script setup>
import { RouterLink, useRoute } from 'vue-router'

const route = useRoute()
</script>

<template>
  <header class="header">
    <div class="wrap">
      <div class="brand">
        <RouterLink to="/">Task Manager</RouterLink>
      </div>
      <nav class="nav">
        <RouterLink :class="{ active: route.path === '/' }" to="/">Главная</RouterLink>
        <RouterLink :class="{ active: route.path.startsWith('/tasks') }" to="/tasks">Задачи</RouterLink>
      </nav>
    </div>
  </header>
</template>

<style scoped>
.header {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
}

.wrap {
  max-width: 980px;
  margin: 0 auto;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.brand a {
  text-decoration: none;
  font-weight: 700;
}

.nav {
  display: flex;
  gap: 12px;
}

.nav a {
  text-decoration: none;
  padding: 6px 10px;
  border-radius: 8px;
}

.nav a.active {
  background: var(--primary-weak);
  color: var(--primary-strong);
}
</style>
