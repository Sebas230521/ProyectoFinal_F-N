<template>
  <div class="c d-flex align-items-center justify-content-center">
    <div class="container " id="ct">
      <div class="row align-items-center">
        <div class="col-12 col-md-6 d-flex justify-content-center mb-3">
          <img src="../assets/Logo_Fish-Nexus.png" alt="Logo" class="logo-responsive">
        </div>
        <div class="col-12 col-md-6">
          <RegistView/>
        </div>
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
.c {
  background-image: url(../assets/Fondo-Registrar.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  
}

#ct {
  background-color: rgba(255, 255, 255, 0.6);
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(222, 180, 111, 0.962);
  padding: 45px;

}

.logo-responsive {
  width: 280px;

  object-fit: cover;
}
</style>
