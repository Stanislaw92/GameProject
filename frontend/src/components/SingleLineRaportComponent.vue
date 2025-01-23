<template>
    <div v-if="this.profileStore.profile.name" class="line_style">
        <!-- {{updatedLine}} -->
        <span v-html="updatedLine"></span>
    </div>
    <div v-else>
        loading
    </div>
</template>

<script>
import { useLoggedInProfile } from '@/stores/store.js'
export default {
    name: 'SingleLineRaportComponent',
    props: ['line'],
    data() {
        return{
            updatedLine: '',
            profileStore: useLoggedInProfile()
        }
    },
    methods: {
        getLine(){
            const profileName = this.profileStore.profile.name
            this.updatedLine = this.line.replace(profileName, `<b style="font-size: 13px; color: rgb(51, 172, 164)"> ${profileName} </b>`)
        }
    },
    created(){
        this.getLine()


    },

}
</script>

<style scoped>
span {
    padding: 0;
}

.line_style:nth-child(odd) {
    background: rgba(0, 0, 0, 0.041)
}
.line_style:nth-child(even) {
    background: rgb(255, 255, 255)
}

.line_style {
    width: 100%;
    white-space: pre-line;
    padding: 3px 10px 5px 10px;

}
.name_of_user {
    font-size: 15px;
    color: rgb(51, 192, 114);
}
</style>