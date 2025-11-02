import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)

a = 1
b = 0
c = 0

y = a * x**2 + b * x + c

plt.plot(x,y, color = 'darkblue', linewidth = 2)

plt.title('Simple line chart')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.grid(True, linestyle='-', alpha=1)

plt.show()

print (y)