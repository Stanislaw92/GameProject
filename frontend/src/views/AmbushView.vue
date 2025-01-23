<template>


    <ContainerComponent class="custom_background">
        <div class="form-container">
                <form v-on:submit.prevent="AttackPlayer" class="form" autocomplete="off" ref="msgform">
                    <div class="form-group">
                    <label for="text">Name of player</label>

                    <input 
                        autocomplete="off"
                        type="text" 
                        id="reciever" 
                        name="reciever" 
                        required
                        v-model="search"
                        v-on:input="filterOptions"
                        placeholder="nick"
                        @keyup="checkVisibility"
                    >
                    <select  
                        class="search_options"
                        v-if="optionsVisibility"
                        v-model="selectedOption" 
                        v-bind:size="profiles.length"
                    >
                        <option 
                            class="option_style"
                            v-for="option in filteredOptions" :value="option"
                            :key="option"
                            @click="setSearchModel"
                        >
                            {{ option.name }}
                        </option>
                    </select>

                    </div>
                    <button class="form-submit-btn">Attack</button>
                </form>
            </div>
    </ContainerComponent>

</template>

<script>
import { axios } from '@/common/api.service.js';
import ContainerComponent from '../components/containerComponent.vue'
export default {
    name: 'AmbushView',
    components: {
        ContainerComponent
    },
    data() {
        return {
            search: '',
            selectedOption: '',
            profile: '',
            optionsVisibility: false,
            profiles: [],
            target_profile: '',
        }
    },
    methods: {
        async AttackPlayer() {
            let endpoint = `/api/v1/combat_result/attack/${this.target_profile.uuid}/`
            try {
                const response = await axios.post(endpoint)
                console.log(response)
            } catch(error){
                console.log(error)
            }
        },
        async getProfilesData() {
            let endpoint = '/api/v1/profiles/'
            let endpoint2 = '/api/v1/all_profiles/'
            try {

                const response = await axios.get(endpoint)
                this.profile = response.data[0]
                console.log(this.profile)

                const response2 = await axios.get(endpoint2)
                response2.data.forEach(el => {
                    if (el.name != `${this.profile.name}`) {
                        this.profiles.push(el)
                    }
                });
                console.log(this.profiles)
            } catch (error) {
                console.log(error.response);
            }
        },
        setSearchModel() {
            this.target_profile = this.selectedOption
            this.search = this.selectedOption.name
            this.optionsVisibility = false
            console.log(this.target_profile)
        },
        setOptionsVisibility() {
            this.optionsVisibility = true
        },
        checkVisibility() {
            this.filteredOptions.length ? this.optionsVisibility = true : this.optionsVisibility = false
            this.search.length ? this.optionsVisibility = true : this.optionsVisibility = false

            if ( this.filteredOptions.length && this.search.length ) {
                this.optionsVisibility = true
            } else if ( !this.filteredOptions.length || !this.search.length ){
                this.optionsVisibility = false
            }
        },
        async getReplyToObject(uuid) {
            const endpoint = `/api/v1/profiles/${uuid}/`
            try {
                const response = await axios.get(endpoint)

                this.search = response.data.name
                this.target_profile = response.data



            } catch (error){
                console.log(error)
            }
        },

    },
    created() {
        this.getProfilesData()

    },
    computed: {
        filteredOptions() {
            return this.profiles.filter(option => { 
                return option.name.toLowerCase().includes(this.search.toLowerCase());
            });
        },

    },
    
}
</script>

<style scoped>


.custom_background {
    width: 100%;
    height: 70vh;
    margin-top: 0;
    background-image: url("../../../static/photos/ambushphoto.jpg");
    background-position: center;
    background-size: cover;
}
.main_img {
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: -1;
}

.component_container{
    width: 80%;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    /* flex-direction: row; */
    /* height: 90vh; */
}

.form-container {
  width: 400px;
  background: #212121b0 padding-box;
              
  border: 2px solid transparent;
  padding: 32px 24px;
  font-size: 14px;
  font-family: inherit;
  color: white;
  display: flex;
  flex-direction: column;
  gap: 20px;
  box-sizing: border-box;
  border-radius: 16px;
  margin: 15px;
}

.form-container button:active {
  scale: 0.95;
}

.form-container .form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-container .form-group {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.form-container .form-group label {
  display: block;
  margin-bottom: 5px;
  color: rgb(255, 255, 255);
  font-weight: 600;
  font-size: 20px;
}

.form-container .form-group input {
  width: 100%;
  padding: 12px 16px;
  border-radius: 8px;
  color: #fff;
  font-family: inherit;
  background-color: rgba(0, 0, 0, 0.964);
  border: 1px solid rgb(255, 255, 255);;
}

.form-container .form-group textarea {
  width: 100%;
  padding: 12px 16px;
  border-radius: 8px;
  resize: none;
  color: #fff;
  height: 96px;
  border: 1px solid #414141;
  background-color: transparent;
  font-family: inherit;
}

.search_options{
    width: 100%;
    border-radius: 10px;
    padding: 10px;
    overflow: hidden;
    height: 80px;
    padding: 5px;
}

.option_style {
    display: flex;
    justify-content: flex-start;
    align-items: center;
}

.form-container .form-group input::placeholder {
  opacity: 0.5;
  color: rgb(255, 255, 255);;
}

.form-container .form-group input:focus {
  outline: none;
  border-color: rgb(0, 161, 193);
}

.form-container .form-group textarea:focus {
  outline: none;
  border-color: rgb(0, 161, 193);
}

.form-container .form-submit-btn {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  align-self: center;
  font-family: inherit;
  color: rgb(255, 255, 255);
  font-weight: 600;
  width: 40%;
  background: #313131;
  border: 1px solid rgb(255, 255, 255);
  padding: 12px 16px;
  font-size: inherit;
  gap: 8px;
  margin-top: 8px;
  cursor: pointer;
  border-radius: 6px;
}
</style>