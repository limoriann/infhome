import matplotlib.pyplot as plt
import numpy as np
#Задание 1

def f(x, a=1, b=1):
  return (x**b + a**b) / (x**b)

x_left = np.linspace(-10, -0.2, 1000)
x_right = np.linspace(0.2, 10, 1000)

plt.plot(x_left, f(x_left), label = '1 график', color = 'red')
plt.plot(x_right, f(x_right), color = 'red')

plt.plot(x_left, f(x_left, 1, 2), label = '2 график', color = 'green')
plt.plot(x_right, f(x_right, 1, 2), color = 'green')

plt.plot(x_left, f(x_left, 2, 1), label = '3 график', color = 'blue')
plt.plot(x_right, f(x_right, 2, 1), color = 'blue')

plt.axvline(0, linewidth=0.5, c='red', linestyle='--')

plt.grid()
plt.ylim([-10, 10])
plt.title('Графики')
plt.xlabel('Ocь aбсцисс')
plt.ylabel('Оcь oрдинат')
plt.legend()
plt.show()
