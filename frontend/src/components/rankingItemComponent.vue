<template>
  <div class="itemContainer">
    <div style="width: 5%;">{{index+1}}</div>
    <router-link 
      style="width: 40%;" 
      class="name"
      :class="{current_logged_in: checkLoggedPlayer}"
      :to="{name: 'ProfileView', params: {uuid: `${this.player.uuid}`}}"
    >
        {{player.name}}
    </router-link>
    <div style="width: 10%;">{{player.race}}</div>
    <div style="width: 10%;">{{player.lvl}}</div>
    <div class="buttons_container">
        <div><i class="fa-solid fa-magnifying-glass"></i></div>
        <div><i class="fa-solid fa-gun"></i></div>
        <div><i class="fa-solid fa-plus"></i></div>
    </div>
  </div>
</template>

<script>

export default {
  name:'rankingItemComponent',
  props: ['player', 'index', 'loggedIn'],
    data() {
      return {
      }
    },
    computed: {
        checkLoggedPlayer() {
          return this.loggedIn.name == this.player.name
        }
    },
  created() {
  }
}
</script>

<style scoped>
.itemContainer {
    display: flex;
    align-items: center;

    width: 95%;
    height: 50px;
    margin: 5px 0 5px 0;
    background-color: rgb(255, 255, 255);

    border-radius: 5px;
}

.buttons_container {
    width: 35%;
    padding: 5px;
    display: flex;
    justify-content:space-evenly;
}
.name {
  text-decoration: none;
  color: black;
}

.current_logged_in {
  color: rgb(68, 0, 255);
}

.name:hover{
    text-decoration: underline;
}
</style>