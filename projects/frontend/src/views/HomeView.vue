<template>
  <div class="container mt-5" id="ct">
      <div class="row">
          <div class="col-md-6 mb-4 d-flex justify-content-center">
              <img src="../assets/Logo_Fish-Nexus.png" alt="" class="img-fluid rounded">
          </div>
          <div class="col-md-6"><!--formulario-->
              <RegistView/>
          </div>
      </div>
  </div>
</template>

<script>

import RegistView from '@/components/RegistView'

export default {
  name: 'HomeView',
  components: {
  RegistView
  }
};
</script>

<style scoped>
#ct {
  background-color: rgba(255, 255, 255, 0.4); 
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}
</style>