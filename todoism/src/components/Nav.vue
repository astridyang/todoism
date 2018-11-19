<template>
    <div class="td_nav">
        <div class="wrap_main">
            <router-link to="/">Home</router-link>
            <span class="float-right">
                <router-link to="/add_category">New Category</router-link>
                <router-link to="/add_plan">New Plan</router-link>
            </span>
            <span class="float-right">
                <router-link to="/manage_category">Manage Category</router-link>
                <router-link to="/manage_plan">Manage Plan</router-link>
            </span>
            <span class="float-right">
                <router-link to="/mission_list">mission list</router-link>
            </span>
        </div>
    </div>
</template>
<script>
    export default{
        name:'Nav'
    }
</script>
<style lang="scss">
    .td_nav {
        height: var(--navHeight);
        background: var(--blue);
        color: var(--white);
        a{
            line-height:var(--navHeight);
            color: var(--white);
        }
        span{
            a{
                margin-left: 20px;
            }
        }
    }


</style>
