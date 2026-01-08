<script setup>
import { useRouter } from 'vue-router'
import LayoutCard from '../components/LayoutCard.vue'

const router = useRouter()
</script>

<template>
  <LayoutCard>
    <template #header>
      <h1 class="h1">404</h1>
    </template>

    <p class="p">Страница не найдена.</p>
    <button class="btn" type="button" @click="router.push({ name: 'home' })">На главную</button>
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
</style>
