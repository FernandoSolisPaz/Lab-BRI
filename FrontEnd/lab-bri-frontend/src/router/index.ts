import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NewsMap from '@/views/NewsMap.vue'
import NewsView from '@/views/NewsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: NewsMap,
    },
    {
      path: '/newsview',
      name: 'newsview',
      component: NewsView,
    }
  ],
})

export default router
