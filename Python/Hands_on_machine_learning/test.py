import numpy as np
import math
import matplotlib.pyplot as plt

x  = np.arange(0.1,1.1,0.1)
print(x)
z = 0
y = []

for i in range(0,len(x)-1):
    z =  z + math.exp(x[i])
    y.append(math.log(z))

y.append(3)
print(len(y))
print(len(x))
print(y)
plt.plot(x,y)
plt.show()
