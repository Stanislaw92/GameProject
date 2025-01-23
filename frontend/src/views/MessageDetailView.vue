<template>

        <div 
            class="message_container"
        >
            <MessageTitleContainerComponent 
                :type="type"
                :incoming=checkIfIncoming
                :message="message"
            />
            <div class="textContainer">
                    <div 
                        v-if="type==1"
                        class="wrap-it">
                        {{message.text}}
                    </div>
                    <TripMsgComponent 
                        v-if="type==2"
                        :message = "message"
                    >
                    </TripMsgComponent>
                    <Combat1v1Component 
                        v-if="type==3 && dataLoaded"
                        :message = "message"
                        :testArr = 'testArr'
                        :attacker = 'attacker'
                        :victim = "victim"
                    />
            </div>
            <div class="buttons_class">
                <ButtonComponent 
                    v-if="profile.name != message.sender && !message.saved && !israport" @click="answerMsg"
                    :style_of_button = 'style_of_button'
                >answer</ButtonComponent>
                <ButtonComponent v-if="!message.saved && message.sender != profile.name" @click="saveMsg" :style_of_button = 'style_of_button'>save</ButtonComponent>
                <ButtonComponent 
                    v-if="type==1"
                    @click="deleteMessage('txtmsg')"
                    :style_of_button = 'style_of_button'
                >delete</ButtonComponent>
                <ButtonComponent v-if="type==2" @click="deleteMessage('trip_results')" :style_of_button = 'style_of_button'>delete</ButtonComponent>
                <ButtonComponent v-if="type==3" @click="deleteMessage('combat_result')" :style_of_button = 'style_of_button'>delete</ButtonComponent>
            </div>
        </div>
</template>

<script>
import ButtonComponent from '../components/ButtonComponent.vue'
import MessageTitleContainerComponent from '../components/MessageTitleContainerComponent.vue'
import TripMsgComponent from '../components/TripMsgComponent.vue'
import Combat1v1Component from '../components/Combat1v1Component'
import { useLoggedInProfile } from '@/stores/store.js'
import { useReplyMsgUuid } from '../stores/store'
import { axios } from '@/common/api.service.js';

export default {
    name: 'MessageDetalView',
    props: ['uuid','type'],
    data() {
        return {
            message: '',
            profile: '',
            israport: true,
            text: '',
            test: '',
            testArr: [],
            sender: '',
            reiever: '',
            attacker: null,
            victim: null,
            str_array_loaded: false,
            profiles_loaded: false,
            style_of_button: 'primary'
        }
    },
    components: {
        Combat1v1Component,
        MessageTitleContainerComponent,
        ButtonComponent,
        TripMsgComponent
    },
    methods: {
        async getProfileData() {
            let endpoint = '/api/v1/profiles/'
            try {
                const response = await axios.get(endpoint)
                this.profile = response.data[0]
                console.log(this.profile)
                const store = useLoggedInProfile()
                store.updateProfile(this.profile)

            } catch (error) {
                    console.log(error);
            }
        },
        async getMessage() {
            const endpoint = `/api/v1/txtmsg/${this.uuid}/`
            try {
                const response = await axios.get(endpoint)
                this.message = response.data
                this.sender = String(this.message.sender)
                this.reciever = String(this.message.reciever)

                if ( this.message.new ){
                    this.markAsRed('txtmsg')
                }
                if (this.message.sender == this.profile.name) {
                    this.isSender = true
                } else if ( this.message.reciever == this.profile.name ){
                    this.isReciever = true

                this.israport = false
        }
            } catch (error){
                console.log(error)
            }
        },
        async getTripRaport(){
            const endpoint = `/api/v1/trip_results/${this.uuid}/`
                try {
                    const response = await axios.get(endpoint)
                    this.message = response.data
                    console.log(this.message)
                    if ( this.message.new ){
                        this.markAsRed('trip_results')
                    }
                } catch (error){
                    console.log(error)
                }
        },
        async get1v1Raport(){
            const endpoint = `/api/v1/combat_result/${this.uuid}/`
                try {
                    const response = await axios.get(endpoint)
                    this.message = response.data


                    if ( this.message.new ){
                        this.markAsRed('combat_result')
                    }

                    this.updateMessageArray()
                    this.getPlayersProfiles()

                    

                } catch (error){
                    console.log(error)
                }
        },
        async getPlayersProfiles(){
            
            const logged_in_profile = useLoggedInProfile().profile
            
            if (logged_in_profile.name == this.message.attacker) {
                this.attacker = logged_in_profile
                console.log(this.message.victim_uuid)
                let endpoint = `/api/v1/profiles/${this.message.victim_uuid}/`
                try {
                    const response = await axios.get(endpoint)
                    this.victim = response.data
                    console.log(this.victim)
                    this.profiles_loaded = true
                } catch (error) {
                        console.log(error);
                }

            } else {
                this.victim = logged_in_profile
                let endpoint = `/api/v1/profiles/${this.message.attacker_uuid}/`
                try {
                    const response = await axios.get(endpoint)
                    this.attacker = response.data
                    console.log(this.attacker)
                    this.profiles_loaded = true


                } catch (error) {
                        console.log(error);
                }
            }
        },
        async markAsRed(typeOfMessage) {
            const endpoint = `/api/v1/${typeOfMessage}/${this.uuid}/`
            try {
                if (this.type==1){
                    const response = await axios.put(endpoint, {
                        new: false,
                        text: this.message.text,
                        title: this.message.title,
                    })
                    this.message = response.data
                } else if (this.type==2){
                    const response = await axios.put(endpoint, {
                        new: false,
                    })
                    this.message = response.data
                } else if (this.type == 3){
                    const response = await axios.put(endpoint, {
                        new: false,
                    })
                    this.message = response.data
                }
                
                
            } catch (error){
                console.log(error)
            }
        },
        async deleteMessage(typeOfMessage) {

            const endpoint = `/api/v1/${typeOfMessage}/${this.uuid}/`

            try {
                if (this.type==1){

                    if (this.message.sender == this.profile.name) {
                        const response = await axios.put(endpoint, {
                            text: this.message.text,
                            title: this.message.title,
                            deleted_sender: true
                        })
                        console.log(response.data)
                    } else {
                        const response = await axios.put(endpoint, {
                            text: this.message.text,
                            title: this.message.title,
                            deleted_reciever: true
                        })
                        console.log(response.data)
                    }

                } else if (this.type==2){
                    await axios.delete(endpoint)

                } else if (this.type == 3){

                    if (this.message.sender == this.profile.name) {
                        const response = await axios.put(endpoint, {
                            deleted_sender: true
                        })
                        console.log(response.data)
                    } else {
                        const response = await axios.put(endpoint, {
                            deleted_reciever: true
                        })
                        console.log(response.data)
                    }
                }
                
                

                
                this.$router.push({name: 'MessagesView'})
            } catch (error){
                console.log(error)
            }
        },
        async saveMsg() {
            let endpoint = ``
            if ( this.type == 1) {
                endpoint = `/api/v1/txtmsg/${this.uuid}/`
            } else if ( this.type == 2) {
                endpoint = `/api/v1/trip_results/${this.uuid}/`
            } else { 
                endpoint = `/api/v1/combat_result/${this.uuid}/`
            }

            try { 
                await axios.put(endpoint, {
                    saved: true,
                    text: this.message.text,
                    title: this.message.title,
                    owner: this.message.owner,
                    new: this.message.new
                })

                this.$router.push('/messages/')

            } catch (error){
                console.log(error)
            }
        },
        answerMsg() {
            const store = useReplyMsgUuid()
            store.updateUuid(`${this.message.sender_uuid}`)
            store.updateTitle(`${this.message.title}`)
            
            // this.$router.push({name: 'MessagesView', params: {replyTo: this.message.sender_uuid}} )
            this.$router.push('/messages/')
        },
        updateMessageArray() {

            this.test = this.message.result.slice(0,-1).replace(/'/g, "").replace('[',' ')
            this.testArr = this.test.split( 'end of round,')
            // this.testArr = this.test.split()
            // this.testArr = this.test.split(',')
            console.log(this.testArr)
            this.str_array_loaded = true
        },
    },
    computed: {
        dataLoaded() {
            if (this.str_array_loaded && this.profiles_loaded){
                return true
            } else {
                return false
            }
        },
        checkIfIncoming() {
            if (this.type ==1 && this.message.reciever == this.profile.name){
                return 1
            } else if (this.type ==1 && this.message.reciever != this.profile.name) {
                return 0
            } else if (this.type != 1) {
                return 2
            } else {
                return 3
            }
        }
    
    },
    created() {

        this.getProfileData()
        if (this.type == 1){
            this.getMessage()
        } else if ( this.type == 2){
            this.getTripRaport()
            this.israport = true
        } else if (this.type==3){
            this.get1v1Raport()
            this.style_of_button = 'combat1v1'
            this.israport = true
        }

        if (this.message.title) {
            this.israport = false
        }

    }
}
</script>

<style scoped>



.buttons_class {
    width: 40%;
    display: flex;
    justify-content: space-around;
    align-items: center;

}


.message_container {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    flex-direction: column;
    width: 80%;
    background-color: rgb(238, 238, 238);
    padding: 10px 0px 10px 0px;
    margin: 3% 10%;
    border-radius: 5px;
    height: max-content;
}

/* .content_container {
    display: flex;
    align-items: center;
    flex-direction: column;

    width: 95%;
    margin: 5px 0 5px 0;
    background-color: rgba(31, 31, 31, 0.819);

    border-radius: 5px;
    color: rgb(223, 223, 223);
} */

.textContainer {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-direction: column;

    padding: 30px 20px 30px 20px;
    width: 95%;
    margin: 5px 0 5px 0;
    background-color: rgb(255, 255, 255);
    border-radius: 5px;

    
    
   
}
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

.round_container {
    width: 100%;
}

.horizontal_line {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 80%;
    height: 50px;
    margin-top:20px ;
    margin-bottom:20px ;
    background: radial-gradient(circle, rgba(73,0,0,0.5) 0%, rgba(255,255,255,1) 100%);
}


.center_class {
    padding: 10px 20px 0 20px;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-direction: column;
}

.active_name {
    font-weight: bold;
    color: rgb(139, 139, 249);
}

.msg_title {
    align-self: center;
}



</style>