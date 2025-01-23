<template>
    <div class="page_container" @mouseup="StopDragging">
      <div class="buttons">
        <button @click="goLeft">
            <i class="fa-solid fa-arrow-left" style="color: #010101;"></i>
        </button>
        <button @click="goRight">
            <i class="fa-solid fa-arrow-right" style="color: #010101;"></i>
        </button>
        <button @click="goUp">
            <i class="fa-solid fa-arrow-up" style="color: #010101;"></i>
        </button>
        <button @click="goDown">
            <i class="fa-solid fa-arrow-down" style="color: #010101;"></i>
        </button>

      </div>
      <div class="container">
          <div class="board">
              <div v-for="i in stepNumber"
                  :key="i"
                  class="cube"
                  @mouseenter="checkNumberOfSquare(i)"
              >
                  <div class="face top"></div>
                  <div class="face bottom"></div>
                  <div class="face left"></div>
                  <div class="face right"></div>
                  <div 
                    
                    class="face front">{{i[0]}}</div>
                  <div class="face back"></div>
              </div>
          </div>
          <div 
            class="moving_box" 
            :style="{top: mouseCoordY, left: mouseCoordX}"

            :class="{dragging:dragging}" 
          >
            <!-- :style="[ dragging ? {top: dragCordY +'px', left: dragCordX + 'px'} : {transform: 'translateX(' + cordX + 'px) translateY(' + cordY + 'px)'}]"  -->
            <div 
              @mousedown="DragBox"

              class="cube cube2">
                  <div class="face top"></div>
                  <div class="face bottom index_top"></div>
                  <div class="face left index_top"></div>
                  <div class="face right index_top"></div>
                  <div class="face front index_top"></div>
                  <div class="face back"></div>
            </div>
          </div>
          <!-- <div class="upper_board">
              <div
                  class="cube"
              >
                  <div class="face upper top2"></div>
                  <div class="face upper bottom2"></div>
                  <div class="face upper left2"></div>
                  <div class="face upper right2"></div>
                  <div class="face upper front2"></div>
                  <div class="face upper back2"></div>
              </div>
          </div> -->



      </div>
    </div>
</template>

<script>
export default {
    name: 'TestBattleView',
    data(){
        return {
            stepNumber: [],
            cordY: -121,
            cordX: -135,
            redSquarePlace: 0,
            dragging: false,
            dragCordX: 0,
            dragCordY: 0,
            targetSquare: 0,
        }
    },
    methods: {
        DragBox() {
            const dir_x = (this.targetSquare[0] - this.targetSquare[0] % 10) / 10
            const dir_y = this.targetSquare[0] % 10
            this.dragCordX = -121 + (dir_x * 30)
            this.dragCordY = -135 + (dir_y * 30)

            console.log(dir_x)
            console.log(this.targetSquare[0])
            
            this.dragging = true
        },
        StopDragging(){
            console.log('stop dragging')
            this.dragging = false
        },
        goDown(){
          if (this.cordY < 150 ){
            this.cordY += 30
            this.redSquarePlace += 10
          }
        },
        goUp() {
          if (this.cordY > -120 ){
            this.cordY -= 30
            this.redSquarePlace -= 10
          } 
        },
        goRight() {
          if (this.cordX < 136) {
            this.cordX += 30
            this.redSquarePlace += 1

          }
        },
        goLeft() {
          if (this.cordX > -134) {
            this.cordX -= 30
            this.redSquarePlace -= 1
          }
        },
        checkCordX: function (event) {
            console.log(event.pageX)
            console.log(event.pageY)
        },
        checkNumberOfSquare(number){
          if (this.dragging) {
            this.targetSquare = number[0]
            console.log(number[0])
          }
        }
    },
    computed: {
      mouseCoordX(event){
        return event.pageX
      },
      mouseCoordY(event){
        return event.pageY
      }
    },
    created(){
        for (let i = 0; i<100; i++) {
            this.stepNumber.push([i, 0])
        }
        console.log(this.stepNumber)
        this.stepNumber[0][1] = 1
        this.targetSquare = this.stepNumber[0]
        console.log(this.targetSquare)
    }
}
</script>

<style scoped>
button {
  display: inline-block;
  outline: none;
  cursor: pointer;
  font-weight: 600;
  border-radius: 3px;
  padding: 12px 24px;
  border: 0;
  color: #000021;
  background:skyblue;
  line-height: 1.15;
  font-size: 16px;
}

button:hover{
      transition: all .3s ease;
      /* box-shadow: 0 0 0 0 #fff, 0 0 0 3px skyblue; */
      transform: scale(1.1)
}

.page_container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 95vw;
    height: 95vh;
    flex-direction: column;
}

.buttons {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    width: 50%;

}
.index_top {
  z-index: 110;
}

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 95vw;
    height: 95vh;
    perspective: 3000px;
    position: relative;
    /* transform: translateX(-150px); */
    /* transform:  rotateX(55deg) rotateZ(-35deg) rotateY(0deg) translateY(25%);
    transform-style: preserve-3d; */
}

.board {
    width: 300px;
    height: 300px;
    display: grid;
    align-items: center;
    justify-content: center;
    grid-template-columns: repeat(10, 30px);
    grid-template-rows: repeat(10, 30px);
    /* z-index: 10; */
    /* transform: rotate3d(-5, -0.2, 1, -25deg) translateY(25%); */
    /* transform:  rotateX(55deg) rotateZ(-35deg) rotateY(0deg) translateY(25%); */
    /* transform: rotate3d(1, 1, 0, 45deg); */
    /* transform-style: preserve-3d; */
    /* transform:  rotateX(55deg) rotateZ(-35deg) rotateY(0deg) translateY(25%); */
    /* transform:  rotate3d(1, 0.5, -1, 65deg); */
    transform-style: preserve-3d;
    
}
.upper_board {
    position: absolute;
    width: 30px;
    height: 30px;
    display: grid;
    align-items: center;
    justify-content: center;
    grid-template-columns: repeat(10, 30px);
    grid-template-rows: repeat(10, 30px);

    /* transform: rotate3d(-5, -0.2, 1, -25deg) translateY(25%); */
    /* transform:  rotateX(55deg) rotateZ(-35deg) rotateY(0deg) translateY(25%); */
    /* transform: rotate3d(1, 1, 0, 45deg); */
    /* transform:  rotate3d(1, 0.5, -1, 65deg) translateZ(29px); */
    transform-style: preserve-3d;
}
.moving_box {
    cursor: grab;
    cursor: -moz-grab;
    cursor: -webkit-grab;
    position: fixed;
    width: 30px;
    height: 30px;
    display: grid;
    /* z-index: -1; */
    /* align-items: center;
    justify-content: center; */
    /* transform:  rotateX(55deg) rotateZ(-35deg) rotateY(0deg) translateY(0px) translateZ(-30px); */
    transform-style: preserve-3d;
    /* transform: translateY(15px); */
}
.moving_box:active{
    cursor: grabbing;
    cursor: -moz-grabbing;
    cursor: -webkit-grabbing;
}

.moving_box .face {
  background: rgb(143, 30, 19);
  opacity: 1;
}

.upper_board .face {
    opacity: 1;
    border: 0.5px solid rgba(0, 0, 0, 0.445);
    font-size: 2rem;
}

.cube {
    position: relative;
    /* width: 200px;
    height: 50px; */
    transform-style: preserve-3d;
}

.cube2 {
  width: 30px;
  height: 30px;
}

/* .cube2 .face {
  width: 20px;
  height: 20px;
} */

.face {
    /* transform: translate(-50%, -50%); */
    width: 30px;
    height: 30px;
    background: skyblue;
    border: 1px solid rgba(0, 0, 0, 0.505);
    position: absolute;
    opacity: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: Arial, sans-serif;
    font-size: 0.5rem;
}

.upper {
  width: 300px;
  height: 300px;
}

.dragging {
  position: fixed;
  /* opacity: 0.9; */
}

.painted .face {
    background: red;
}

.front {
  transform: translateZ(15px);
  /* background: rgb(14, 17, 17)(0, 0, 0); */
  opacity: 1;
}

.back {
  transform: translateZ(-15px) rotateY(180deg);
}

.left {
  transform: translateX(-15px) rotateY(-90deg);
}

.right {
  transform: translateX(15px) rotateY(90deg);
}

.top {
  transform: translateY(-15px) rotateX(90deg);
  /* height: 200px; */
}

.bottom {
  transform: translateY(15px) rotateX(-90deg);
  /* height: 200px; */
}

.front2 {
  transform: translateZ(15px);
  /* background: rgb(14, 17, 17)(0, 0, 0); */
}

.back2 {
  transform: translateZ(-15px) rotateY(180deg);
}

.left2 {
  transform: translateX(-15px) rotateY(-90deg);
  width: 30px;
}

.right2 {
  transform: translateX(285px) rotateY(90deg);
  width: 30px;
}

.top2 {
  transform: translateY(285px) rotateX(90deg);
  height: 30px;
}

.bottom2 {
  transform: translateY(-15px) rotateX(-90deg);
  height: 30px;
}







                















.scene {
  perspective: 1000px;
}

.container_sphere {
  margin-top: 5vh;
  margin-left: auto;
  margin-right: auto;
  position: relative;
  width: 200px;
  height: 200px;
  transform-style: preserve-3d;
}
.border {
  border: 1px solid black;
}
.circle {
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: rgba(204,0,102, 1);
}
/* X Axis */
.circle:nth-child(1) {transform: rotate3d(1, 0, 0, 0deg);}
.circle:nth-child(2) {transform: rotate3d(1, 0, 0, 36deg);}
.circle:nth-child(3) {transform: rotate3d(1, 0, 0, 72deg);}
.circle:nth-child(4) {transform: rotate3d(1, 0, 0, 108deg);}
.circle:nth-child(5) {transform: rotate3d(1, 0, 0, 144deg);}
/* Y Axis */
.circle:nth-child(6) {transform: rotate3d(0, 1, 0, 0deg);}
.circle:nth-child(7) {transform: rotate3d(0, 1, 0, 36deg);}
.circle:nth-child(8) {transform: rotate3d(0, 1, 0, 72deg);}
.circle:nth-child(9) {transform: rotate3d(0, 1, 0, 108deg);}
.circle:nth-child(10) {transform: rotate3d(0, 1,0, 144deg);}
/* Z Axis */
.circle:nth-child(11) {transform: rotate3d(0, 1, 0, 90deg) rotate3d(1, 0, 0, 0deg);}
.circle:nth-child(12) {transform: rotate3d(0, 1, 0, 90deg) rotate3d(1, 0, 0, 36deg);}
.circle:nth-child(13) {transform: rotate3d(0, 1, 0, 90deg) rotate3d(1, 0, 0, 72deg);}
.circle:nth-child(14) {transform: rotate3d(0, 1, 0, 90deg) rotate3d(1, 0, 0, 108deg);}
.circle:nth-child(15) {transform: rotate3d(0, 1, 0, 90deg) rotate3d(1, 0, 0, 144deg);}

/* Light effect */
.light {
   margin: auto;
   border-radius: 50%;
   width: 200px;
   height: 200px;
  box-shadow: 10px 1px 30px white;
} 
/* Clip the sphere a bit */
.clip {
  clip-path: circle(47%);
}
</style>