<template>
    <div id="container">

        <UpdatePassword />
    </div>
</template>

<script>
import UpdatePassword from '@/components/UpdatePassword.vue';

export default {
    components: {
        UpdatePassword
    }
};
</script>


<style scoped>
#container{
    background: linear-gradient(to bottom, #eee0c7, #dacfc6); 
}
</style>








































<!-- <template>
    <div class="container vh-100 d-flex justify-content-center align-items-center">
        <div class="alert alert-success w-50 text-center">
            <h4>Cambio de contraseña exitoso</h4>
            <p>Su contraseña ha sido actualizada correctamente.</p>
        </div>
    </div>
</template>

<script>
    export default {};
</script> -->
