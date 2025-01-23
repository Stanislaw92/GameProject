<template>
  <ContainerComponent class="custom_container">
    <div class="main_img">
        <img src="../../../static/photos/modifications.png" alt="">
    </div>

    <div class="list_of_stats">
            <div class="item">
                <p> stat 1 </p> 
                <p> {{ checkCost(stats_to_up[0]) }} </p>
                <div class="width50">
                    <div class="icons_cont">
                        <i @click="plusStat(0)" class="fa-solid fa-plus" style="color: #000000;"></i>
                        <i @click="minusStat(0)" class="fa-solid fa-minus" style="color: #000000;"></i>
                    </div>
                    <span
                        :class="{ green: stats_to_up[0]>profile.stat1}"
                    >{{stats_to_up[0]}}</span> 
                </div>
            </div>
            <div class="item">
                <p> stat 2 </p> 
                <p> {{ checkCost(stats_to_up[1]) }} </p>
                <div class="width50">
                    <div class="icons_cont">
                        <i @click="plusStat(1)" class="fa-solid fa-plus" style="color: #000000;"></i>
                        <i @click="minusStat(1)" class="fa-solid fa-minus" style="color: #000000;"></i>
                    </div>
                    <span
                        :class="{ green: stats_to_up[1]>profile.stat2}"
                    >{{stats_to_up[1]}}</span> 
                </div>
            </div>
            <div class="item">
                <p> stat 3 </p> 
                <p> {{ checkCost(stats_to_up[2]) }} </p>
                <div class="width50">
                    <div class="icons_cont">
                        <i @click="plusStat(2)" class="fa-solid fa-plus" style="color: #000000;"></i>
                        <i @click="minusStat(2)" class="fa-solid fa-minus" style="color: #000000;"></i>
                    </div>
                    <span
                        :class="{ green: stats_to_up[2]>profile.stat3}"
                    >{{stats_to_up[2]}}</span> 
                </div>
            </div>
            <div class="item">
                <p> stat 4 </p>
                <p> {{ checkCost(stats_to_up[3]) }} </p>
                <div class="width50">
                    <div class="icons_cont">
                        <i @click="plusStat(3)" class="fa-solid fa-plus" style="color: #000000;"></i>
                        <i @click="minusStat(3)" class="fa-solid fa-minus" style="color: #000000;"></i>
                    </div>
                    <span
                        :class="{ green: stats_to_up[3]>profile.stat4}"
                    >{{stats_to_up[3]}}</span> 
                </div>
            </div>
            <div class="item">
                <p> stat 5 </p>
                <p> {{ checkCost(stats_to_up[4]) }} </p>
                <div class="width50">
                    <div class="icons_cont">
                        <i @click="plusStat(4)" class="fa-solid fa-plus" style="color: #000000;"></i>
                        <i @click="minusStat(4)" class="fa-solid fa-minus" style="color: #000000;"></i>
                    </div>
                    <span
                        :class="{ green: stats_to_up[4]>profile.stat5}"
                    >{{stats_to_up[4]}}</span> 
                </div>
            </div>
            <div class="item pts">
                <span> training points: {{points_left}} </span>
                <div class="icons_cont">
                    <i @click="trainStats" class="fa-solid fa-check" style="color: #000000;"></i>
                    <i @click="refreshPoints" class="fa-solid fa-arrows-rotate" style="color: #000000;"></i>
                </div>
            </div>
    </div>

  </ContainerComponent>
</template>

<script>
import { axios } from '@/common/api.service.js';
import ContainerComponent from '../components/containerComponent.vue'
export default {
    name: 'TrainingView',
    components: {
        ContainerComponent
    },
    data() {
        return {
            profile: '',
            stats_to_up: [
                0,
                0,
                0,
                0,
                0
            ],
            base_stats: [],
            points_left: 0
        }
    },
    methods: {
        async getProfileData() {
            let endpoint = '/api/v1/profiles/'
            try {
                const response = await axios.get(endpoint)
                this.profile = response.data[0]
                console.log(this.profile)

                this.stats_to_up[0] = this.profile.stat1
                this.stats_to_up[1] = this.profile.stat2
                this.stats_to_up[2] = this.profile.stat3
                this.stats_to_up[3] = this.profile.stat4
                this.stats_to_up[4] = this.profile.stat5

                this.base_stats[0] = this.profile.stat1
                this.base_stats[1] = this.profile.stat2
                this.base_stats[2] = this.profile.stat3
                this.base_stats[3] = this.profile.stat4
                this.base_stats[4] = this.profile.stat5
                
                this.points_left = this.profile.training_points



            } catch (error) {
                        console.log(error.response);
                        alert(error.response.statusText);
            }
        },
        plusStat(x){
            if ( this.points_left >= this.checkCost(this.stats_to_up[x])) {
                this.stats_to_up[x] += 1
                this.points_left -= this.checkCost(this.stats_to_up[x]-1)

            }
            
        },
        minusStat(x){
            if ( this.stats_to_up[`${x}`] > this.base_stats[`${x}`]) {
                this.stats_to_up[`${x}`] -= 1   
                this.points_left += this.checkCost(this.stats_to_up[x])
            }
        },
        refreshPoints() {
            for ( let i=0; i<4; i++) {
                this.stats_to_up[i] = this.base_stats[i]
            }
            this.points_left = this.profile.training_points
        },
        async trainStats() {
            const endpoint = `/api/v1/profiles/${this.profile.uuid}/`
            try {
                let textForNotify = 'You have succesfully upgraded your '

                if ( this.stats_to_up[0] - this.base_stats[0] ) {
                    textForNotify += `stat1 by: ${this.stats_to_up[0] - this.base_stats[0]}`
                }
                if ( this.stats_to_up[1] - this.base_stats[1] ) {
                    textForNotify += ` stat2 by: ${this.stats_to_up[1] - this.base_stats[1]}`
                }
                if ( this.stats_to_up[2] - this.base_stats[2] ) {
                    textForNotify += ` stat3 by: ${this.stats_to_up[2] - this.base_stats[2]}`
                }
                if ( this.stats_to_up[3] - this.base_stats[3] ) {
                    textForNotify += ` stat4 by: ${this.stats_to_up[3] - this.base_stats[3]}`
                }
                if ( this.stats_to_up[4] - this.base_stats[4] ) {
                    textForNotify += ` stat5 by: ${this.stats_to_up[4] - this.base_stats[4]}`
                }


                const result = await axios.put(endpoint, {
                    stat1: this.stats_to_up[0],
                    stat2: this.stats_to_up[1],
                    stat3: this.stats_to_up[2],
                    stat4: this.stats_to_up[3],
                    stat5: this.stats_to_up[4],
                    training_points: this.points_left
                })
                console.log(result)
                this.getProfileData()
                this.$notify({
                    title: "Training",
                    text: `${textForNotify}`,
                    duration: 4000,
                    type: 'success'
                });
            } catch (error){
                console.log(error)
            }
        }


    },
    computed: {
        checkCost: function() {
            return function(x) {
                return 10 + Math.round(x*2.4)
            }
        }
    },
    created() {
        this.getProfileData()
    }
    
}
</script>

<style scoped>
i {
    cursor: pointer;
}

img {
    object-fit: cover;
    width: 100%;
    height: 100%;
    border-radius: 5%;
    object-position: top;
}

span {
    font-weight: 600;
}

.custom_container {
    flex-direction: row;
    width: 90%;
    background-color: black;
}
.list_of_stats {
    width: 55%;
    display: flex;
    justify-content: center;
    align-items: flex-end;
    flex-direction: column;

    font-size: 14px;
}
.main_img {
    width: 40%;
    height: 350px;

}

.item {
    display: flex;
    align-items: center;
    justify-content: space-between;

    width: 95%;
    height: 50px;
    margin: 5px 0 5px 0;
    background-color: rgb(255, 255, 255);

    padding: 5px 10px 5px 15px;
    border-radius: 5px;
}

.item p {
    /* width: 15%; */
    margin-bottom: 0;
}

.item div {
    display: flex;
    justify-content: space-around;
    align-items: center;
}

.item div span {
    width: 50%;
}

.width50 {
    width: 30%;
}

.icons_cont {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 35%;
}

.green { 
    color: green;
}

.pts {
    justify-content: space-around;
    align-items: center;
}


</style>