import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
tmp = np.array([[1,3],[2,3],[5,7],[8,20]])
x_data = tmp[:,0]
y_data = tmp[:,1]

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0, seed=555))
b = tf.Variable(tf.zeros([1]))
hypothesis = W * x_data + b #예측치

loss = tf.reduce_mean(tf.square(hypothesis -y_data))
optimizer = tf.train.GradientDescentOptimizer(0.003) # 매우 작은 LR
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(1001): # LR이 너무 작아 매우 여러번 해야 한다.
    if step%100 == 0:  # mini-batch 적용. 100번 단위만 쪼개서 진행한다.  
        sess.run(train)
        print(x_data, y_data, sess.run(hypothesis))
        print('step ==', step, sess.run(W), sess.run(b))
        print('loss==>', sess.run(loss))
        print("-------------------------------------")

        plt.plot(x_data, y_data, 'ro')
        plt.plot(x_data, sess.run(W) * x_data + sess.run(b))
        plt.show()
        print("-------------------------------------")
