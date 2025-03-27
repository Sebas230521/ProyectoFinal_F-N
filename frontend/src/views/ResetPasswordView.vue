<template>
    <div id="container">

        <ResetPassword />
    </div>
</template>

<script>
import ResetPassword from '@/components/ResetPassword.vue';

export default {
    components: {
        ResetPassword
    }
};
</script>

<style scoped>
#container{
    background: #91a1ac; 
    background: -webkit-linear-gradient(to top, #0080ff, #333537);  
    background: linear-gradient(to bottom, #033450, #F56217);
    }
</style>