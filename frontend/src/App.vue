<script setup>
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'
</script>

<template>
  <div class="app">
    <AppHeader />
    <main class="main">
      <RouterView />
    </main>
    <AppFooter />
  </div>
</template>

<style>
:root {
  font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  line-height: 1.5;

  /* Ало-розовая палитра */
  --bg: #fff0f6;
  --surface: #ffffff;
  --text: #1f2328;
  --muted: #6b5b66;
  --border: #ffd6e7;

  --primary: #ff2d55;
  --primary-weak: #ffe2ec;
  --primary-strong: #d20f3a;

  --danger: #ff1f3d;
  --danger-weak: #ffe3e7;

  --card-header: #fff7fa;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
}

.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main {
  flex: 1;
  max-width: 980px;
  width: 100%;
  margin: 0 auto;
  padding: 16px;
}

a {
  color: inherit;
}

button {
  cursor: pointer;
}
</style>
