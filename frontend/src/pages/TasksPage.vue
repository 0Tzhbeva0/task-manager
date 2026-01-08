<script setup>
import { computed, onMounted, ref, watch } from 'vue'
import { useRouter } from 'vue-router'

import LayoutCard from '../components/LayoutCard.vue'
import TaskList from '../components/TaskList.vue'
import { tasksApi } from '../api/tasksApi'

const router = useRouter()

const tasks = ref([])
const loading = ref(false)
const error = ref('')

const statusFilter = ref('all')
const sortBy = ref('created_at')

async function load() {
  loading.value = true
  error.value = ''
  try {
    tasks.value = await tasksApi.list()
  } catch (e) {
    error.value = e?.message || 'Ошибка загрузки'
  } finally {
    loading.value = false
  }
}

onMounted(load)

const filteredTasks = computed(() => {
  if (statusFilter.value === 'done') return tasks.value.filter(t => t.completed)
  if (statusFilter.value === 'open') return tasks.value.filter(t => !t.completed)
  return tasks.value
})

const sortedTasks = computed(() => {
  const copy = [...filteredTasks.value]

  if (sortBy.value === 'alpha') {
    copy.sort((a, b) => String(a.title).localeCompare(String(b.title), 'ru'))
    return copy
  }

  // created_at desc (newest first)
  copy.sort((a, b) => {
    const da = new Date(a.created_at).getTime() || 0
    const db = new Date(b.created_at).getTime() || 0
    return db - da
  })
  return copy
})

watch([statusFilter, sortBy], () => {
  // watch демонстрация: сбрасываем ошибку при изменении фильтров
  error.value = ''
})

async function removeTask(task) {
  if (!confirm('Удалить задачу?')) return
  try {
    await tasksApi.remove(task.id)
    await load()
  } catch (e) {
    error.value = e?.message || 'Ошибка удаления'
  }
}

async function toggleTaskStatus(task) {
  try {
    await tasksApi.update(task.id, { completed: !task.completed })
    await load()
  } catch (e) {
    error.value = e?.message || 'Ошибка обновления'
  }
}

function editTask(task) {
  router.push({ name: 'tasks.edit', params: { id: task.id } })
}
</script>

<template>
  <LayoutCard>
    <template #header>
      <div class="head">
        <h1 class="h1">Задачи</h1>
        <button class="btn" type="button" @click="router.push({ name: 'tasks.new' })">Создать</button>
      </div>
    </template>

    <div class="controls">
      <label>
        Фильтр
        <select v-model="statusFilter">
          <option value="all">все</option>
          <option value="done">выполненные</option>
          <option value="open">невыполненные</option>
        </select>
      </label>

      <label>
        Сортировка
        <select v-model="sortBy">
          <option value="created_at">по дате добавления</option>
          <option value="alpha">по алфавиту</option>
        </select>
      </label>

      <button class="btn secondary" type="button" @click="load" :disabled="loading">Обновить</button>
    </div>

    <div v-if="error" class="error">{{ error }}</div>
    <div v-if="loading" class="muted">Загрузка...</div>

    <TaskList :tasks="sortedTasks" @delete="removeTask" @toggle="toggleTaskStatus" @edit="editTask">
      <template #summary="{ total, completed }">
        <div class="summary">Всего: {{ total }}, выполнено: {{ completed }}</div>
      </template>
    </TaskList>

    <template #footer></template>
  </LayoutCard>
</template>

<style scoped>
.h1 {
  margin: 0;
  font-size: 22px;
}

.head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.controls {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: end;
  margin-bottom: 12px;
}

select {
  margin-left: 6px;
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 6px 10px;
}

.btn {
  border: 1px solid var(--primary);
  background: var(--primary);
  color: #ffffff;
  padding: 8px 12px;
  border-radius: 10px;
}

.btn.secondary {
  border-color: var(--border);
  background: var(--primary-weak);
  color: var(--primary-strong);
}

.summary {
  margin-bottom: 10px;
  color: var(--muted);
}

.error {
  color: var(--danger);
  margin-bottom: 8px;
}

.muted {
  color: var(--muted);
}
</style>
