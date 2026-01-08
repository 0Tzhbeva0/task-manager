<template>
  <section class="card">
    <header v-if="$slots.header" class="header">
      <slot name="header" />
    </header>

    <div class="body">
      <slot />
    </div>

    <footer v-if="$slots.footer" class="footer">
      <slot name="footer" />
    </footer>
  </section>
</template>

<style scoped>
.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
}

.header,
.footer {
  padding: 12px 14px;
  background: var(--card-header);
  border-bottom: 1px solid var(--border);
}

.footer {
  border-top: 1px solid var(--border);
  border-bottom: none;
}

.body {
  padding: 14px;
}
</style>
