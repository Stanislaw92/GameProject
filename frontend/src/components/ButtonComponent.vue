<template>
    <button :class="{secondary: style_of_button=='secondary', combat1v1style: style_of_button=='combat1v1'}"> 
        <slot/>
    </button>
</template>

<script>
export default {
    props: ['style_of_button'],
    created() {
    }
}   
</script>

<style scoped>
button {
  background: #0a1820;
  font-family: inherit;
  padding: 0.3em 0.7em;
  font-weight: 600;
  font-size: 14px;
  border: 3px solid ;
  border-color: rgb(0, 161, 193);
  border-radius: 0.4em;
  box-shadow: 0.1em 0.1em;
  margin-top: 5px;
  color: rgb(0, 161, 193);
}


button:hover {
  transform: translate(-0.05em, -0.05em);
  box-shadow: 0.15em 0.15em;
}

button:active {
  transform: translate(0.05em, 0.05em);
  box-shadow: 0.05em 0.05em;
}

.secondary { 
  border-color: rgb(53, 112, 77);
  color: rgb(53, 112, 77);
}

.combat1v1style {
  border-color: #BA9F9F;
  color: #BA9F9F;
}
</style>