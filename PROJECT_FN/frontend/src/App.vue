<template>
  <appHeader/>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <appPie/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import appHeader from './components/appHeader.vue'
import appPie from './components/appPie.vue';


export default {
  name: 'App',
  components: {
    HelloWorld,
    appHeader,
    appPie
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #1268b3;
  margin-top: 60px;
}
</style>
