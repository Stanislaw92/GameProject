<template>

    <nav class="navbar">
        <div class="navbar_container">

            <router-link 
                :to="{name: 'home'}" 
                class="navbar_brand"    
                :class="{ actual_page: $route.path == '/'}"
            >
                <!-- :style="$route.path=='/'?{borderBottom: '3px solid #ecd08b', color: '#ecd08b'}:{}" -->

                Game
            </router-link>

            <router-link 
                :to="{name: 'ArmoryView'}" 
                class="navbar_brand small-1"    
                :class="{ actual_page: $route.path == '/armory/'}"
            >
                Armory
            </router-link>
            <router-link 
                :to="{name: 'TrainingView'}" 
                class="navbar_brand small-1"    
                :class="{ actual_page: $route.path == '/training/'}"
            >
                Training
            </router-link>

            <router-link 
                :to="{name: 'TripView'}" 
                class="navbar_brand small-1"    
                :class="{ actual_page: $route.path == '/tripView/'}"
            >
                
                <div>
                    Trip
                    <span 
                        class="tripsNum"
                    >
                        <!-- ({{logged_in_profile.trips}}/32) -->
                        ({{trips.trips}}/32)
                    </span>
                </div>
            </router-link>

            <router-link 
                :to="{name: 'RankingView'}" 
                class="navbar_brand small-1"    
                :class="{ actual_page: $route.path == '/ranking/'}"
            >
                Ranking
            </router-link>

            <router-link 
                :to="{name: 'MessagesView'}" 
                class="navbar_brand small-1"    
                :class="{ actual_page: $route.path == '/messages/'}"
            >
                Messages
            </router-link>
            <router-link 
                :to="{name: 'AmbushView'}" 
                class="navbar_brand small-1"    
                :class="{ actual_page: $route.path.includes('/ambush')}"
            >
                Ambush
            </router-link>




        </div>
    </nav>
</template>

<script>
import { useLoggedInProfile } from '../stores/store'
import { useTripStore } from '@/stores/store.js'
import { axios } from '@/common/api.service.js';
export default {

    name: 'NavbarComponent',
    components: {

    },
    data() {
        return {
            
            logged_in_profile: {},
            trips: useTripStore(),
            profileStore: useLoggedInProfile()
        }
    },
    methods: {
        async refreshData(){
            let endpoint = '/api/v1/profiles/'
            try {
                const response = await axios.get(endpoint)
                this.logged_in_profile = response.data[0]
                console.log(this.logged_in_profile)
                this.trips.updatedTrips(this.logged_in_profile.trips)
                this.trips.updateTimer(this.logged_in_profile.trip_cooldown)
                this.profileStore.updateProfile(this.logged_in_profile)
            } catch (error) {
                console.log(error.response);
                alert(error.response.statusText);
            }
        },
        
    },
    created(){
        // this.refreshData()
    },
    watch: {
        $route (){
            this.refreshData()
            
        }
    }
}
</script>

<style scoped>
.navbar {
    display: flex;
    align-items: flex-end;
    justify-content: flex-start;
    width: 90%;
    height: 50px;
    border-bottom: 1px rgba(60, 60, 60, 0.353) solid;
    margin-bottom: 10px;
    /* background-color: rgba(165, 165, 165, 0.242); */
    padding: 0;
}
.navbar_container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 80%;
    /* margin-left: 20%; */

}
.navbar_brand {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: Comic Sans MS, Comic Sans, cursive;
    color: black;
    text-decoration: none;
    font-size: 20px;
    margin-left: 20px;
    border-bottom: 3px solid rgba(0, 161, 193, 0);

}   

/* .navbar_brand:focus {
    border: 3px solid rgba(0, 161, 193, 0.614);
    box-shadow: 1px 0px 1px 0px rgba(0, 161, 193, 0.614);
} */

.actual_page {
    border-bottom: 3px solid rgb(0, 161, 193);
    /* border: 0 0 3px 0 solid rgb(0, 161, 193); */
    color: rgb(0, 161, 193);
}

.small-1 {
    font-size: 15px
}
.tripsNum {
    font-size: 12px;
    transform: translateY(1.5px);
}
</style>