<template>
        <div>
                <h2 class="text-center">Formulario para añadir nuevo estanque</h2>
                <PondView />
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
</style>