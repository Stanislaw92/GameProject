<template>
    <div 
        v-if="!loading"
        class="component_container">
        <div class="boxes_container">
            <div
                :class="{'boxActive': page=='inbox'}"
                @click="changePage('inbox')"
            >
                inbox
            </div>
            <div
                @click="changePage('outbox')"
                :class="{'boxActive': page == 'outbox'}"
            >
                outbox
            </div>
            <div
                @click="changePage('saved')"
                :class="{'boxActive': page == 'saved'}"
            >
                saved
            </div>
            <div
                @click="changePage('send')"
                :class="{'boxActive': page == 'send'}"
            >
                send message
            </div>
        </div>
        <ContainerComponent 
            style="width: 100%"
            v-if="page == 'inbox'"
        >
            <div class="listDescribe_container">
                <div style="width: 15%;"></div>
                <div style="width: 60%;">title</div>
                <div style="width: 10%;">author</div>
            </div>
            <MessageItemComponent 
                
                v-for="message in sortedMsgs"
                :message='message'
                :key="message"
                :page="page"
                :profile="profile"
            />
        </ContainerComponent>
        <ContainerComponent 
            style="width: 100%"
            v-else-if ="page=='outbox'"
        >
            <div class="listDescribe_container">
                <div style="width: 15%;"></div>
                <div style="width: 60%;">title</div>
                <div style="width: 10%;">reciever</div>
            </div>
            <MessageItemComponent 
                v-for="message in outboxMessages"
                :message='message'
                :key="message"
                :page="page"
            />
        </ContainerComponent>
        <ContainerComponent 
            style="width: 100%"
            v-else-if ="page=='saved'"
        >
            <div class="listDescribe_container">
                <div style="width: 15%;"></div>
                <div style="width: 60%;">title</div>
                <div style="width: 10%;">author</div>
            </div>
            <MessageItemComponent 
                v-for="message in savedMessages"
                :message='message'
                :key="message"
                :page="page"
            />
        </ContainerComponent>
        <ContainerComponent
            v-else-if="page=='send'"
            class="send_container"
        >
            <SendMessageComponent 
                @newMsg="newMsg"
            />   
        </ContainerComponent>

    </div>
    <div v-else>
        <div class="lds-spinner"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    </div>
</template>

<script>
import { axios } from '@/common/api.service.js';
import { useReplyMsgUuid } from '../stores/store'
import MessageItemComponent from './messageItemComponent.vue'
import SendMessageComponent from './SendMessageComponent.vue'
import ContainerComponent from './containerComponent.vue'
export default {
    name: 'MessageListComponent',
    components: {
        MessageItemComponent,
        SendMessageComponent,
        ContainerComponent
    },
    data() {
        return {
            loading: true,
            inboxMessages: [],
            outboxMessages: [],
            savedMessages: [],
            page: 'inbox',
            reply: useReplyMsgUuid(),
            profile: null
        }
    },
    methods: {
        async getProfileData() {
            let endpoint = '/api/v1/profiles/'
            try {
                const response = await axios.get(endpoint)
                this.profile = response.data[0]
                console.log(this.profile)
            } catch (error) {
                        console.log(error.response);
                        alert(error.response.statusText);
            }
            },
        changePage(pageName) {
            this.page = pageName
            this.reply.updateUuid(null)
        },
        async getTripRaports(){
            const endpoint = "/api/v1/trip_results/"
                try {
                    const response = await axios.get(endpoint)
                    this.inboxMessages.push(...response.data)
                    console.log(this.inboxMessages)
                } catch (error) {
                    console.log(error.response)
                }
        },
        async getCombatRaports(){
            const endpoint = "/api/v1/combat_result/"
                try {
                    const response = await axios.get(endpoint)
                    this.inboxMessages.push(...response.data)
                    console.log(this.inboxMessages)
                } catch (error) {
                    console.log(error.response)
                }
        },
        async getInboxList(){
            const endpoint = "/api/v1/txtmsg/inbox/"
            try {
                const response = await axios.get(endpoint)
                this.inboxMessages.push(...response.data)
                console.log(this.inboxMessages)
            } catch (error) {
                console.log(error.response)
            }
        },
        async getOutboxList(){
            this.outboxMessages = []
            const endpoint = "/api/v1/txtmsg/outbox/"
            try {
                const response = await axios.get(endpoint)
                this.outboxMessages.push(...response.data)
                console.log(this.outboxMessages)
            } catch (error) {
                console.log(error.response)
            }

        },
        async getSavedList(){
            const endpoint = "/api/v1/txtmsg/saved/"
            try {
                const response = await axios.get(endpoint)
                this.savedMessages.push(...response.data)
            } catch (error) {
                console.log(error.response)
            }``
        },
        newMsg(msgObj) {
            this.page = 'inbox'
            console.log(msgObj)
            this.outboxMessages.push(msgObj)
            this.newNotification('success', 'success!','You have successfully send your message!')
        },

        newNotification(type, title, text){
            this.$notify({
                title: title,
                text: text,
                duration: 4000,
                type: type,
            });
        },
        sortMsgs() {
            this.inboxMessages.slice().sort((a,b) => {
                return new Date(b.created_at) - new Date(a.created_at)
            })
        },
        getRaports() {
            this.getInboxList()
            this.getTripRaports()
            this.getCombatRaports()
        },
        getAllMessages(){

            this.getRaports()
            this.getOutboxList()
            this.getSavedList()
            this.sortMsgs()

            this.loading = false
        },

    },
    computed: {
        sortedMsgs: function() {        
            return this.inboxMessages.slice().sort((a,b) => {
                return new Date(b.created_at) - new Date(a.created_at)
            })
        }
    },
    created() {
        this.getAllMessages()
        this.getProfileData()

        if (this.reply.uuid){
            this.page = 'send'
            // this.getReplyToObject(this.reply.uuid)
        }
    }
}
</script>

<style scoped> 
.component_container{
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.boxes_container {
    width: 40%;
    display: flex;
    justify-content: space-around;
    align-items: center;
    font-size: 15px;
    cursor: pointer;
}

.boxActive {
    font-weight: bold;
    font-size: 18px;
    color: rgb(0, 161, 193);
}

/* .message_list_container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width: 100%;
    background-color: rgb(238, 238, 238);
    padding: 10px 0px 10px 0px;
    margin-top: 20px;
    border-radius: 5px;
} */

.send_container {
    width: 450px;
}


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




.column_names_container {
    /* margin: 5px; */
    padding: 5px;
    display: flex;
    /* justify-content: center; */
    align-items: center;
    justify-content: space-between;
    border-bottom: 0.5px rgba(0, 0, 0, 0.182) solid;
    background-color: azure;
    border-radius: 10px;
    padding: 5px;
    width: 100%;
    height: 40px;
}

.box1 {
    width: 40%;
}
.box2 {
    width: 20%;
}
.box3 {
    width: 15%;
}

.check_box {
    width: 15%;
}

.lds-spinner {
  color: official;
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-spinner div {
  transform-origin: 40px 40px;
  animation: lds-spinner 1.2s linear infinite;
}
.lds-spinner div:after {
  content: " ";
  display: block;
  position: absolute;
  top: 3px;
  left: 37px;
  width: 6px;
  height: 18px;
  border-radius: 20%;
  background: rgb(0, 0, 0);
}
.lds-spinner div:nth-child(1) {
  transform: rotate(0deg);
  animation-delay: -1.1s;
}
.lds-spinner div:nth-child(2) {
  transform: rotate(30deg);
  animation-delay: -1s;
}
.lds-spinner div:nth-child(3) {
  transform: rotate(60deg);
  animation-delay: -0.9s;
}
.lds-spinner div:nth-child(4) {
  transform: rotate(90deg);
  animation-delay: -0.8s;
}
.lds-spinner div:nth-child(5) {
  transform: rotate(120deg);
  animation-delay: -0.7s;
}
.lds-spinner div:nth-child(6) {
  transform: rotate(150deg);
  animation-delay: -0.6s;
}
.lds-spinner div:nth-child(7) {
  transform: rotate(180deg);
  animation-delay: -0.5s;
}
.lds-spinner div:nth-child(8) {
  transform: rotate(210deg);
  animation-delay: -0.4s;
}
.lds-spinner div:nth-child(9) {
  transform: rotate(240deg);
  animation-delay: -0.3s;
}
.lds-spinner div:nth-child(10) {
  transform: rotate(270deg);
  animation-delay: -0.2s;
}
.lds-spinner div:nth-child(11) {
  transform: rotate(300deg);
  animation-delay: -0.1s;
}
.lds-spinner div:nth-child(12) {
  transform: rotate(330deg);
  animation-delay: 0s;
}
@keyframes lds-spinner {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
</style>