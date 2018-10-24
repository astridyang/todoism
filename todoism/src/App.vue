<template>
  <div id="app">
    <Nav/>
    <div class="td_main">
      <!--<img alt="Vue logo" src="./assets/logo.png">-->

      <router-view></router-view>
    </div>
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import Nav from './components/Nav.vue'
import './static/css/common.scss'
import './static/css/pink.scss'
export default {
  name: 'app',
  components: {
      Nav
  }
}
</script>

<style lang="scss">

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

}
.td_main{
  width: var(--mainWidth);
  margin:0 auto;
}
</style>
