<template>
        <div class="container-fluid background-custom min-vh-100 d-flex flex-column justify-content-center align-items-center">
                <div class="w-100 d-flex justify-content-start p-3">
                        <button class="btn btn-danger" @click="goToMenu">
                                <i class="bi bi-box-arrow-right"></i> Salir
                        </button>
                </div>
                <div class="col-12 d-flex justify-content-center ms-0">
                        <img src="../assets/logoMenuLBlanca.png" alt="Logo" class="img-fluid logo-responsive">
                </div>
                <div class="w-100 px-3">
                        <PondView />
                </div>
        </div>
</template>

<script>
        import PondView from '@/components/PondView.vue';

        export default {
        components: {
                PondView
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
padding-bottom: 5rem;
background: linear-gradient(to bottom, #033450, #F56217); 
}

.logo-responsive {
max-width: 90%;
height: auto;
max-height: 180px;
}
</style>