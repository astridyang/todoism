import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Login from './components/Login.vue'
import Mission from './components/Mission.vue'
import axios from 'axios'
import store from './store/store'
axios.defaults.baseURL = 'http://localhost:5000/api/v1'


Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.prototype.$http = axios
const routes = [
    {path: '/', component: Login},
    {path: '/mission', component: Mission}
]

const router = new VueRouter({
    mode: 'history',
    routes
})

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')