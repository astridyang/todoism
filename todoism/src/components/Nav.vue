<template>
    <div class="td_nav">
        <div class="wrap_main">
            <router-link to="/">Home</router-link>
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
        background: var(--pink);
        color: var(--white);
        a{
            line-height:var(--navHeight);
            color: var(--white);
        }
    }


</style>
