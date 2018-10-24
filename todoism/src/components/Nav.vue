<template>
    <div class="td_nav">
        <div class="td_main">
            <router-link to="/">Home</router-link>
            <router-link to="/record">Go to record</router-link>
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

    }

</style>
