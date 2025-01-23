<template>
    <div 
         v-if="type!=1"
        class="msg_title_container"
    >
        Raport
    </div>
    
    <div
        v-else-if="type==1 && incoming==0" 
        class="msg_title_container"
    >
        <div class="headerObj">
            <div style="width: 15%; font-size:12px;"> sender: </div>
            <div style="width: 70%; font-weight: bold;">{{message.sender}}</div>
        </div>
        <div class="headerObj">
            <div style="width: 15%; font-size:12px;"> title: </div>
            <div style="width: 70%; font-weight: bold;"></div>
        </div>
    </div>

    <div
        v-else-if="type==1 && incoming==1" 
        class="msg_title_container"
    >
        <div class="headerObj">
            <div style="width: 15%; font-size:12px;"> reciever: </div>
            <div style="width: 70%; font-weight: bold;">{{message.reciever}}</div>
        </div>
        <div class="headerObj">
            <div style="width: 15%; font-size:12px;"> title: </div>
            <div style="width: 70%; font-weight: bold;">{{message.title}}</div>
        </div>
    </div>

</template>

<script>
export default {
    name: 'MessageTitleContainerCoponent',
    props: ['type', 'incoming', 'message'],
    created() {
    }
}
</script>

<style scoped>

.msg_title_container {
    display: flex;
    align-items: center;
    flex-direction: column;

    width: 95%;
    margin: 5px 0 5px 0;
    background-color: rgba(31, 31, 31, 0.819);

    border-radius: 5px;
    color: rgb(223, 223, 223);
}

.headerObj {
    margin: 7px 5px 7px 5px;
    width: 100%;
    display: flex;
    align-items: center;
}
</style>