<template>
    <div class="td-login">
        <h4 class="text-center">Login</h4>
        <form onsubmit="return false;" method="post" name="login">
            <input type="hidden" value="password" name="grant_type">
            <div class="form-item">
                <input type="text" placeholder="username" name="username">
            </div>
            <div class="form-item">
                <input type="password" placeholder="password" name="password">
            </div>
            <div class="form-item">
                <button @click="login">submit</button>
            </div>
        </form>
    </div>
</template>
<script>
    export default{
        name: 'Login',
        data () {
          return {
              count: 0
          }
        },
        methods: {
            login () {
                let loginForm = document.forms.namedItem('login')
                let formData = new FormData(loginForm)
                this.$http({
                    method: 'post',
                    url: '/oauth/token',
                    data:formData
                }).then(res => {
                    if (res.status_code === 200) {
                        this.$store.commit('set_token', res.data.access_token)
                        this.$store.commit('set_token_type', res.data.token_type)
                        var _this = this;
                        setTimeout(function () {
                            _this.$router.push('/mission')
                        }, 1500)
                    }
                })
            }
        }
    }
</script>
<style lang="scss">
    .td-login{
        margin-top: 100px;
        .form-item{
            text-align: center;
            input{
                width: 200px;
            }
        }
    }

</style>
