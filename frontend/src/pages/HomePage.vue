<script setup>
import { useRouter } from 'vue-router'
import LayoutCard from '../components/LayoutCard.vue'

const router = useRouter()

function goToTasks() {
  router.push({ name: 'tasks.list' })
}
</script>

<template>
  <LayoutCard>
    <template #header>
      <h1 class="h1">Добро пожаловать</h1>
    </template>

    <p class="p"></p>

    <button class="btn" type="button" @click="goToTasks">Перейти к задачам</button>

    <template #footer></template>
  </LayoutCard>
</template>

<style scoped>
.h1 {
  margin: 0;
  font-size: 22px;
}

.p {
  margin: 0 0 12px;
}

.btn {
  border: 1px solid var(--primary);
  background: var(--primary);
  color: #ffffff;
  padding: 10px 14px;
  border-radius: 10px;
}

.muted {
  color: var(--muted);
}
</style>
