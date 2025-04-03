<template class="c">
        

        <div class="w-100 d-flex justify-content-between align-items-center mt-3 p-2">
        <button class="btn btn-danger" @click="goToMenu">
                <i class="bi bi-box-arrow-left"></i> Atras
        </button>
        </div>


                <InformationView/>


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
.c{
        background-color: #434343;
}

</style>