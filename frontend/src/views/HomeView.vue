<template>
  <div class="c d-flex align-items-center justify-content-center">
    <div id="ct">
      <div class="row align-items-center">
        <div class="col-12 col-md-6  d-flex justify-content-center mb-3">
          <img src="../assets/Fond.png" alt="Logo" class="logo-responsive">
        </div>
        <div class=" col-md-6 ">
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
  background-image: url(../assets/fondo_l.jpeg);
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
  background-color: rgba(255, 255, 255, 0.575);
  border-radius: 15px;
  box-shadow: 0px 4px 10px rgba(253, 156, 0, 0.962);
  padding: 30px;

}

.logo-responsive {
  width: 240px;
  object-fit: cover;
}
</style>
