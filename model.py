# imports
# NumPy is a library for the Python
# programming language, adding support for large,
# multi-dimensional arrays and matrices
import numpy as np
# Matplot lib is a 2D plotting library for Python
import matplotlib.pyplot as plt
# Keras is a hign level open-source nerual-network library written in Python
# it runs on top of TensorFlow, Theano and PlaidML
import keras as kr
# The MNIST database is a large database of handwritten digits that is
# commonly used for training various image processing systems.
# This imports The MNIST dirctly from the from the keras API
from keras.datasets import mnist
from keras.models import Sequential
# Importing the constants.py
import constants
# Importing from keras Dense which implemnets the operation, Flatten is an
# operation preformed on a tensor thta treshapes the tensor to have a
# shape that is equal to the number of elements contained in tensor.
# Conv2D converts the image into pixels and takes an n-sized window
# those features are then condensed into a feature map and the
# window slides
# MaxPooling2D is used for spatial data
# Dropout is a feature that stops certain neurals from training in order to
# prevent an overfitting
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout

from keras.models import load_model


# This downloads the MNIST dataset from the Keras API. The dataset has 60,000
# images and associated labels used for training and 10,000 testing images
# with associated labels. We need to seperate the dataset into two groups
# a training group and a testing group. train_imgs, train_labels,
# test_imgs and test_labels.
(train_imgs, train_labels), (test_imgs, test_labels) = mnist.load_data()

# Debug
print(train_imgs.shape[0])
print(train_labels.shape[0])

print(test_imgs.shape[0])
print(test_labels.shape[0])


img_height, img_width = 28, 28

# We have to reshape the MNIST dataset with Keras, we will convert it from a 3d
# Array to a 4d NumPy array
# Making sure train_imgs and test_imgs are floats, so we can use decimal points
train_imgs = train_imgs.reshape(train_imgs.shape[0], img_width,
                                img_height, 1)
test_imgs = test_imgs.reshape(test_imgs.shape[0], img_width,
                              img_height, 1)
input_shape = (img_width, img_height, 1)
train_imgs = train_imgs.astype('float32')
test_imgs = test_imgs.astype('float32')

# Data is normalized when being used in a nerual network to obtain a mean close
# to 0 Normalizing the data generally speeds up learning and
# leads to faster convergence. Normalizing the RGB code by dividing it by the
# max RGB value(255)
train_imgs /= 255
test_imgs /= 255

num_classes = 10

train_labels = kr.utils.to_categorical(train_labels, num_classes)
test_labels = kr.utils.to_categorical(test_labels, num_classes)
train_labels[0]

print(test_imgs.shape[0])
print(test_labels.shape[0])


# Creating a model and adding layers
# Sequential allows you to create a nerual network layer by layer
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu', input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(constants.rate))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss=kr.losses.categorical_crossentropy,
              optimizer=kr.optimizers.Adadelta(), metrics=['accuracy'])


# Current set up requires the model to be trained every time the application
# is ran, so we will train out file here and ave the model for future use.
# The try and except block in Python is used to catch and handle exceptions.
# Python executes code following the try statement as a “normal” part of the
# program.The code that follows the except statement is the program's response
# to any exceptions in the preceding try clause.

print(test_imgs.shape)
print(test_labels.shape)


model.fit(train_imgs, train_labels,
          batch_size=constants.batch_size,
          epochs=constants.num_epoch,
          verbose=1,
          validation_data=(test_imgs, test_labels)
          )
model.save_weights("model.h5")
model.save("model.h5")

plt.imshow(test_imgs[3333].reshape(28, 28), cmap="gray")
plt.show()

try:
    print("Model loaded")
    model = load_model("model.h5")
except IndexError:
    print("Error opening file, no model Present")
    print("Creating Model")
    model_log = model.fit(train_imgs, train_labels,
                          batch_size=constants.batch_size,
                          epochs=constants.num_epoch,
                          verbose=1,
                          validation_data=(test_imgs, test_labels))
    model.save_weights("model.h5")
    model.save("model.h5")
    print("Model Saved.")

plt.imshow(test_imgs[3333].reshape(28, 28), cmap="gray")
plt.show()