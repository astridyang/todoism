<template>
    <div class="td_login">
        <h4 class="text-center">Login</h4>
        <form action="">
            <div class="form_item">
                <input type="text" placeholder="username" name="username">
            </div>
            <div class="form_item">
                <input type="password" placeholder="password" name="password">
            </div>
            <div class="form_item">
                <button>submit</button>
            </div>
        </form>
    </div>
</template>
<script>
    export default{
        name: 'Login'
    }
</script>
<style lang="scss">
    .td_login{
        margin-top: 100px;
        .form_item{
            text-align: center;
            input{
                width: 200px;
            }
        }
    }

</style>
