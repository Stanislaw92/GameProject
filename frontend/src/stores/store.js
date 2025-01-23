import { defineStore } from 'pinia'



export const useArmoryBoxStore = defineStore({
    id: 'armoryBoxStore',
    state: () => ({
        visible: 'hidden',
        item: null,
        mouseCordX: 100,
        mouseCordY: 100,
        stats: ''
    }),
    actions: {
        updateVisibility(x){
            if (x) {
                this.visible = 'visible'
            } else { 
                this.visible = 'hidden'
            }
        },
        updateMouseCord(x,y){
            this.mouseCordX = x
            this.mouseCordY = y
        },
        updateItem(x){
            this.item = x
            this.stats = ''
            this.item.overall_stats.forEach((el)=>{
                if (el[0] == 'dmg'){
                    this.stats += `${el[0]}: ${el[1]} - ${el[2]}, `
                } else if (this.item.overall_stats.indexOf(el) + 1 < this.item.overall_stats.length){
                    this.stats += `${el[0]}: ${el[1]}, `
                } else {
                    this.stats += `${el[0]}: ${el[1]}`
                }
            })
        },
    }
})


export const useGetMouseCord = defineStore({
    id: 'getMouseCord',
    state: () => ({
        cordY: 0,
        cordX: 0,
    }),
    actions: {
        updateCord(x,y){
            this.cordY = y
            this.cordX = x
        },
    }
})

export const useTripStore = defineStore({
    id: 'tripStore',
    state: () => ({
        trips: 10,
        timer: 0
    }),
    actions: {
        updatedTrips(x){
            this.trips = x
        },
        updateTimer(x){
            this.timer = x
        },
    }
})

export const useReplyMsgUuid = defineStore({
    id: 'replyMsgStore',
    state: () => ({
        uuid: null,
        title: null
    }),
    actions: {
        updateUuid(x){
            this.uuid = x
        },
        updateTitle(x){
            this.title = x
        }
    }
})

export const useLoggedInProfile = defineStore({
    id: 'loggedInProfile',
    state: () => ({
        profile: null,

    }),
    actions: {

        updateProfile(x){
            this.profile = x
        }
    }
})

