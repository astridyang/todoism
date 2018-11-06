<template>
    <div class="modal">
        <div class="content"><slot></slot></div>
    </div>
</template>
<script>
    export default{
        name: 'Modal',
        data () {
            return {
                content: ''
            }
        }
    }
</script>
<style>

</style>
