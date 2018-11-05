<template>
    <div class="add-plan">
        <form onsubmit="return false;">
            <div class="form-item">
                <input type="text" placeholder="name">
                <select name="category" id="">
                    <option value="">select category</option>
                </select>
            </div>
            <div class="form-item">
                <button>submit</button>
            </div>
        </form>
    </div>
</template>
<script>
    export default{
        name: 'AddPlan'
    }
</script>
<style>

</style>
