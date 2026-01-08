<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="layout">
    <div class="tabs">
      <RouterLink class="tab" :to="{ name: 'tasks.list' }">Список</RouterLink>
      <RouterLink class="tab" :to="{ name: 'tasks.new' }">Создать</RouterLink>
    </div>

    <RouterView />
  </div>
</template>

<style scoped>
.layout {
  display: grid;
  gap: 12px;
}

.tabs {
  display: flex;
  gap: 8px;
}

.tab {
  text-decoration: none;
  padding: 8px 10px;
  border-radius: 10px;
  border: 1px solid var(--border);
  background: var(--surface);
}
</style>
