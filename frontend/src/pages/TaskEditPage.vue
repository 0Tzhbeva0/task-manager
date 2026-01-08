<script setup>
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import LayoutCard from '../components/LayoutCard.vue'
import TaskForm from '../components/TaskForm.vue'
import { tasksApi } from '../api/tasksApi'

const route = useRoute()
const router = useRouter()

const taskId = Number(route.params.id)

const taskDraft = ref({
  title: '',
  description: '',
  priority: 'medium',
  category: 'other',
  important: false,
  completed: false
})

const loading = ref(false)
const saving = ref(false)
const error = ref('')

async function load() {
  loading.value = true
  error.value = ''
  try {
    const data = await tasksApi.get(taskId)
    taskDraft.value = {
      title: data.title,
      description: data.description,
      priority: data.priority,
      category: data.category,
      important: data.important,
      completed: data.completed
    }
  } catch (e) {
    error.value = e?.message || 'Не удалось загрузить задачу'
  } finally {
    loading.value = false
  }
}

onMounted(load)

async function submit(payload) {
  saving.value = true
  error.value = ''
  try {
    await tasksApi.update(taskId, payload)
    router.push({ name: 'tasks.list' })
  } catch (e) {
    error.value = e?.message || 'Ошибка сохранения'
  } finally {
    saving.value = false
  }
}
</script>

<template>
  <LayoutCard>
    <template #header>
      <h1 class="h1">Редактировать задачу</h1>
    </template>

    <div v-if="error" class="error">{{ error }}</div>
    <div v-if="loading" class="muted">Загрузка...</div>

    <TaskForm
      v-else
      v-model="taskDraft"
      submit-text="Сохранить"
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
