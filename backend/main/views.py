from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import io
import base64
import json

# Load the pre-trained TensorFlow model
model = keras.models.load_model('./mnist_model/mnist_model.h5')


@csrf_exempt
def predict_number(request):
    if request.method == 'POST':
        # Load the canvas data from the request body
        canvas_data = json.loads(request.body.decode('utf-8')).get('canvasData', None)
        if not canvas_data:
            return JsonResponse({'error': 'Missing canvasData parameter'}, status=400)
        try:
            canvas_img = Image.open(io.BytesIO(base64.b64decode(canvas_data.split(',')[1])))
        except (IndexError, TypeError, binascii.Error):
            return JsonResponse({'error': 'Invalid canvasData parameter'}, status=400)
        canvas_img = canvas_img.resize((28, 28), resample=Image.BILINEAR)
        canvas_img = canvas_img.convert('L')
        canvas_arr = np.array(canvas_img).astype(np.float32) / 255.0
        canvas_arr = np.reshape(canvas_arr, (1, 28, 28, 1))

        # Make a prediction using the pre-trained TensorFlow model
        prediction = model.predict(canvas_arr)
        prediction = int(np.argmax(prediction))

        # Return the prediction as a JSON response
        return JsonResponse({'prediction': prediction})
    else:
        # Return a 405 Method Not Allowed error for any request method other than POST
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
