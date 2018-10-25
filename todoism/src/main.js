import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Login from './components/Login.vue'
import Record from './components/Record.vue'
import fake from './static/js/faker'
import axios from 'axios'

// axios.defaults.baseURL = 'http://todoism.com/api'


Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.prototype.$http = axios
Vue.prototype.fake = fake
const routes = [
    {path: '/', component: Login},
    {path: '/record', component: Record}
]

const router = new VueRouter({
    routes
})

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
