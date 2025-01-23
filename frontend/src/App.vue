<template>
  <div class="appContainer">
    
    <NavbarComponent
    />
    <notifications classes="customNotification" position="top center" width="500px"/>
    <PageComponent>
      <router-view/>
    </PageComponent>
  </div>

</template>

<script>
import PageComponent from './components/pageComponent.vue'
// import { axios } from '@/common/api.service.js';
import NavbarComponent from "@/components/NavbarComponent.vue";
// import AlertComponent from "@/components/AlertComponent.vue"

export default {
    components: {
        NavbarComponent,
        PageComponent
        // AlertComponent
    },
    data() {
      return {
      }
    },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.vue-notification-group {
  top: 55px!important;
}

.customNotification {
  margin: 0 5px 5px;
  padding: 10px;
  font-size: 12px;
  color: #ffffff;
  border-radius: 20px;

  background: #44a4fc;
  border-left: 5px solid #187fe7;
}

.customNotification.success {
  background: #68cd86;
  border-left-color: #42a85f00;
}

.customNotification.warn {
  background: #ffb648;
  border-left-color: #f4890600;
}

.customNotification.error {
  background: #e54d42;
  border-left-color: #b82e2400;
}


.appContainer {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.home {
  /* margin: auto; */
  padding: 10px;
  height: 90vh;
  width: 90%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  border: 1px solid black;
  border-radius: 50px;
  box-shadow: 0px 0px 10px rgb(3, 0, 91);
}

</style>
