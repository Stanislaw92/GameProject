<template>
        <RankingListComponent 
            class="List_container"
            :players = 'players'
        > </RankingListComponent>
</template>

<script>
import { axios } from '@/common/api.service.js';
import RankingListComponent from '../components/rankingListComponent.vue';
export default {
  name: 'RankingView',
  components: {
        RankingListComponent
  },
  data() {
    return {
        players: []
    }
  },
  methods: {
    async getPlayersList(){
        const endpoint = `/api/v1/all_profiles/`
        try {
            const response = await axios.get(endpoint)
            this.players.push(...response.data)
            } catch (error) {
                console.log(error.response);
                alert(error.response.statusText);
            }
    }
  },
  created() {
    this.getPlayersList()
  }
}
</script>

<style scoped>
.List_container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width: 100%;
    background-color: rgb(238, 238, 238);
    padding: 10px 0px 10px 0px;
    margin-top: 20px;
    border-radius: 5px;
}
</style>