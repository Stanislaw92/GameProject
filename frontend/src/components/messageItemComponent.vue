<template>

  <div class="itemContainer">
        
        <div style="width: 15%; height: 100%;">
            <div class="checkbox_icon_cont">
                <label class="container">
                    <input type="checkbox">
                    <svg viewBox="0 0 64 64" height="1.2em" width="1.2em">
                        <path d="M 0 16 V 56 A 8 8 90 00 8 64 H 56 A 8 8 90 0 0 64 56 V 8 A 8 8 90 0 0 56 0 H 8 A 8 8 90 0 0 0 8 V 16 L 32 48 L 64 16 V 8 A 8 8 90 0 0 56 0 H 8 A 8 8 90 0 0 0 8 V 56 A 8 8 90 0 0 8 64 H 56 A 8 8 90 0 0 64 56 V 16" pathLength="575.0541381835938" class="path"></path>
                    </svg>
                </label>
                <img :src=icon_src>
            </div>


        </div>
    <router-link
        v-if="message.title"
        style="width: 60%;" 
        class="name"
        :class="[ isNew && page=='inbox'? 'bold_style': 'pass']"
         :to="{name: 'MessageDetalView', params: {uuid: `${this.message.uuid}`, type: 1}}"
    >
        {{message.title}}
    </router-link>
    <router-link
        v-else-if="message.loot"
        style="width: 60%;" 
        class="name"
        :class="[ isNew && page=='inbox'? 'bold_style': 'pass']"
         :to="{name: 'MessageDetalView', params: {uuid: `${this.message.uuid}`, type: 2}}"
    >
        Trip raport
    </router-link>
    <router-link
        v-else-if="message.attacker"
        style="width: 60%;" 
        class="name"
        :class="[ isNew && page=='inbox'? 'bold_style': 'pass']"
         :to="{name: 'MessageDetalView', params: {uuid: `${this.message.uuid}`, type: 3}}"
    >
        <p v-if="!defense_raport">you set up an ambush for {{message.victim}}</p>
        <p v-else>{{message.attacker}} attacked you</p>
    </router-link>
    <router-link  
        v-if="page=='inbox' && !isRaport"
        class="name"
        style="width: 10%;"
        :to="{name: 'ProfileView', params: {uuid: `${this.message.sender_uuid}`}}"
    >
        {{message.sender}}
    </router-link >
    <div
        v-else-if="page=='inbox' && isRaport"
        class="name raport"
        style="width: 10%;"
    >
        -
    </div >
    <router-link  
        v-else-if="page=='outbox'"
        class="name"
        style="width: 10%;"
        :to="{name: 'ProfileView', params: {uuid: `${this.message.reciever_uuid}`}}"
    >
        {{message.reciever}}
    </router-link >
    <router-link  
        v-else-if="page=='saved'"
        class="name"
        style="width: 10%;"
        :to="{name: 'ProfileView', params: {uuid: `${this.message.sender_uuid}`}}"
    >
        {{message.sender}}
    </router-link >
  </div>
</template>

<script>
export default {
    name: 'MessageItemComponent',
    props: ['message', 'page', 'profile'],
    data(){ 
        return {
            isNew: this.message.new,
            icon_src: "",
            defense_raport: false,
            isRaport: true
        }
    },
    created(){

        if (this.message.loot){
            this.icon_src = "../../../static/icons/gem.svg"

        } else if (this.message.attacker) {


            if (this.message.attacker == this.profile.name) {
                this.defense_raport = false
            } else {
                this.defense_raport = true
            }

            this.icon_src = "../../../static/icons/sword-fill.svg"
        } else if (this.message.title) {
            this.isRaport = false
            this.icon_src = "../../../static/icons/envelope.svg"
        }
        

        
    }
}
</script>

<style scoped> 
img {
    width: 50%;
    height: 50%;
}

p {
    margin: 0;
}

.itemContainer {
    display: flex;
    align-items: center;

    width: 95%;
    height: 50px;
    margin: 5px 0 5px 0;
    background-color: rgb(255, 255, 255);

    border-radius: 5px;
}

.buttons_container {
    width: 35%;
    padding: 5px;
    display: flex;
    justify-content:space-evenly;
}
.name {
    text-decoration: none;
    color: black;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
}

.name:hover {
    text-decoration: underline;
}
.raport {
    cursor: auto;
}

.raport:hover {
    text-decoration: none;
}

.message_container {
    /* margin: 5px; */
    padding: 5px;
    display: flex;
    /* justify-content: center; */
    align-items: center;
    justify-content: space-between;
    border-bottom: 0.5px rgba(0, 0, 0, 0.182) solid;
    background-color: rgba(240, 248, 255, 0);
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

.checkbox_icon_cont {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
}

.container {
    cursor: pointer;
}

.container input {
  display: none;
}

.container svg {
  overflow: visible;
}

.icon_container {
    width: 100%;
    height: 100%;
}



.path {
  fill: none;
  stroke: rgba(0, 0, 0, 0.67);
  stroke-width: 6;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: stroke-dasharray 0.5s ease, stroke-dashoffset 0.5s ease;
  stroke-dasharray: 241 9999999;
  stroke-dashoffset: 0;
}

.container input:checked ~ svg .path {
  stroke-dasharray: 70.5096664428711 9999999;
  stroke-dashoffset: -262.2723388671875;
}

.bold_style {
    font-weight: bold;
}
</style>