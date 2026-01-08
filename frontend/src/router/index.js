import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '../pages/HomePage.vue'
import TasksLayout from '../pages/TasksLayout.vue'
import TasksPage from '../pages/TasksPage.vue'
import TaskNewPage from '../pages/TaskNewPage.vue'
import TaskEditPage from '../pages/TaskEditPage.vue'
import NotFoundPage from '../pages/NotFoundPage.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'home', component: HomePage },
    {
      path: '/tasks',
      component: TasksLayout,
      children: [
        { path: '', name: 'tasks.list', component: TasksPage },
        { path: 'new', name: 'tasks.new', component: TaskNewPage },
        { path: ':id/edit', name: 'tasks.edit', component: TaskEditPage, props: true }
      ]
    },
    { path: '/:pathMatch(.*)*', name: 'notfound', component: NotFoundPage }
  ]
})

export default router
