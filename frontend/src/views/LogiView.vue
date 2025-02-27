<template>

  <LogiView />
</template>

<script>
import LogiView from '@/components/LoginView.vue';

export default {
  components: {
    LogiView
  }
};
</script>

<style scope>
.contai {
  background-image: url(../assets/fondo_longo.jpeg);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-shadow: 0px 0px 5px rgb(9, 0, 0);
}


</style>
