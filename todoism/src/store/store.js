/**
 * Created on 11/2/2018.
 */
import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
// TODO actions
export default new Vuex.Store({
    state: {
        token: '',
        token_type: '',
        categorise: [],
        plans: []
    },
    mutations: {
        set_token (state, token) {
            state.token = token
        },
        set_token_type (state, type) {
            state.token_type = type
        },
        cache_categorise (state, categorise) {
            state.categorise = categorise
        },
        cache_plans (state, plans) {
            state.plans = plans
        }
    }
})
