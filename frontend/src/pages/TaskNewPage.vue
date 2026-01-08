<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import LayoutCard from '../components/LayoutCard.vue'
import TaskForm from '../components/TaskForm.vue'
import { tasksApi } from '../api/tasksApi'

const router = useRouter()

const taskDraft = ref({
  title: '',
  description: '',
  priority: 'medium',
  category: 'other',
  important: false,
  completed: false
})

const saving = ref(false)
const error = ref('')

async function submit(payload) {
  saving.value = true
  error.value = ''
  try {
    await tasksApi.create(payload)
    router.push({ name: 'tasks.list' })
  } catch (e) {
    error.value = e?.message || 'Ошибка создания'
  } finally {
    saving.value = false
  }
}
</script>

<template>
  <LayoutCard>
    <template #header>
      <h1 class="h1">Создать задачу</h1>
    </template>

    <div v-if="error" class="error">{{ error }}</div>

    <TaskForm
      v-model="taskDraft"
      submit-text="Создать"
      @submit="submit"
      @cancel="router.push({ name: 'tasks.list' })"
    />

    <template #footer>
      <div v-if="saving" class="muted">Сохранение...</div>
    </template>
  </LayoutCard>
</template>

<style scoped>
.h1 {
  margin: 0;
  font-size: 22px;
}

.error {
  color: var(--danger);
  margin-bottom: 8px;
}

.muted {
  color: var(--muted);
}
</style>
