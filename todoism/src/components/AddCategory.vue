<template>
    <div class="add-category">
        <h3>New Category</h3>
        <form onsubmit="return false;" method="post" name="category">
            <div class="form-item">
                <input type="text" placeholder="name" name="name">
            </div>
            <div class="form-item">
                <button @click="addCategory">Submit</button>
            </div>
        </form>
        <Modal>{{ alertMsg }}</Modal>
    </div>
</template>
<script>
    import Modal from './Modal.vue'
    export default{
        name: 'AddCategory',
        data () {
          return {
              alertMsg: '5555'
          }
        },
        components: {
            'Modal': Modal
        },
        methods: {
            addCategory () {
                let loginForm = document.forms.namedItem('login')
                let formData = new FormData(loginForm)
                let _this = this
                this.$http({
                    method: 'post',
                    data: formData,
                    url: '/user/categorise'
                }).then(res => {
                    _this.alertMsg = res.data.msg
                })
            }
        }
    }
</script>
<style>

</style>
