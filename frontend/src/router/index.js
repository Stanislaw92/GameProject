import { createRouter, createWebHistory } from 'vue-router'
import AmbushView from '../views/AmbushView.vue'
import ArmoryView from '../views/ArmoryView.vue'
import HomeView from '../views/HomeView.vue'
import RaceView from '../views/RaceChoose.vue'
import TripView from '../views/TripView.vue'
import RankingView from '../views/RankingView.vue'
import ProfileView from '../views/ProfileView.vue'
import MessagesView from '../views/MessagesView.vue'
import MessageDetailView from '../views/MessageDetailView.vue'
import TrainingView from '../views/Training.vue'
import TestBattleView from '../views/TestBattleView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/raceChoose/',
    name: 'RaceChoose',
    component: RaceView
  },
  {
    path: '/tripView/',
    name: 'TripView',
    component: TripView
  },
  {
    path: '/armory/',
    name: 'ArmoryView',
    component: ArmoryView
  },
  {
    path: '/ranking/',
    name: 'RankingView',
    component: RankingView
  },
  {
    path: '/profile_view/:uuid/',
    name: 'ProfileView',
    component: ProfileView,
    props: true
  },
  {
    path: '/messages/',
    name: 'MessagesView',
    component: MessagesView,
    // props: true
  },
  {
    path: '/training/',
    name: 'TrainingView',
    component: TrainingView,
    // props: true
  },
  {
    path: '/messages/:type/:uuid/',
    name: 'MessageDetalView',
    component: MessageDetailView,
    props: true
  },
  {
    path: '/ambush/:uuid?',
    name: 'AmbushView',
    component: AmbushView,
    props: true
  },
  {
    path: '/test_battle/',
    name: 'TestBattleView',
    component: TestBattleView,
    // props: true
  },
  

]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})

export default router
