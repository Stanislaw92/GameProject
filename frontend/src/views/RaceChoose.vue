<template>
    <div class="container">
        <div class="textStyle">Choose class what u want to play</div>
        <div class="radio-input-wrapper flexStyle">
            <div>
                <div class="card">
                    <div class="card-details">
                        <p class="text-title">Class 1</p>
                        <p class="text-body">Class description</p>
                    </div>
                </div>
                <label class="label">
                    <input value="1" name="value-radio" class="radio-input" type="radio" v-model="picked" @click="clicked">
                    <div class="radio-design"></div>
                    <div class="label-text">Class 1</div>
                </label>
            </div>
            <div>
                <div class="card">
                    <div class="card-details">
                        <p class="text-title">Class 2</p>
                        <p class="text-body">Class description</p>
                    </div>
                </div>
                <label class="label">
                    <input value="2" name="value-radio" class="radio-input" type="radio" v-model="picked" @click="clicked">
                    <div class="radio-design"></div>
                    <div class="label-text">Class 2</div>
                </label>
            </div>
            <div>
                <div class="card">
                    <div class="card-details">
                        <p class="text-title">Class 3</p>
                        <p class="text-body">Class description</p>
                    </div>
                </div>
                <label class="label">
                    <input value="3" name="value-radio" class="radio-input" type="radio" v-model="picked" @click="clicked">
                    <div class="radio-design"></div>
                    <div class="label-text">Class 3</div>
                </label>
            </div>
            <div>
                <div class="card">
                    <div class="card-details">
                        <p class="text-title">Class 4</p>
                        <p class="text-body">Class description</p>
                    </div>
                </div>
                <label class="label">
                    <input value="4" name="value-radio" class="radio-input" type="radio" v-model="picked" @click="clicked">
                    <div class="radio-design"></div>
                    <div class="label-text">Class 4</div>
                </label>
            </div>
        </div>
        <input placeholder="Enter name here" class="input-style" type="text" v-model="inputName">
        <div v-if="showTxt" style="color:red;margin-bottom:5px;">U need to select a race!</div>
        <button class="accept_button" @click="confirm">Accept</button>
    </div>
</template>

<script>
import { axios } from '@/common/api.service.js';
export default {
    name: 'RaceView',
    data() {
        return {
            radioChecked: false,
            showTxt: false,
            inputName: '',
            picked: null,

        }
    },
    methods: {
        async confirm() {
            if (this.radioChecked) {
                const endpoint = `/api/v1/profiles/create/${this.picked}/`
                try {
                    await axios.post(endpoint, {name: this.inputName})
                    this.$router.push('/')
                } catch (error) {
				console.log(error.response);
				alert(error.response.statusText);
			}
            } else {
                this.showTxt = true
            }
        },
        clicked() {
            this.showTxt = false
            this.radioChecked = true
 
        }
    }
}
</script>

<style scoped>
.input-style {
  padding: 10px;
  border: 2px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  color: #555;
  outline: none;
  margin-bottom: 20px;
}

.input-style:focus {
  border-color: #007bff;
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

.container {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}
.textStyle {
    font-size: 35px;
    font-family: "Trirong", serif;
    font-weight: bold;
}

.flexStyle {
    margin-top: 20px;
    width: 100%;
    display: flex;
    align-items: space-between;
    justify-content: space-evenly;

}

.label {
  display: flex;
  align-items: center;
  flex-direction: column;
  border-radius: 100px;
  padding: 14px 16px;
  margin: 5px 0;
  cursor: pointer;
  transition: .3s;
}

.label:hover,
.label:focus-within,
.label:active {
  background: hsla(0, 0%, 80%, .14);
}

.radio-input {
  position: absolute;
  left: 0;
  top: 0;
  width: 1px;
  height: 1px;
  opacity: 0;
  z-index: -1;
}

.radio-design {
  width: 22px;
  height: 22px;
  border-radius: 100px;
  background: linear-gradient(to right bottom, hsl(154, 97%, 62%), hsl(225, 97%, 62%));
  position: relative;
}

.radio-design::before {
  content: '';
  display: inline-block;
  width: inherit;
  height: inherit;
  border-radius: inherit;
  background: hsl(0, 0%, 90%);
  transform: scale(1.1);
  transition: .3s;
}

.radio-input:checked+.radio-design::before {
  transform: scale(0);
}

.label-text {
  color: hsl(0, 0%, 60%);
  margin-left: 14px;
  letter-spacing: 3px;
  text-transform: uppercase;
  font-size: 18px;
  font-weight: 900;
  transition: .3s;
}

.radio-input:checked~.label-text {
  color: hsl(0, 0%, 40%);
}

.accept_button {
  display: flex;
  align-items: center;
  justify-content: center;
  outline: none;
  cursor: pointer;
  width: 150px;
  height: 50px;
  background-image: linear-gradient(to top, #D8D9DB 0%, #fff 80%, #FDFDFD 100%);
  border-radius: 30px;
  border: 1px solid #8F9092;
  transition: all 0.2s ease;
  font-family: "Source Sans Pro", sans-serif;
  font-size: 14px;
  font-weight: 600;
  color: #606060;
  text-shadow: 0 1px #fff;
}

.accept_button:hover {
  box-shadow: 0 4px 3px 1px #FCFCFC, 0 6px 8px #D6D7D9, 0 -4px 4px #CECFD1, 0 -6px 4px #FEFEFE, inset 0 0 3px 3px #CECFD1;
}

.accept_button:active {
  box-shadow: 0 4px 3px 1px #FCFCFC, 0 6px 8px #D6D7D9, 0 -4px 4px #CECFD1, 0 -6px 4px #FEFEFE, inset 0 0 5px 3px #999, inset 0 0 30px #aaa;
}

.accept_button:focus {
  box-shadow: 0 4px 3px 1px #FCFCFC, 0 6px 8px #D6D7D9, 0 -4px 4px #CECFD1, 0 -6px 4px #FEFEFE, inset 0 0 5px 3px #999, inset 0 0 30px #aaa;
}

.card {
 width: 150px;
 height: 204px;
 border-radius: 20px;
 background: #f5f5f5;
 position: relative;
 padding: 1.8rem;
 border: 2px solid #c3c6ce;
 transition: 0.5s ease-out;
 overflow: visible;
 margin-bottom: 20px;
}

.card-details {
 color: black;
 height: 100%;
 gap: .5em;
 display: grid;
 place-content: center;
}

.card-button {
 transform: translate(-50%, 125%);
 width: 60%;
 border-radius: 1rem;
 border: none;
 background-color: #008bf8;
 color: #fff;
 font-size: 1rem;
 padding: .5rem 1rem;
 position: absolute;
 left: 50%;
 bottom: 0;
 opacity: 0;
 transition: 0.3s ease-out;
 cursor: pointer;
}

.text-body {
 color: rgb(134, 134, 134);
}

/*Text*/
.text-title {
 font-size: 1.5em;
 font-weight: bold;
}

/*Hover*/
.card:hover {
 border-color: #008bf8;
 box-shadow: 0 4px 18px 0 rgba(0, 0, 0, 0.25);
}

</style>