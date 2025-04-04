<template>
        <div class="full-background d-flex flex-column">
                <div class="w-100 d-flex justify-content-between align-items-center mt-3 p-2">
                <button class="btn btn-danger" @click="goToMenu">
                <i class="bi bi-box-arrow-left"></i> Atras
                </button>
                </div>

                <InformationView/>
        </div>
</template>

<script>
        import InformationView from '@/components/InformationView.vue';

        export default {
        components: {
                InformationView
        },
        methods: {
                goToMenu() {
                this.$router.push({ name: 'menu' });
                },
        },
        }
</script>

<style scoped>
.full-background {
min-height: 100vh; /* Ocupa toda la pantalla */
width: 100%;
background-color: #3f4142; /* Fondo gris claro */
color: white;
display: flex;
}
</style>
