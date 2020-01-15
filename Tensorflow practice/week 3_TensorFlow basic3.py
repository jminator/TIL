import matplotlib.pyplot as plt
import numpy as np

# def step_function(x):
#     # return np.array(x>0.0, dtype=np.int)
#     return np.array(x>0.0, dtype=np.int64)

# x = np.arange(-5, 5, 0.1)
# y = step_function(x)

# print("x=", x, "\n", "y=", y)
# plt.plot(x, y)
# plt.show()

def sigmoid(x):
    return 1/(1+np.exp(-x))

# arange(start, stop, step)

x = np.arange(-7.0, 7, 1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.2, 1.2)

plt.show()