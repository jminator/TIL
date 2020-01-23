import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
tmp = np.array([[1,3],[2,3],[5,7],[8,20]])
x_data = tmp[:,0]
y_data = tmp[:,1]

# Placeholder를 이용해 x_data, y_data의 값을 각각 입력
X = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0, seed=555))
b = tf.Variable(tf.zeros([1]))
hypothesis = W * X + b #예측치

loss = tf.reduce_mean(tf.square(hypothesis - y))
optimizer = tf.train.GradientDescentOptimizer(0.005)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(10):
    print(sess.run(train, feed_dict={X: x_data, y: y_data}))
    print(x_data, y_data, sess.run(hypothesis, feed_dict={X: x_data, y: y_data}))
    print('step ==', step, sess.run(W), sess.run(b))
    print('loss==>', sess.run(loss, feed_dict={X: x_data, y: y_data}))
    print("-------------------------------------")

# Prediction
print(sess.run(hypothesis, feed_dict={X:2}))