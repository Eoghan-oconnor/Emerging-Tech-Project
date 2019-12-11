# Importing Flask as fl
from flask import Flask as fl
from flask import render_template
from flask import request

# Numpy 
import numpy as np

# base64 from encoding 
import base64

# Tensorflow to use the model.h5
import tensorflow as tf

# PIL is a %%python imaging library
from PIL import ImageOps, Image

# This section runs the Main application 
app = fl(__name__)

# Gives working directory for webpage
@app.route('/')
def hello():
    return render_template('app/frontend/Home.html')

    if __name__ == '__main__':
        app.run()

# getting uploaded image from the js 


@app.route('/image', methods=['GET', 'POST'])
def image():
    # retirve image from  request
    userImage = request.values['imageData']

    print(userImage)

    decodedImage = base64.b64decode(userImage[22:])
    with open ("image.png", "wb") as f:
        f.write(decodedImage)

    model = load_model()

    reshapedImage = reshape()
        
    prediction_array = model.predict(reshapedImage)
    prediction = np.argmax(prediction_array)
  
    print(prediction)
    return{"prediction": str(prediction)}
    
def load_model():
    jsonModel = open('model.json', 'r')
    loadModel = jsonModel.read()
    jsonModel.close()
    loadedModel = tf.keras.models.model_from_json(loadModel)
    
    loadedModel.load_weights('model.h5')
    print('Loaded')
    return loadedModel

def predict(model, image_array):
    prediction_array = model.predict(image_array)
    prediction = np.argmax(prediction_array)
    return prediction

def reshape():
    # Adapted from: https://dev.to/preslavrachev/python-resizing-and-fitting-an-image-to-an-exact-size-13ic
    ogImage = Image.open('image.png').convert("L")
    size = 28, 28
    ogImage = ImageOps.fit(ogImage, size, Image.ANTIALIAS)

    img_array = np.array(ogImage).reshape(1, 28, 28, 1)
    return img_array