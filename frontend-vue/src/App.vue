<template>
  <div class="drawing-container">
    <div class="drawing-canvas">
      <h1>Predict a number from your drawing</h1>
      <div class="drawing-box" ref="box" @mousedown="startDrawing" @mousemove="drawLine" @mouseup="stopDrawing">
        <canvas ref="canvas"></canvas>
      </div>
      <div class="buttons">
        <button class="clear-button" @click="clearCanvas">Clear</button>
        <button class="predict-button" @click="predictNumber">Predict</button>
      </div>
      <div v-if="prediction !== null">
        <p>The number you drew is {{ prediction }}</p>
        <div class="feedback-buttons">
          <button class="thumbs-up" @click="thumbsUp">👍</button>
          <button class="thumbs-down" @click="thumbsDown">👎</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      isDrawing: false,
      lastX: 0,
      lastY: 0,
      ctx: null,
      prediction: null,
    };
  },
  mounted() {
    const canvas = this.$refs.canvas;
    canvas.width = 280;
    canvas.height = 280;
    this.ctx = canvas.getContext('2d');
    this.ctx.lineCap = 'round';
    this.ctx.lineWidth = 20;
    this.ctx.fillStyle = '#ffffff';
    this.ctx.fillRect(0, 0, canvas.width, canvas.height);
    this.ctx.strokeStyle = '#000000';
  },
  methods: {
    startDrawing(e) {
      this.isDrawing = true;
      this.lastX = e.offsetX;
      this.lastY = e.offsetY;
    },
    drawLine(e) {
      if (!this.isDrawing) return;
      this.ctx.beginPath();
      this.ctx.moveTo(this.lastX, this.lastY);
      this.ctx.lineTo(e.offsetX, e.offsetY);
      this.ctx.stroke();
      this.lastX = e.offsetX;
      this.lastY = e.offsetY;
    },
    stopDrawing() {
      this.isDrawing = false;
    },
    clearCanvas() {
      this.ctx.fillStyle = '#ffffff';
      this.ctx.fillRect(0, 0, 280, 280);
      this.prediction = null;
    },
    async predictNumber() {
      const canvasData = this.ctx.getImageData(0, 0, 280, 280);
      const canvas = document.createElement('canvas');
      canvas.width = canvasData.width;
      canvas.height = canvasData.height;
      canvas.getContext('2d').putImageData(canvasData, 0, 0);
      const dataUrl = canvas.toDataURL('image/jpeg');
      try {
        const response = await axios.post('http://localhost:8001/predict/', { canvasData: dataUrl });
        console.log(response);
        this.prediction = response.data.prediction;
      } catch (error) {
        console.log(error);
      }
    },
    thumbsUp() {
      this.sendFeedback('correct');
    },
    thumbsDown() {
      this.sendFeedback('incorrect');
    },
    async sendFeedback(feedback) {
      //Console log the feedback
      console.log(feedback);
},

},
};
</script>

<style scoped>
.drawing-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.drawing-canvas {
  text-align: center;
}

.drawing-box {
  display: inline-block;
  width: 300px;
  height: 300px;
  border: 2px solid #000000;
  border-radius: 10px;
  margin: 20px;
}

.buttons {
  margin: 20px;
}

.clear-button {
  background-color: #cccccc;
  color: #ffffff;
  border: none;
  padding:10px;
  margin-right: 10px;
  border-radius: 5px;
  cursor: pointer;
  }

.predict-button {
  background-color: #007bff;
  color: #ffffff;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  }

.feedback-buttons {
  margin-top: 20px;
}

.thumbs-up, .thumbs-down {
  font-size: 30px;
  border: none;
  background-color: transparent;
  cursor: pointer;
  margin-right: 10px;
}
</style>
       
