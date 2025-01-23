<template>
		
    <p
        v-if="item !=0"
    >   
        <span
            @click="updateItemInStore"
            class="name_text"
        >
            {{ item.name }}
        </span>
    </p>
    <p v-else class="name_text">
        EMPTY
    </p>
    

</template>

<script>


import { useArmoryBoxStore } from '@/stores/store.js'
export default {
    name: 'ItemNameComponent',
    props: ['item'],
    data(){
        return {
            
        }
    },
    methods: {
        updateItemInStore(event){
			const x = useArmoryBoxStore()
			x.updateVisibility(true)
			x.updateMouseCord(event.pageX, event.pageY)
			x.updateItem(this.item)
			
		},
    },
    created() {
    }
    
}
</script>

<style scoped>
.name_text {
    cursor: pointer;
    font-weight: 600;
}

.name_text:hover {
    color: rgb(0, 87, 13);
}
</style>