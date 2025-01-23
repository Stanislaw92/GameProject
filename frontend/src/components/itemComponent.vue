<template>
	<div v-if="equipped">
		
		<div v-if="item.item != 0" class="itemContainer" :class="{item_component_clicked_bg : checked}">

			<ItemNameComponent :item="item.item" />
			<div class="checkMark" @click="checkUnCheck">
				<i v-if="checked" class="fa-solid fa-check" style="color: #27282a"> </i>
			</div>
		</div>
		<div v-else class="itemContainer">
			<span style="font-weight: 600;">empty</span>
			<div class=""></div>
		</div>

	</div>

	<div v-else>

		<div v-if="item.item != 0" class="itemContainer" :class="{item_component_clicked_bg:checked}">
			<ItemNameComponent :item="item.item" />

			<div class="checkMark" @click="checkUnCheck">
				<i v-if="checked" class="fa-solid fa-check" style="color: #27282a"> </i>
			</div>
		</div>
		<div v-else class="itemContainer">
			empty
			<div class=""></div>
		</div>

	</div>
</template>
l
<script>

import ItemNameComponent from './ItemNameComponent.vue';
// import { Icon } from '@iconify/vue';
// import { useArmoryBoxStore } from '@/stores/store.js'
// import { axios } from '@/common/api.service.js';
export default {
	name: 'ItemComponent',
	props: ['item', 'equipped', 'checked', 'slotName'],
	data() {
		return {
			clicked: this.checked,
			itemVar: null
		};
	},
	components: {
		// Icon,
		ItemNameComponent,
	},
	methods: {
		checkUnCheck() {
			if (this.equipped && this.item.item != 0) {
				this.$emit('addToUnEquipList', this.item);
			} else {
				this.$emit('addToEquipList', this.item);
			}
		},

		// updateItemInStore(event){
		// 	const x = useArmoryBoxStore()
		// 	x.updateVisibility(true)
		// 	x.updateMouseCord(event.pageX, event.pageY)
		// 	x.updateItem(this.item)	
		// },

		// clickItemName(event) {
		// 	const x = useArmoryBoxStore()
		// 	if (x.item) {
		// 		if (x.item != this.item) {
		// 			console.log('different item')
		// 			this.updateItemInStore(event, x)
		// 		} else {
		// 			console.log('same item')
		// 			x.updateVisibility(true)
		// 			x.updateMouseCord(event.pageX, event.pageY)
		// 		}
		// 	} else {
		// 		console.log('no item')
		// 		this.updateItemInStore(event, x)
		// 	}
		// }
	},
	created() {
	},
};
</script>

<style scoped>
img  {
	height: 100px;
	width: 100px;
}


.checkMark {
	height: 100%;
	width: 30px;
	border-left: 1px solid black;
	/* position: absolute; */
	top: 0px;
	border-radius: 2% 6% 5% 4% / 1% 1% 2% 4%;
	left: 80px;
	cursor: pointer;
	display: flex;
	justify-content: center;
	align-items: center;
	z-index: 1;
}



.itemContainer {
	width: 200px;
	height: 30px;
	margin: 5px 0 5px 0;
	font-family: 'Just Another Hand', cursive;
	padding-left: 10px;
    display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
    border: 1px solid #333333;
    font-size:12px;
    border-radius: 2% 6% 5% 4% / 1% 1% 2% 4%;
    text-transform: uppercase;
    letter-spacing: 0.01ch;
    position: relative;
}

.itemContainer p {
	text-align: center;
	margin: 0;
	cursor: pointer;
	z-index: 1;
}

.item_component_clicked_bg {
	background: #cd9c52ad;
}

.itemContainer::before {
	content: '';
	border: 1px solid #353535;
	display: block;
	width: 100%;
	height: 100%;
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate3d(-50%, -50%, 0) scale(1.015) rotate(0.5deg);
	border-radius: 1% 1% 2% 4% / 2% 6% 5% 4%;
}



</style>
