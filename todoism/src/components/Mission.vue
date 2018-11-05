<template>
    <div class="td_mission">
        <div class="mission_table">
            <div class="text-right"><button @click="addMission">New mission</button></div>
            <form action="">
                <!-- eslint-disable -->
                <div class="form_item" v-for="(mission, index) in missions">
                    <span><input type="text" class="time_span" placeholder="time span" v-model="mission.time_span" :key="mission.id"></span>
                    <span><input type="text" placeholder="task" v-model="mission.content" :key="mission.id"></span>
                    <span>
                    <select name="plan" id="" v-model="mission.plan">
                        <option value="0">select plan</option>
                        <option :value="plan.id" :key="plan.id" v-for="plan in plans">{{plan.name}}</option>
                    </select>
                        <a href="javascript:;" class="dangerous" @click="deleteMission(index)" v-if="missions.length>1">delete</a>
                </span>
                </div>
                <div class="form_item">
                    <button>submit</button>
                </div>
                {{message}}
            </form>
        </div>
    </div>
</template>
<script>

    export default{
        name:'Mission',
        data () {
            return {
                missions:[{id:0,time_span:'',content:'',plan:1}],
                plans:[],
                message:''
            }
        },
        mounted () {
            this.getCategories();
        },
        methods: {
            addMission () {
                this.missions.push({id:0,time_span:'',content:'',plan:0})
            },
            deleteMission (idx) {
                this.missions.splice(idx,1)
            },
            getCategories () {
                let _this = this
                this.$http.get("/user/categorise", {
                    headers: {'Authorization': `${this.$store.state.token_type} ${this.$store.state.token}`}
                }).then(res=>{
                    _this.plans = res.data.items
                })
            }
        }
    }
</script>
<style lang="scss">
    .td_mission{
        .form_item{
            input,select{
                margin-right: 10px;
            }
            .time_span{
                width: 120px;
            }

        }
    }
</style>
