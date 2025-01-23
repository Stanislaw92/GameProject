<template>
    <div v-if="!counter" class="card">
      <div class="trip" >
        <div class="imageField">
          <img src="../../../static/photos/trip1.png" alt="trip_page_photo">
          <div class="whatever"></div>
        </div>
        <div class="textField">You have {{logged_in_profile.trips}} / 32 trips left</div>
        <div class="buttonField">
          <button @click="startTrip">trip!</button>
        </div>
      </div>

    </div>
    <div 
      v-else-if="counter"
      class="card"
    > 
        <span class="timer">{{counter}}</span>
    </div>

</template>

<script>

import { useTripStore } from '@/stores/store.js'
import { axios } from '@/common/api.service.js';
export default {
  name: 'TripView',
  data() {
    return {
      logged_in_profile: {},
      trip_timer: 0,
      counter: 0,
      intervalId: '',
      isRotate: false,
      startRotating: false,
    }
  },
  methods: {
      rotateCard(){
        this.startRotating = true
        setTimeout(()=>{
          this.isRotate = true
        }, 3000)
      },
      async getProfileData() {
          let endpoint = '/api/v1/profiles/'
          try {
              const response = await axios.get(endpoint)
              this.logged_in_profile = response.data[0]
              console.log(this.logged_in_profile)
              const store = useTripStore()
              store.updatedTrips(this.logged_in_profile.trips)

 
              const date_now = new Date()

              if (this.logged_in_profile.trip_cooldown > date_now.getTime() && this.logged_in_profile.trip_cooldown != 0){
                // this.interval(this.logged_in_profile.trip_cooldown)
                const date_now = new Date()
                  this.counter = Math.round((this.logged_in_profile.trip_cooldown - date_now.getTime()) / 1000 )

                  this.intervalId  = setInterval(() => {
                        const intervalDate = new Date()
                        this.counter = Math.round((this.logged_in_profile.trip_cooldown - intervalDate.getTime()) / 1000 )
                        if (this.counter <= 0){
                          this.counter = 0
                          clearInterval(this.intervalId)
                        }
            }, 1000)
              } 
              // else if (this.logged_in_profile.trip_cooldown <= date_now.getTime() && this.logged_in_profile.trip_cooldown != 0) {
              //   this.trip()
              // }
          } catch (error) {
              console.log(error.response);
              alert(error.response.statusText);
          }
      },
      async startTrip() {
        const endpoint = `/api/v1/profiles/${this.logged_in_profile.uuid}/`

        if (this.logged_in_profile.trips) {

          
          try {
            const dateNow = new Date()
            const timerDate = dateNow.getTime() + 10000
            console.log(timerDate)

            const result = await axios.put(endpoint, {
              trips: this.logged_in_profile.trips - 1,
              trip_cooldown: timerDate,
            })
            console.log(result)

            this.trip_timer = timerDate
            this.counter = (timerDate - dateNow) / 1000
  
            this.interval(timerDate)

          } catch(error){
            console.log(error)
          }
        }
      },
      interval(timerDate) {
            const date_now = new Date()
            this.counter = Math.round((timerDate - date_now.getTime()) / 1000 )

            this.intervalId  = setInterval(() => {
                  const intervalDate = new Date()
                  this.counter = Math.round((timerDate - intervalDate.getTime()) / 1000 )
                  console.log(this.counter)
                  if (this.counter <= 0){
                    this.counter = 0
                    clearInterval(this.intervalId)
                    this.trip()
                  }
            }, 1000)
      },
      checkTripCounter(){
        const store = useTripStore()
        const date_now = new Date()

        console.log(store.timer)
        console.log(date_now.getTime())
        if (store.timer > date_now.getTime()){
            // const counterInterval = setInterval(() => {
            //     const date_now = new Date()
            //     this.counter = Math.round((store.timer - date_now.getTime()) / 1000 )
            //     console.log(this.counter)
            //     if (this.counter == 0){
            //       clearInterval(counterInterval)
            //     }
            // }, 1000)
          this.interval(store.timer)
        }
      },
      async trip() {

        const endpoint = `/api/v1/trip_results/create/`
        const endpointUpdate = `/api/v1/profiles/${this.logged_in_profile.uuid}/`


        try {
          this.$emit('changeTripsNumber')
            
            const resultUpdate = await axios.put(endpointUpdate, {
              trip_cooldown: 0,
            })

            const result = await axios.post(endpoint)
            console.log(result.data.result)
            console.log(resultUpdate.data)

            if (result.data.result == 'True') {
                this.$notify({
                  title: "Trip result",
                  text: "You have successfully completed your trip!",
                  duration: 4000,
                  type: 'success'
                });
            } else {
                this.$notify({
                  title: "Trip result",
                  text: "You dont complete your trip",
                  duration: 4000,
                  type: 'warn'
                });
            }
            this.getProfileData()

        } catch (error) {
            console.log(error)
        }



        // const num_of_trips = this.logged_in_profile.trips - 1

        // const endpoint = `/api/v1/profiles/${this.logged_in_profile.uuid}/`
        // try {
        //     this.$emit('changeTripsNumber')
        //     const result = await axios.put(endpoint, {trips: num_of_trips})
        //     console.log(result)
        //     this.getProfileData()

        // } catch (error) {
        //     console.log(error)
        // }
      },
  },
  created() {
    clearInterval(this.intervalId)
    this.getProfileData()
    // this.checkTripCounter()
  },
  watch: {
        $route (to, from){
          console.log(to)
            if (from.fullPath == '/tripView/') {
                // clearInterval(this.intervalId)
            } 

        }
  }
}
</script>

<style scoped>
img {
  width: 90%;
  max-width: 400px;
  border-radius: 10px;
  box-shadow: 0px 0px 10px 2px black;
  opacity: 0.9;
  position: relative;
}

button {
  background: #0a1820;
  font-family: inherit;
  padding: 0.6em 1.3em;
  font-weight: 900;
  font-size: 18px;
  border: 3px solid #feb584;
  border-radius: 0.4em;
  box-shadow: 0.1em 0.1em;
  margin-top: 10px;
  color: #feb584;

}

button:hover {
  transform: translate(-0.05em, -0.05em);
  box-shadow: 0.15em 0.15em;
}

button:active {
  transform: translate(0.05em, 0.05em);
  box-shadow: 0.05em 0.05em;
}

.whatever {
    background-image: -webkit-gradient(
        linear,
        left top,
        left bottom,
        color-stop(0, #000000),
        color-stop(1, rgba(0,0,0,0))
    );
    background-image: -o-linear-gradient(bottom, #000000 0%, rgba(0,0,0,0) 100%);
    background-image: -moz-linear-gradient(bottom, #000000 0%, rgba(0,0,0,0) 100%);
    background-image: -webkit-linear-gradient(bottom, #000000 0%, rgba(0,0,0,0) 100%);
    background-image: -ms-linear-gradient(bottom, #000000 0%, rgba(0,0,0,0) 100%);
    background-image: linear-gradient(to bottom, #000000 0%, rgba(0,0,0,0) 100%);
    height:20%;
    position:relative;
    width:100%;
    top: -100%;
}


.card {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 75%;
  min-width: 300px;
  max-width: 400px;
  height: 550px;
  border: 1px solid black;
  border-radius: 10px;
  box-shadow: 0px 0px 15px 2px black;
  flex-direction: column;
  justify-content: space-around;
  background-color: black;
  padding: 20px;
}

.trip {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-direction: column;
  width: 100%;
  height: 100%;
}

.timer {
  font-size: 50px;
}

.textField {
  font-family: 'Lugrasimo', cursive;
  font-size: 20px;
  font-weight: bold;
  color: #feb584;
}

@media only screen and (min-width: 300px) and (max-width: 500px) {
  .textField {
    font-size: 15px;
  }
}
</style>