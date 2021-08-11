/*
 * @Author: flwfdd
 * @Date: 2021-08-04 23:19:33
 * @LastEditTime: 2021-08-11 14:54:44
 * @Description: 
 * _(:з」∠)_
 */
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Login',
    name: 'Login',
    component: () => import('@/views/Login.vue')
  },
  {
    path: '/Diary',
    name: 'Diary',
    component: () => import('@/views/Diary.vue')
  },
  {
    path: '/Editor',
    name: 'Editor',
    component: () => import('@/views/Editor.vue')
  },
  {
    path: '/Render',
    name: 'Render',
    component: () => import('@/views/Render.vue')
  },
  {
    path: '/Date',
    name: 'Date',
    component: () => import('@/views/Date.vue')
  },
  {
    path: '/Flag',
    name: 'Flag',
    component: () => import('@/views/Flag.vue')
  },
]

const router = new VueRouter({
  routes
})

export default router
