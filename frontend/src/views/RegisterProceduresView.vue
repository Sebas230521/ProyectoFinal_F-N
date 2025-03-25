<template>
        <div class="container-fluid background-custom min-vh-100 d-flex flex-column align-items-start">
                <div class="w-100 d-flex justify-content-start p-4">
                        <button class="btn btn-danger" @click="goToMenu">
                                <i class="bi bi-box-arrow-left"></i> Atras
                        </button>
                </div>
                <div class="col-12 d-flex justify-content-center mt-2">
                        <img src="../assets/logoMenuLBlanca.png" alt="Logo" class="img-fluid logo-responsive">
                </div>
                <div class="w-100 px-3 mt-4">
                        <ProceduresForm />
                </div>
        </div>
        </template>

<script>
import ProceduresForm from '@/components/ProceduresForm.vue';

export default {
components: {
        ProceduresForm
},
methods: {
        goToMenu() {
                this.$router.push({ name: 'menu' });
        }
}
};
</script>

<style scoped>
.background-custom {
background: linear-gradient(to bottom, #033450, #F56217);
}

.logo-responsive {
max-width: 90%;
height: auto;
max-height: 150px; 
}

.mt-2 {
margin-top: 0.5rem; 
}

.mt-4 {
margin-top: 1.5rem; 
}
</style>
      