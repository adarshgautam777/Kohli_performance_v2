import numpy as np
import matplotlib.pyplot as plt

# Compute x and y coordinates for points on a sine curve
# x = np.arange(0, 3*np.pi, 0.1)
# y = np.sin(x)

# print(x)
# print(y)

# plt.plot(x, y)
# plt.show()  # this pause the program

# print("I a here")

# x = np.arange(0, 3*np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)

# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('Sine and Cosine')
# plt.legend(['Sine', 'Cosine'])
# plt.show()


# x = np.arange(0, 3*np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)

# setting up a subplot grid having
# height 2 and width 1 and set the first
# subplot as active
# plt.subplot(2, 1, 1)  # third parameter shows where to show the graph 1 for up and 2 for down


# # Creating the first subplot
# plt.plot(x, y_sin)
# plt.title("Sine wave")

# # Creating the second subplot
# plt.subplot(2, 1, 2)
# plt.plot(x, y_cos)
# plt.title("Cosine wave")

# plt.show()

# x = [0, 2, 3, 5]
# y = [6, 7, 9, 10]

# plt.plot(x, y)
# plt.axis([0, 6, 0, 20])
# plt.show()

# 1) y = x**2
# 2) y = -5x**2 + 6x + 1
# 3) y = 1 - x**2/2

x = np.linspace(-20, 20, 100)


def fun(x):
    y = []
    for elem in x:
        result = elem**2
        # result = -5*(elem**2) + 6*(elem) + 1
        # result = 1 - (elem**2)/2
        y.append(result)
    return y


y = fun(x)

plt.plot(x, y)

# Creating the first subplot
plt.plot(x, fun(x))
plt.title("Y equals to x2")

# # Creating the second subplot
plt.subplot(2, 1, 2)
plt.plot(x, fun(x))
plt.title("Y equals to x2")

plt.show()