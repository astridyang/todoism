<template>
    <div class="add-category">
        <h3>New Category</h3>
        <form onsubmit="return false;" method="post">
            <div class="form-item">
                <input type="text" placeholder="name">
            </div>
            <div class="form-item">
                <button>Submit</button>
            </div>
        </form>
    </div>
</template>
<script>
    export default{
        name: 'AddCategory'
    }
</script>
<style>

</style>
