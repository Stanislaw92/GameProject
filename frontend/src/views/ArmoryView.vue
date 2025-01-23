<template>
    <div 
        class="container" 
        >
        <!-- @click="checkElement" -->
        <ItemMobileBoxComponent/>
        <div class="buttons_container">
            <button @click="equip_unequip_items(equip=true)">Equip</button>
            <button @click="equip_unequip_items(equip=false)">UnEquip</button>
        </div>
        <div class="itemsList">
            <div v-if="loadingData">
                <div v-for="index in 7" :key="index" class="loader">
                    <div class="wrapper">
                        <div class="line-3"></div>
                    </div>
                </div>
            </div>
            <div v-else class="armory_items_equipped">
                <div class="buttons">
                    <button class="checkBtns" @click="checkAll('true')"><i class="fa-solid fa-check-double fa-xl"></i></button>
                    <button class="checkBtns" @click="unCheckAll('true')"><i class="fa-solid fa-circle-xmark fa-xl"></i></button>
                    <button class="checkBtns" @click="swapCheckes('true')"><i class="fa-solid fa-arrows-rotate fa-xl"></i></button>
                </div>
                <div class="equipped_items">
                    <div class="armory_equipped_rows"
                            v-for="item in equippedItems"
                            :item="item"
                            :key="item"
                    >
                        <div class="slot_name_class">
                            {{ item.slotName }}
                        </div>
                        <ItemComponent
                            :item="item"
                            :key="item"
                            :checked = "item.checked"
                            class="container_items"
                            @addToUnEquipList ="addToUnEquipList"
                            :equipped ="true"
                        />
                    </div>
                
                </div>
            </div>
            <div v-if="loadingData">
                <div v-for="index in 7" :key="index" class="loader">
                    <div class="wrapper">
                        <div class="line-3"></div>
                    </div>
                </div>
            </div>
            <div v-else
                class="armory_items_unequipped" >
                <div class="buttons">
                    <button class="checkBtns" @click="checkAll('false')"><i class="fa-solid fa-check-double fa-xl"></i></button>
                    <button class="checkBtns" @click="unCheckAll('false')"><i class="fa-solid fa-circle-xmark fa-xl"></i></button>
                    <button class="checkBtns" @click="swapCheckes('false')"><i class="fa-solid fa-arrows-rotate fa-xl"></i></button>
                </div>
                <ItemComponent 
                    class="container_items"
                    v-for="item in unEquippedItems" 
                    :key="item"
                    :item = "item"
                    :checked = "item.checked"
                    @refreshItems = "refreshItems"
                    @addToEquipList = 'addToEquipList'
                    :equipped = 'false'
                > </ItemComponent>
            </div>
            <!-- <div v-else class="unEquipped">
                There is none unequipped items
            </div> -->
        </div>





    </div>
</template>

<script>
import ItemMobileBoxComponent from '../components/ItemMobileBoxComponent.vue';
import { axios } from '@/common/api.service.js';
import ItemComponent from '../components/itemComponent.vue';
import { useArmoryBoxStore } from '@/stores/store.js'

export default {
    name: 'ArmoryView',
    emits: 
        ['addToEquipList', 'addToUnEquipList']
    ,
    data() {
        return {
            loadingData: true,
            equippedItems: 
            [
                {
                    item: 0,
					checked: false,
                    slotName: 'Mainhand'
				},
                {
                    item: 0,
					checked: false,
                    slotName: 'Offhand'
				},
                {
                    item: 0,
					checked: false,
                    slotName: 'Ring 1'
				},
				{
                    item: 0,
					checked: false,
                    slotName: 'Chest'
				},
				{
                    item: 0,
					checked: false,
                    slotName: 'Legs'
				},
				{
                    item: 0,
					checked: false,
                    slotName: 'Ring 2'
				},
				{
                    item: 0,
					checked: false,
                    slotName: 'Necklacle'
				},
				{
                    item: 0,
					checked: false,
                    slotName: 'Head'
				},
				{
                    item: 0,
					checked: false,
                    slotName: 'Shoes'
				},
            ],
            profile: [],
            items: [],
            checkedItems: [],
            unEquippedItems: [],
            itemsToUnEquip: [],

        }
    },
    components: {
        ItemComponent,
        ItemMobileBoxComponent
    },
    methods: {
        checkElement(event){
            if (!event.target.classList.contains("mobileBoxContainer")) {
                console.log('dont have that class')  
                const x = useArmoryBoxStore()
                console.log(x.visible)
                // if (x.visible == "visible") {
                //     x.updateVisibility(false)
                // }
            }
        },
        async getItemsData() {
            this.loadingData = true
            let endpoint = '/api/v1/items/'
            let endpoint1 = '/api/v1/eqippedItems/'
            let endpoint2 = '/api/v1/unEqippedItems/'
            // try {
                this.items = []
                const response = await axios.get(endpoint)
                this.items.push(...response.data)

                const response1 = await axios.get(endpoint1)
                // response1.data.forEach((el)=>{
                //     this.equippedItems[el.itemType-1].item = el
                // })
  

                this.unEquippedItems = []
                const response2 = await axios.get(endpoint2)
                
                let arrayForLoop = []

                arrayForLoop.push(...response2.data)
                arrayForLoop.forEach((el)=>{
                    this.unEquippedItems.push({
                        item: el, 
                        checked: false
                    }) 
                })

                arrayForLoop = []
                arrayForLoop.push(...response1.data)
                arrayForLoop.forEach((el)=>{
                    if(el.itemType == 1) {
                        if ( this.equippedItems[0].item == 0 ) {
                            this.equippedItems[0].item = el
                        } else if (this.equippedItems[1].item == 0 ) {
                            this.equippedItems[1].item = el
                        }
                    } else {
                        this.equippedItems[el.itemType].item = el
                    }
                })

                console.log('equippedItems', this.equippedItems)
                // this.unEquippedItems.push(...response2.data)

                this.equippedItems.forEach((el)=>{
                    el.checked = false
                })
                console.log('unEquippedItems', this.unEquippedItems)
                this.loadingData = false

        },
        refreshItems() {
            this.getItemsData()
        },
        addToUnEquipList(item) {
            if (this.itemsToUnEquip.includes(item.item)) {
                this.itemsToUnEquip.splice(this.itemsToUnEquip.indexOf(item), 1)
                this.equippedItems[item.item.itemType-1].checked = false
            } else {
                this.itemsToUnEquip.push(item.item)
                
                this.equippedItems[item.item.itemType-1].checked = true
            }
            console.log(this.itemsToUnEquip)
        },
        addToEquipList(item){
            console.log(item)
                            
            this.unEquippedItems.forEach((el)=>{
                if ( el.item.uuid == item.item.uuid ){
                    el.checked = !el.checked
                }
            })

            if (this.checkedItems.includes(item.item)) {
                this.checkedItems.splice(this.checkedItems.indexOf(item.item), 1)
                console.log(this.checkedItems)
            } else { 
                this.checkedItems.push(item.item)
                console.log(this.checkedItems)
            }
        },


        async equip_unequip_items(equip){
            let uuids_list = []
            let listForDoubles = {
                '1': 0,
                '2': 0,
                '3': 0,
                '4': 0,
                '5': 0,
                '6': 0,
                '7': 0,
                '8': 0,
                '9': 0
            }
            let data = {
                'equipped' : equip,
                'uuids': uuids_list
            }
            if (equip){
                console.log(this.checkedItems)
                console.log(this.equippedItems)
                this.checkedItems.forEach((el)=>{
                    console.log(this.equippedItems)

                    if ( el.itemType - 1 == 1) {

                        if ( this.equippedItems[0] == 0 ) {

                            if ( listForDoubles['1'] == 0) {
                                listForDoubles['1'] = el.uuid
                            } else if ( listForDoubles['1'] != 0 && listForDoubles['2'] == 0) {
                                listForDoubles['2'] == el.uuid
                            } else {
                                console.log('both places taken')
                            }

                        } else if (this.equippedItems[1] == 0 && this.equippedItems[0] != 0) {

                            if ( listForDoubles['2'] == 0) {
                                listForDoubles['2'] = el.uuid
                            } else {
                                console.log('both places taken')
                            }
                        } else {
                            this.$notify({
                                title: "Armory alert",
                                text: `You have already equipped slot no 1 and 2`,
                                duration: 2000,
                                type: 'warn'
                            });
                        }

                    } else {
                        if ( this.equippedItems[el.itemType-1].item == 0){
                            if (listForDoubles[`${el.itemType}`] == 0 ) {
                                console.log('true')
                                listForDoubles[`${el.itemType}`] = el.uuid
                            }
                        } else {
                            this.$notify({
                                title: "Armory alert",
                                text: `You have already equipped slot no ${el.itemType}`,
                                duration: 2000,
                                type: 'warn'
                            });
                        }
                    }

                })
                console.log(listForDoubles)

                for (const [key, value] of Object.entries(listForDoubles)) {
                    if ( value != 0 ) {
                        console.log(key)
                        uuids_list.push(value)
                    }
                }

                if (uuids_list.length > 0){
                    try {      
                        console.log(data)
                        const endpoint = '/api/v1/items_update/'
                        await axios.put(endpoint, data)
                        this.checkedItems = []
                        this.getItemsData()
                    } catch(error){
                        console.log(error)
                    }
                } else if (uuids_list.length==0 && this.checkedItems.length==0){
                        this.$notify({
                            title: "Armory alert",
                            text: "Choose atleasts 1 item",
                            duration: 2000,
                            type: 'warn'
                        });
                }

            } else {
                console.log(this.itemsToUnEquip)
                this.itemsToUnEquip.forEach((el)=>{
                    uuids_list.push(el.uuid)
                })
                
                if (uuids_list.length > 0){
                    try {      
                        const endpoint = '/api/v1/items_update/'
                        const result = await axios.put(endpoint, data)
                        console.log(result)
                        this.getItemsData()
                        result.data.forEach((el)=>{
                            this.equippedItems[el.itemType-1].item=0
                        })
                        this.itemsToUnEquip = []
                        this.equippedItems.forEach((el)=>{
                            el.checked = false
                        })
                        this.checkedItems = []
                    } catch(error){
                        console.log(error)
                    }
                } else {
                        this.$notify({
                            title: "Armory alert",
                            text: "Choose atleasts 1 item",
                            duration: 2000,
                            type: 'warn'
                        });
                }
            }

        },
        checkAll(equipped){

            if (equipped == 'true'){
                console.log(this.equippedItems)
                this.equippedItems.forEach((el)=>{
                    if (el.item != 0) {
                        el.checked = true
                        this.itemsToUnEquip.push(el.item)
                    }
                })

            } else {
                this.checkedItems = []
                this.unEquippedItems.forEach((el)=>{
                    el.checked = true
                    this.checkedItems.push(el.item)
                })
                console.log(this.checkedItems)
            }
        },

        unCheckAll(equipped){
            console.log(equipped)
            if (equipped == 'true'){
                this.equippedItems.forEach((el)=>{
                    el.checked = false
                })
                this.itemsToUnEquip = []
            } else {
                console.log('unequipped')
                this.unEquippedItems.forEach((el)=>{
                    el.checked = false
                })
                this.checkedItems = []
            }
        },
        swapCheckes(equipped){
            if (equipped == 'true'){
                this.itemsToUnEquip = []
                this.equippedItems.forEach((el)=>{
                    if ( el.item != 0){
                        el.checked = !el.checked
                        if (el.checked) {
                            this.itemsToUnEquip.push(el.item)
                        }
                    }
                })
                console.log(this.itemsToUnEquip)
            } else {
                this.checkedItems = []
                this.unEquippedItems.forEach((el)=>{
                    el.checked = !el.checked
                    if (el.checked) {
                        this.checkedItems.push(el.item)
                    }
                })
                console.log(this.checkedItems)
            }

        }
    },
    created() {
        this.getItemsData()
    }
}
</script>

<style scoped>
button {
    background: rgb(0, 161, 193);
    font-family: inherit;
    padding: 0.6em 1.3em;
    font-weight: 900;
    font-size: 18px;
    border: 3px solid black;
    border-radius: 0.4em;
    box-shadow: 0.1em 0.1em;
    margin: 10px;
}

button:hover {
  transform: translate(-0.05em, -0.05em);
  box-shadow: 0.15em 0.15em;
}

button:active {
  transform: translate(0.05em, 0.05em);
  box-shadow: 0.05em 0.05em;
}

.buttons {
    margin: 10px 0 10px 0;
}

.checkBtns {
    background: rgb(68, 194, 192);
    padding: 0.6em 0.8em;
    font-weight: 600;
    font-size: 12px;
    margin-bottom: 10px;
}

.container {
    display: flex;
    flex-direction: column;
    width: 90%;
    height: 90%;
    justify-content: space-around;
    align-items: center;
}
/* .container_items {
    border: 1px solid black;
    width: 100px;
    height: 20px;
    position: relative;
    margin-bottom: 10px;
} */

.itemsList {
    width: 100%;
    display: flex;
    justify-content: space-around;
    align-items: flex-start;
    flex-direction: row;
}

.checkMark {
    height: 100%;
    width: 20px;
    border: 1px solid rgba(0, 0, 0, 0.329);
    position: absolute;
    top: 0px;
    left: 0px;
    cursor: pointer;
}

.armory_items_equipped, .armory_items_unequipped {
    width: 30vw;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
}

.equipped_items {
    width: 100%;
    max-width: 400px;
}

.armory_equipped_rows {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}

.slot_name_class {
    border-bottom: 1px solid black;
    width: 35%;
    text-align: left;
    font-size: 90%;
    opacity: 60%;
}

.loader {
  position: relative;
  width: 100px;
  height: 20px;
  margin-bottom: 10px;
  border: 1px solid #00000000;
  /* padding: 15px; */
  background-color: #e3e3e3;
  overflow: hidden;
}

.loader:after {
  content: "";
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background: linear-gradient(110deg, rgba(227, 227, 227, 0) 0%, rgba(227, 227, 227, 0) 40%, rgba(227, 227, 227, 0.5) 50%, rgba(227, 227, 227, 0) 60%, rgba(227, 227, 227, 0) 100%);
  animation: gradient-animation_2 1.2s linear infinite;
}

.loader .wrapper {
  width: 100%;
  height: 100%;
  position: relative;
}

.loader .wrapper > div {
  background-color: #ffffff;
}

.loader .button {
  display: inline-block;
  height: 32px;
  width: 75px;
}


.loader .line-3 {
  position: absolute;
  top: 0px;
  left: 0px;
  height: 100%;
  width: 100%;
}

.buttons_container {
    width: 70%;
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-direction: row;
    margin-bottom: 10px;
}




@keyframes gradient-animation_2 {
  0% {
    transform: translateX(-100%);
  }

  100% {
    transform: translateX(100%);
  }
}
</style>