import numpy as np
import matplotlib.pyplot as plt

# Compute x and y coordinates for points on a sine curve
x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)

print(x)
print(y)

plt.plot(x, y)
plt.show()

x = np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()