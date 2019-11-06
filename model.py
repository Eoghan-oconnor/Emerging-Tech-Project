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
# Importing the constants.py
import constants

# This downloads the MNIST dataset from the Keras API. The dataset has 60,000
# images and associated labels used for training and 10,000 testing images
# with associated labels. We need to seperate the dataset into two groups
# a training group and a testing group. train_imgs, train_labels,
# test_imgs and test_label.
(train_imgs, train_labels), (test_imgs, test_label) = mnist.load_data()



