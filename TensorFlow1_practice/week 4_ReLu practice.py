import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# x,y의 데이터 값
data = [[2, 0], [4, 0], [6, 0], [35, 1], [10, 1], [12, 1], [14, 1]]
#data = [[2, 9], [4, 10], [6, 12], [8, 9], [10, 99], [12, 15], [14, 20]]


x_data = [x_row[0] for x_row in data]
y_data = [y_row[1] for y_row in data]

# W와 b의 값을 임의로 정함
W = tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=0))
b = tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=0))
#b=tf.Variable(0.0)


y=W*x_data   # hypothesis 
#y = 1/(1 + np.e**(-(W * x_data + b))) # y 시그모이드 함수의 방정식을 세움


# loss를 구하는 함수
loss = tf.reduce_mean(tf.square(y - y_data))
#loss = -tf.reduce_mean(np.array(y_data) * tf.log(y) + (1 - np.array(y_data)) * tf.log(1 - y))


learning_rate=0.005 # 학습률 값

# loss를 최소로 하는 값 찾기
gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
# Minimize: Gradient Descent using derivative: W -= learning_rate * derivative
learning_rate = 0.001
gradient = tf.reduce_mean((W * x_data - y) * x_data)*2
descent = W - learning_rate * gradient
update = W.assign(descent)


# 학습
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sequence = []    #차트출력 자료 저장소 준비
   
    for i in range(90000):
        sess.run(update)
        sequence.append(sess.run(loss))    #차트 출력하기 위하여 값 저장
        if i % 10000 == 0:
          print("Epoch: %.f, loss = %.4f, 기울기 W = %.4f, 바이어스 b = %.4f" % (i, sess.run(loss),  sess.run(W), sess.run(b)))
          plt.plot(x_data, y_data, 'ro')
          plt.plot(x_data, sess.run(W) * x_data + sess.run(b))
          plt.show()

plt.plot(sequence,"o")
plt.show()