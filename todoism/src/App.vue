<template>
  <div id="app">
    <Nav/>
    <div class="wrap_main">
      <!--<img alt="Vue logo" src="./assets/logo.png">-->
      <p>Welcome, today is </p>
      <p>You got points today.</p>
      <div class="td_main">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import Nav from './components/Nav.vue'
import './static/css/common.scss'
import './static/css/default.scss'
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
.wrap_main{
  width: var(--mainWidth);
  margin:0 auto;
}
.td_main{
  padding:30px 0;
}
</style>
