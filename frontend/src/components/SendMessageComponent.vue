<template>
    <div class="">

        <div class="form-container">
            <form v-on:submit.prevent="sendMessage" class="form" autocomplete="off" ref="msgform">
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
                <div class="form-group">
                    <label for="textarea" >Title</label>
                    <textarea v-model="title_text" style="height: 48px; margin-bottom: 10px;" required></textarea>
                    <label for="textarea" >Message text</label>
                    <textarea style="height: 200px;" v-model="message_text" required></textarea>
                </div>
                <button class="form-submit-btn">Send</button>
            </form>
        </div>

    </div>
</template>

<script>
import { axios } from '@/common/api.service.js';
import { useReplyMsgUuid } from '../stores/store'
export default {
    name: 'SendMessageComponent',
    data() {
        return {
            search: '',
            selectedOption: '',
            profile: '',
            optionsVisibility: false,
            profiles: [],
            reciever_profile: '',
            message_text: '',
            title_text: '',
            reply: useReplyMsgUuid()
        }
    },
    methods: {
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

        async sendMessage(){
            let endpoint = `/api/v1/txtmsg/create/${this.reciever_profile.uuid}/`
            try {
                const response = await axios.post(endpoint, {
                    text: this.message_text,
                    title: this.title_text,

                })
                console.log(response)

                // const response2 = await axios.post(endpoint, {
                //     text: this.message_text,
                //     title: this.title_text,
                //     owner: this.reciever_profile.id
                // })
                // console.log(response2)

                this.$refs.msgform.reset()
                this.$emit('newMsg', response.data)
            } catch(error){
                this.$notify({
                    title: 'invalid form',
                    text: 'Choose player name from the list below',
                    duration: 4000,
                    type: 'error',
                });
                console.log(error)
            }
        },

        // filterOptions() {
        //     this.filteredOptions = this.options.filter(option => {
        //         return option.toLowerCase().includes(this.search.toLowerCase());
        //     });
        // },

        setSearchModel() {
            this.reciever_profile = this.selectedOption
            this.search = this.selectedOption.name
            this.optionsVisibility = false
            console.log(this.reciever_profile)
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
                this.reciever_profile = response.data



            } catch (error){
                console.log(error)
            }
        },

    },
    created() {
        this.getProfilesData()

        console.log(this.reply.title)

        if (this.reply.uuid) {
            this.getReplyToObject(this.reply.uuid)
            this.title_text = `Re: ${this.reply.title}`
        }
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
  background: linear-gradient(#212121, #212121) padding-box,
              linear-gradient(145deg, transparent 35%,rgb(0, 161, 193), #40c9ff) border-box;
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
  color: rgb(0, 161, 193);
  font-weight: 600;
  font-size: 12px;
}

.form-container .form-group input {
  width: 100%;
  padding: 12px 16px;
  border-radius: 8px;
  color: #fff;
  font-family: inherit;
  background-color: transparent;
  border: 1px solid #414141;
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
  color: rgb(0, 161, 193);
  font-weight: 600;
  width: 40%;
  background: #313131;
  border: 1px solid #414141;
  padding: 12px 16px;
  font-size: inherit;
  gap: 8px;
  margin-top: 8px;
  cursor: pointer;
  border-radius: 6px;
}

/* .form-container .form-submit-btn:hover {
  background-color: #fff;
  border-color: #fff;
} */




</style>