<template>
    <div class="wrap-it" v-if="message.result=='True'">
        You have succesfully completed the trip.
        <br/><br/>
        thats what you found:
        <div         
            v-for="item in message.loot" 
            :key="item"
        >
            {{item.name}}
        </div>
     </div>
     <div class="wrap-it" v-else>
        You have failed the trip
     </div>
</template>

<script>
export default {
    name: 'TripMsgComponent',
    props: ['message'],
    created() {
        console.log(this.message)
    }
}
</script>

<style scoped>
.wrap-it {  
    text-align:justify;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    /* margin: auto; */
    font-size: 15px;
    /* overflow: hidden; */
    word-wrap: break-word;
    /* overflow-wrap: break-word; */
    white-space: pre-line;


}
</style>