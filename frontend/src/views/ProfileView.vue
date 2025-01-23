<template>
    <ProfileInspectComponent :profile='profile'/>
</template>

<script>
import { axios } from '@/common/api.service.js';
import ProfileInspectComponent from '../components/profileInspectComponent.vue';

export default {

    name: 'ProfileView',
    props: ['uuid'],
    data() {
        return {
            profile: {}
        }
    },
    components: {
        ProfileInspectComponent
    },
    methods: {
        async getProfile(){
            const endpoint = `/api/v1/profiles/${this.uuid}/`
            try {
                const response = await axios.get(endpoint)
                this.profile = response.data
                console.log(this.profile)
                } catch (error) {
                    console.log(error.response);
                    alert(error.response.statusText);
                }
        }
    },
    created() {
        this.getProfile()
    }
}
</script>

<style scoped>

</style>