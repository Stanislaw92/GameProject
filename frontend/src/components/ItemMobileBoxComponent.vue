<template>
    <div class="mobileBoxContainer"
        v-if="!boxStore.item"
        :style="{ visibility: boxStore.visible}">
    </div>
    <div 
        v-else
        class="mobileBoxContainer"
        @mouseleave="turnOffBox"
        :style="{ visibility: boxStore.visible, top: boxStore.mouseCordY-50 +'px', left: boxStore.mouseCordX-50 +'px' }"
        >
        
        
        <div class="leftRowBox">
            <div class="itemImageBox">
                <img :src="boxStore.item.base.item_base_pic" alt="">
            </div>
            <div class="prefixesImageBox">
                <div 
                    class="leftPrefixesBox"
                >
                    <img :src="boxStore.item.prefix.prefix_pic" alt="">
                </div>
                <div class="rightPrefixesBox">
                    <img :src="boxStore.item.sufix.sufix_pic" alt="">
                </div>
            </div>
        </div>
        <div class="rightRowBox">
            <p class="titleP"> {{boxStore.item.name}}</p>
            <div>
                {{ boxStore.stats}}
                <!-- <span
                    v-for="stat in boxStore.item.item.overall_stats"
                    :key="stat"
    
                >
                    <p v-if="stat[0]=='dmg'">dmg: {{ stat[1] }} - {{ stat[2] }}</p>
                    <p v-else>{{ stat[0] }} : {{ stat[1] }}</p>
    
                </span> -->
            </div>
        </div>


    </div>
</template>

<script>
import { useArmoryBoxStore } from '@/stores/store.js'
export default {
    data() {
        return {
            boxStore: useArmoryBoxStore(),   
        }
    },
    methods: {
        test(){
            console.log(this.boxStore.item)
        },
        turnOffBox() {
            // if (this.boxStore.visible == 'visible'){
            this.boxStore.updateVisibility(false)
            // }
        },
    },
    created() {
    }


}
</script>

<style scoped>
    img {
        height: 100%;
        width: 100%;
    }

    p {
        margin-bottom: 0;
    }

    .mobileBoxContainer {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: row;
        width: 500px;
        height: 300px;
        border: 1px solid rgb(86, 86, 86);
        border-image: fill 0 linear-gradient(rgba(225, 225, 225, 0.2),#3000008f);
        border-radius: 10px;
        position: absolute;
        background: gray;
        z-index: 10;
    }

    .leftRowBox, .rightRowBox {
        height: 100%;
    }

    .leftRowBox {
        width: 40%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .itemImageBox {
        width: 100%;
        /* height: 170px; */
    }

    .prefixesImageBox {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        /* height: 80px; */
    }

    .leftPrefixesBox {
        width: 100%;
        height: 100%;
    }

    .rightPrefixesBox {
        width: 100%;
        height: 100%;

    }

    .rightRowBox {
        padding: 10px;
        width: 60%;
        display: flex;
        justify-content:flex-start;
        align-items: center;
        flex-direction: column;
        overflow: visible;
    }


    .titleP {
        margin: 5px;
        font-family: "Sriracha", cursive;
        font-weight: 600;
    }
</style>