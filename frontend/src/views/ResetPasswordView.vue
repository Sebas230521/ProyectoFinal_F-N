<template>
    <ResetPassword.vue />
</template>

<script>
    export default {
        computed: {
            email() {
                return this.$route.query.email; // Obtener el email desde la URL si lo pasas como query param
            },
        },
    };
</script>
