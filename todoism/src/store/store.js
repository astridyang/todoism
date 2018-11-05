/**
 * Created on 11/2/2018.
 */
import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
export default new Vuex.Store({
    state: {
        token: '222'
    },
    mutations: {
        set_token (state, token) {
            state.token = token
        }
    }
})
