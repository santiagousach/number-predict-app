# Handwritten Digit Recognition Web App
This is a web application that allows users to draw a digit on the canvas and uses a pre-trained machine learning model to predict the digit. The front-end of the application is built using Vue.js, while the back-end is built using Django. The machine learning model is built using TensorFlow.

## Prerequisites
To run this project, you need to have Docker installed on your machine.

Installation and Usage
Clone the repository:
```
git clone https://github.com/example/handwritten-digit-recognition.git
```

Build the docker container
```
docker-compose build

```

Start the Docker containers:
```
docker-compose up
```
Open application in your browser:
```
http://localhost:8080/
```
Draw a digit on the canvas and click "Predict" to see the predicted digit.

