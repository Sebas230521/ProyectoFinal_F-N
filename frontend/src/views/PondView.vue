<template>
        <div class="background-custom min-vh-100" style="padding-bottom: 5rem;">
                <div class="col-12 d-flex justify-content-center mb-3">
                <img src="../assets/logoMenuLBlanca.png" alt="Logo" class="img-fluid logo-responsive">
                </div>
                <div>
                        <PondView />
                </div>
        </div>
</template>

<script>
import PondView from '@/components/PondView.vue';

export default {
        components: {
        PondView
        }
};
</script>
        
<style scoped>
/* h2 {
margin-top: 2rem;
margin-bottom: 1.5rem;
color: #4CAF50;
} */

.logo-responsive {
max-width: 100%;
height: auto; 
width: auto;
max-height: 300px;
}

.background-custom {
min-width: 100%;
min-height: 100vh;
max-width: 100%;
background: #009dff;  /* fallback for old browsers */
background: -webkit-linear-gradient(to bottom,#0392e6, #F56217);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to bottom,  #1c2a33, #F56217); 

}
</style>