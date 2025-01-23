import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import Notifications from '@kyvg/vue3-notification'


const pinia = createPinia()

createApp(App).use(Notifications).use(router).use(pinia).mount('#app')
