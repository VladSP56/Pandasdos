import numpy as np

#a = np.ones((2,5))
#print(a)

#a =np.random.random((4,5))
#a = np.arange(0, 10, 2)
#a=np.linspace(0, 13, 10)
#print(a)

import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = x**2
plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Graph of a function y = x**2")
plt.grid(True)
plt.show()


