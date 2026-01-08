<script setup>
const props = defineProps({
  task: { type: Object, required: true }
})

const emit = defineEmits(['delete', 'toggle', 'edit'])

function onToggle() {
  emit('toggle', props.task)
}

function onDelete() {
  emit('delete', props.task)
}

function onEdit() {
  emit('edit', props.task)
}
</script>

<template>
  <article class="item" :class="{ done: task.completed, important: task.important }">
    <div class="top">
      <div class="title">
        <span class="badge" v-if="task.important">Важно</span>
        <strong>{{ task.title }}</strong>
      </div>
      <div class="meta">
        <span class="pill">{{ task.priority }}</span>
        <span class="pill">{{ task.category }}</span>
      </div>
    </div>

    <p v-if="task.description" class="desc">{{ task.description }}</p>

    <div class="actions">
      <button class="btn" type="button" @click="onEdit">Редактировать</button>
      <button class="btn" type="button" @click="onToggle">Изменить статус</button>
      <button class="btn danger" type="button" @click="onDelete">Удалить</button>
    </div>
  </article>
</template>

<style scoped>
.item {
  border: 1px solid var(--border);
  border-radius: 12px;
  background: var(--surface);
  padding: 12px;
}

.item.done {
  opacity: 0.75;
}

.top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 10px;
}

.title {
  display: flex;
  align-items: center;
  gap: 8px;
}

.badge {
  font-size: 12px;
  padding: 2px 8px;
  border-radius: 999px;
  background: var(--primary-weak);
  color: var(--primary-strong);
}

.meta {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.pill {
  font-size: 12px;
  padding: 2px 8px;
  border-radius: 999px;
  background: #fff7fa;
  border: 1px solid var(--border);
  color: var(--muted);
}

.desc {
  margin: 8px 0 0;
  color: var(--text);
}

.actions {
  margin-top: 10px;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.btn {
  border: 1px solid var(--border);
  background: var(--surface);
  padding: 6px 10px;
  border-radius: 10px;
}

.btn.danger {
  border-color: var(--danger);
  background: var(--danger-weak);
}
</style>
