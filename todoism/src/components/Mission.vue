<template>
    <div class="td_record">
        <div class="record_table">
            <div class="text-right"><button @click="addRecord">New record</button></div>
            <form action="">
                <!-- eslint-disable -->
                <div class="form_item" v-for="(record, index) in records">
                    <span><input type="text" class="time_span" placeholder="time span" v-model="record.time_span" :key="record.id"></span>
                    <span><input type="text" placeholder="task" v-model="record.task" :key="record.id"></span>
                    <span>
                    <select name="category" id="" v-model="record.cate">
                        <option value="0">select category</option>
                        <option :value="cate.id" :key="cate.id" v-for="cate in categories">{{cate.name}}</option>
                    </select>
                        <a href="javascript:;" class="dangerous" @click="deleteRecord(index)" v-if="records.length>1">delete</a>
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
        name:'Record',
        data () {
            return {
                records:[{id:1,time_span:'',task:'',cate:2},{id:2,time_span:'',task:'',cate:1}],
                categories:[],
                message:''
            }
        },
        mounted (){
            this.getCategories();
        },
        methods: {
            addRecord () {
                this.records.push({id:0,time_span:'',task:'',cate:0})
            },
            deleteRecord (idx) {
                this.records.splice(idx,1)
            },
            getCategories () {
                this.$http.get("/").then(res=>{
                    this.message = res.data.message
                })
            }
        }
    }
</script>
<style lang="scss">
    .td_record{
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
