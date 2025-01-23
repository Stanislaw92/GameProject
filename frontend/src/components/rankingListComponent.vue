<template>
    <div>
        <button @click="updateRanking">updated ranking</button>
        <div class="listDescribe_container">
            <div style="width: 5%;">#</div>
            <div style="width: 40%;">name</div>
            <div style="width: 10%;">race</div>
            <div style="width: 10%;">lvl</div>
            <div class="buttons_container">
                <div>spy</div>
                <div>atack</div>
                <div>add</div>
            </div>
        </div>
        <RankingItemComponent 
            v-for="player, index in players"
            :player="player"
            :index ="index"
            :key="player"
            :loggedIn='loggedInProfile.profile'
        ></RankingItemComponent>
    </div>
</template>

<script>
import { useLoggedInProfile } from '@/stores/store.js'
import { axios } from '@/common/api.service.js';
import RankingItemComponent from '../components/rankingItemComponent.vue';
export default {
    name: 'rankingListComponent',
	props: ['players'],
    components: {
        RankingItemComponent,
        
    },
    methods: {
        async getProfileData() {
            let endpoint = '/api/v1/profiles/'
            try {
                const response = await axios.get(endpoint)
                this.loggedInProfile = response.data[0]
                console.log(this.loggedInProfile)
            } catch (error) {
                        console.log(error.response);
                        alert(error.response.statusText);
            }
        },
        async updateRanking(){
            const endpoint = "/api/v1/updateRanking/"
            try {
                await axios.post(endpoint)
            } catch (error){
                console.log(error)
            }
        }
    },
	data() {
		return {
            loggedInProfile: '',
            profileStore: useLoggedInProfile()
        }
    },
    created() {
        this.loggedInProfile = this.profileStore
    }
}
</script>

<style scoped>
.listDescribe_container {
    display: flex;
    align-items: center;

    width: 95%;
    height: 25px;
    margin: 5px 0 5px 0;
    background-color: rgba(31, 31, 31, 0.819);

    border-radius: 5px;
    color: rgb(223, 223, 223);
}

.buttons_container {
    width: 35%;
    padding: 5px;
    display: flex;
    justify-content:space-evenly;
}
</style>