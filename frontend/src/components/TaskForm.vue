<script setup>
import { computed, reactive, watch } from 'vue'

const props = defineProps({
  modelValue: { type: Object, required: true },
  submitText: { type: String, default: 'Сохранить' }
})

const emit = defineEmits(['update:modelValue', 'submit', 'cancel'])

const form = reactive({
  title: props.modelValue.title ?? '',
  description: props.modelValue.description ?? '',
  priority: props.modelValue.priority ?? 'medium',
  category: props.modelValue.category ?? 'other',
  important: props.modelValue.important ?? false,
  completed: props.modelValue.completed ?? false
})

watch(
  () => props.modelValue,
  (v) => {
    form.title = v.title ?? ''
    form.description = v.description ?? ''
    form.priority = v.priority ?? 'medium'
    form.category = v.category ?? 'other'
    form.important = v.important ?? false
    form.completed = v.completed ?? false
  },
  { deep: true }
)

watch(
  () => ({ ...form }),
  (v) => emit('update:modelValue', v),
  { deep: true }
)

const errors = computed(() => {
  const e = {}
  if (!form.title || form.title.trim().length === 0) e.title = 'Заголовок обязателен'
  if (form.title && form.title.trim().length > 120) e.title = 'Слишком длинный заголовок'
  if (form.description && form.description.length > 2000) e.description = 'Слишком длинное описание'
  return e
})

const isValid = computed(() => Object.keys(errors.value).length === 0)

// watch: подсказка, если заголовок слишком короткий
const titleHint = computed(() => {
  const len = form.title?.trim().length || 0
  if (len > 0 && len < 3) return 'Заголовок лучше сделать длиннее (>= 3 символов)'
  return ''
})

function onSubmit() {
  if (!isValid.value) return
  emit('submit', {
    title: form.title.trim(),
    description: form.description.trim(),
    priority: form.priority,
    category: form.category,
    important: form.important,
    completed: form.completed
  })
}
</script>

<template>
  <form class="form" @submit.prevent="onSubmit">
    <div class="field">
      <label>Заголовок</label>
      <input v-model.trim="form.title" type="text" placeholder="Например: Сделать форму" />
      <div v-if="errors.title" class="error">{{ errors.title }}</div>
      <div v-else-if="titleHint" class="hint">{{ titleHint }}</div>
    </div>

    <div class="field">
      <label>Описание</label>
      <textarea v-model.trim.lazy="form.description" rows="4" placeholder="Описание задачи..."></textarea>
      <div v-if="errors.description" class="error">{{ errors.description }}</div>
    </div>

    <div class="field">
      <label>Приоритет</label>
      <select v-model="form.priority">
        <option value="low">low</option>
        <option value="medium">medium</option>
        <option value="high">high</option>
      </select>
    </div>

    <div class="field">
      <label>Категория</label>
      <div class="radios">
        <label><input v-model="form.category" type="radio" value="work" /> work</label>
        <label><input v-model="form.category" type="radio" value="study" /> study</label>
        <label><input v-model="form.category" type="radio" value="home" /> home</label>
        <label><input v-model="form.category" type="radio" value="other" /> other</label>
      </div>
    </div>

    <div class="field row">
      <label class="check"><input v-model="form.important" type="checkbox" /> Важно</label>
      <label class="check"><input v-model="form.completed" type="checkbox" /> Выполнено</label>
    </div>

    <div class="actions">
      <button class="btn" type="submit" :disabled="!isValid">{{ submitText }}</button>
      <button class="btn secondary" type="button" @click="$emit('cancel')">Отмена</button>
    </div>
  </form>
</template>

<style scoped>
.form {
  display: grid;
  gap: 12px;
}

.field {
  display: grid;
  gap: 6px;
}

input,
textarea,
select {
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 8px 10px;
  font: inherit;
}

.radios {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.row {
  display: flex;
  gap: 12px;
}

.check {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.btn {
  border: 1px solid var(--primary);
  background: var(--primary);
  color: #ffffff;
  padding: 8px 12px;
  border-radius: 10px;
}

.btn[disabled] {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn.secondary {
  border-color: var(--border);
  background: var(--primary-weak);
  color: var(--primary-strong);
}

.error {
  color: var(--danger);
  font-size: 13px;
}

.hint {
  color: var(--muted);
  font-size: 13px;
}
</style>
