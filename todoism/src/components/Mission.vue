<template>
    <div class="td_mission">
        <div class="mission_table">
            <form action="">
                <div class="plan" v-for="plan in plans" :key="plan.id">
                    <h3>plan name ({{plan.planed_time}}h/{{plan.used_time}}h)</h3>
                    <ul class="mission-list">
                        <li>
                            <span class="name">mission name</span>
                            <input type="text" class="used-time">
                        </li>
                        <li>
                            <span class="name">mission name</span>
                            <input type="text" class="used-time">
                        </li>
                    </ul>
                </div>
                <div class="total text-right">
                    sum: {{scores}} scores
                    <p><button>submit</button></p>
                </div>

            </form>
        </div>
    </div>
</template>
<script>

    export default{
        name:'Mission',
        data () {
            return {
                plans:[
                    {
                        id: 1,
                        name: "plan1",
                        cate_id: 1,
                        planed_time:50,
                        used_time: 20,
                        expire_date: '2018-12-2',
                        missions:[
                            {
                                id: 1,
                                name: 'mission1'
                            }
                        ]
                    }
                ],
                message:'',
                scores: 0
            }
        },
        mounted () {
            this.getCategories();
        },
        methods: {
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
    .mission-list{
        li{
            display: flex;
            margin-bottom: 10px;
            .name{
                flex: 1;
            }
            input{
                width: 100px;
                margin: 0 20px;
            }
        }
    }
</style>
