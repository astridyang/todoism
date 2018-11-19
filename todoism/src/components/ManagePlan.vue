<template>
    <div class="manage-plan">
        <ul>
            <li v-for="plan in plans" :key="plan.id">
                <span class="name">{{plan.name}}</span>
                <span class="count">mission count</span>
                <span class="operation">
                    <button>edit</button>
                    <button>delete</button>
                </span>
            </li>
        </ul>
    </div>
</template>
<script>
    export default{
        name: 'ManagePlan',
        data () {
            return {
                "plans": []
            }
        },
        mounted () {
            let _this = this;
            this.$http.get('/user/plans')
                .then(res => {
                    _this.plans = res.data.plans
                })
        }
    }
    /**
     *
     */

</script>
<style>

</style>
