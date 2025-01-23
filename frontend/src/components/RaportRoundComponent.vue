<template>
    <div class="round_container">
        <div class="horizontal_line">ROUND {{index+1}}</div>
        <SingleLineRaportComponentVue 
            class="round_style" 
            v-for="i in updatedRound" 
            :key="i" 
            :line = "i"  
        />
        
    </div>
    
</template>

<script>

import SingleLineRaportComponentVue from '../components/SingleLineRaportComponent.vue'
export default {
    name: 'RaportRoundComponent',
    props: ['round', 'message', 'index'],
    data() {
        return {
            updatedRound: ''
        }
    },
    components: {
        SingleLineRaportComponentVue
    },
    created() {
        this.updatedRound = this.round.replace('end of round', '').slice(1,-2).split(', ')
    }
}
</script>

<style scoped>
    .round_container {
        /* padding: 10px 20px 10px 20px; */
        padding: 0 0 20px 0;
        /* border: 1px solid black; */
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .round_style {
        font-size: 10px;
    }

    .horizontal_line {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 50px;
        margin-bottom:20px ;
        background: radial-gradient(circle, rgba(73,0,0,0.5) 0%, rgba(255,255,255,1) 100%);
    }


</style>