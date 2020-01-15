import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
mnist = input_data.read_data_sets("C:/Users/joosu/OneDrive/Documents/_사이버대학교/3학년 2학기/딥러닝/MNIST", one_hot = True)

tr_image = mnist.train.images
tr_y = mnist.train.labels
te_image = mnist.test.images
te_y = mnist.test.labels

print(len(tr_image), type(tr_image))
print(len(tr_y), type(tr_y))
print(len(te_image), type(te_image))
print(len(te_y), type(te_y))

print(tr_image[0])
plt.show()
