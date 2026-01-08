<script setup>
import TaskItem from './TaskItem.vue'

const props = defineProps({
  tasks: { type: Array, required: true }
})

const emit = defineEmits(['delete', 'toggle', 'edit'])

function onDelete(task) {
  emit('delete', task)
}

function onToggle(task) {
  emit('toggle', task)
}

function onEdit(task) {
  emit('edit', task)
}

function countCompleted() {
  return props.tasks.filter(t => t.completed).length
}
</script>

<template>
  <div class="list">
    <!-- Scoped slot: summary -->
    <slot name="summary" :total="tasks.length" :completed="countCompleted()" />

    <div v-if="tasks.length === 0" class="empty">
      Список задач пуст.
    </div>

    <div v-else class="items">
      <TaskItem
        v-for="task in tasks"
        :key="task.id"
        :task="task"
        @delete="onDelete"
        @toggle="onToggle"
        @edit="onEdit"
      />
    </div>
  </div>
</template>

<style scoped>
.items {
  display: grid;
  gap: 12px;
}

.empty {
  padding: 14px;
  border: 1px dashed var(--border);
  border-radius: 12px;
  background: var(--card-header);
  color: var(--muted);
}
</style>
