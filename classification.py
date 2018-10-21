# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import numpy as np

print('Working with TensorFlow version %s' % tf.__version__)

# Use this to control whether plots will be displayed
display_graphics = False

# Models we will train
names_of_models = ['model1', 'model2']
models_to_test = []

# Read fashion_mnist data set
fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images / 255.0

if display_graphics:
    import matplotlib.pyplot as plt

    # Display the first 25 images
    plt.figure(figsize=(10, 10))
    for index in range(25):
        plt.subplot(5, 5, index + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[index], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[index]])
    plt.show()

# *** Model 1 ***
if 'model1' in names_of_models:
    # Building model using Keras
    model1 = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    # Compiling model
    model1.compile(optimizer=tf.train.AdamOptimizer(),
                   loss='sparse_categorical_crossentropy',
                   metrics=['accuracy'])

    # Training model
    model1.fit(train_images, train_labels, epochs=5)

    models_to_test.append(model1)

# *** Model 2 ***
if 'model2' in names_of_models:
    # Building model using Keras
    model2 = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(64, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    # Compiling model
    model2.compile(optimizer=tf.train.AdamOptimizer(),
                   loss='sparse_categorical_crossentropy',
                   metrics=['accuracy'])

    # Training model
    model2.fit(train_images, train_labels, epochs=5)

    models_to_test.append(model2)


# Evaluating accuracy
print('')
print('Test accuracy for trained models')
for index in range(len(models_to_test)):
    test_loss, test_acc = models_to_test[index].evaluate(test_images, test_labels)
    print('Test accuracy for Model %s: %s' % (names_of_models[index], test_acc))





