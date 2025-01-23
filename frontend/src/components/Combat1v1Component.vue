<template>
    <div 
        class="wrap-it">
        <img src="../../../static/photos/clash.jpg" class="clash_image" />
        <div class="horizontal_line">
            <div>{{message.attacker }}</div>
            <div>VS</div>
            <div>{{message.victim}}</div>
        </div>
        <div class="players_stats_container">
            <div class="left_box">
                <p>{{attacker.stat1}}</p>
                <p>{{attacker.stat2}}</p>
                <p>{{attacker.stat3}}</p>
                <p>{{attacker.stat4}}</p>
                <p>{{attacker.stat5}}</p>
            </div>
            <div class="center_box">
                <p>strength</p>
                <p>agility</p>
                <p>resistance</p>
                <p>perception</p>
                <p>knowledge</p>
            </div>
            <div class="right_box">
                <p>{{victim.stat1}}</p>
                <p>{{victim.stat2}}</p>
                <p>{{victim.stat3}}</p>
                <p>{{victim.stat4}}</p>
                <p>{{victim.stat5}}</p>
            </div>
        </div>
        <div style="width:100%; padding: 0 30px 0 30px;" v-for="(round, index) in testArr" :key="round">
            <RaportRoundComponent 
                :round = "round"
                :message = "message"
                :index="index"
            />
            
        </div>
        <div class="horizontal_line">
            Winner is {{message.winner}}
        </div>
    </div> 
</template>

<script>
import RaportRoundComponent from './RaportRoundComponent.vue'
export default {
    props: ['message', 'testArr', 'victim', 'attacker'],
    name: 'Combat1v1Component',
    components: {
        RaportRoundComponent
    },
    data() {
        return {

        }
    },  
    created() {
        console.log(this.message)
        console.log(this.victim)
        console.log(this.attacker)
    }
}
</script>

<style scoped>
p{
    width: 100%;
    text-align: center;
}
p:nth-child(even) {
    background: rgba(0, 0, 0, 0.041)
}
p:nth-child(odd) {
    background: rgb(255, 255, 255)
}
.clash_image {
    width: 100%;
    /* height: 70vh; */
    margin-top: 0;
    background-position: center;
    background-size: cover;
}

.players_stats_container, .left_box, .center_box, .right_box {
    display: flex;
    justify-content: center;
    align-items: center;
}

.left_box, .center_box, .right_box {
    flex-direction: column;
    width: 100%;
}




.players_stats_container {
    margin: 20px 0px 20px 0px;
    padding: 0 30px 0 30px;
    width: 100%;
    justify-content: space-around;
}

.players_stats_container p {
    margin: 0;
}

.horizontal_line {
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 80%;
    height: 50px;
    margin-top:20px ;
    margin-bottom:20px ;
    background: radial-gradient(circle, rgba(73,0,0,0.5) 0%, rgba(255,255,255,1) 100%);
}
</style>