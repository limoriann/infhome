import matplotlib.pyplot as plt
import numpy as np

def f(x, a=1, b=1):
  return (x**b + a**b) / (x**b)
# Задание 1

x_left = np.linspace(-10, -0.01, 1000)
x_right = np.linspace(0.01, 10, 1000)

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

#2
plt.axes([0.25, 0.50, 0.10, 0.15])
plt.title('для малых х')
plt.plot(x, f(x, 1, 1), label = '1 ф-ция', color = 'red')
plt.plot(x, f(x, 1, 2), label = '2 ф-ция', color = 'green')
plt.plot(x, f(x, 2, 1, label = '3 ф-ция', color = 'blue')

plt.axes([0.45, 0.60, 0.25, 0.25])
plt.title('для больших х')
plt.plot(x, f(x, 1, 1), label = '1 ф-ция', color = 'red')
plt.plot(x, f(x, 1, 2), label = '2 ф-ция', color = 'green')
plt.plot(x, f(x, 2, 1), label = '3 ф-ция', color = 'blue')

plt.show()
         
#Задание 3
x = np.linspace(-5, -0.01, 1000)
plt.rcParams['figure.figsize'] = [5, 5]
plt.rcParams['figure.autolayout'] = True

plt.plot(x,f(x, 1, 1), color = 'red', label = '1 случай')
plt.plot(x,f(x, 1, 2), color = 'green, label = '2 случай')
plt.plot(x,f(x, 2, 1), color = 'blue', label = '3 случай')
plt.plot(x, [0] * len(x), color = 'gold', label = 'f(x) = 0')
plt.grid()
plt.title('График')
plt.xlabel('Ось абсцисс')
plt.ylabel('Ось ординат')
plt.legend()
plt.axes([0.21, 0.17, 0.50, 0.25])

x = np.linspace(-5, -0.01, 1000)
plt.axvline(0, linewidth=0.5, c='red', linestyle='--')

#Задание 4
x = np.linspace(-5, 5, 1000)
plt.rcParams['figure.figsize'] = [3, 3]
plt.rcParams['figure.autolayout'] = True
x = np.linspace(-1, 2, 1000)
plt.plot(x,f(x, 1, 1), color = 'red', label = '1 случай')
plt.plot(x,f(x, 1, 2), color = 'green', label = '2 случай')
plt.plot(x,f(x, 2, 1), color = 'lue', label = '3 случай')
plt.plot(x, [0] * len(x), color = 'yellow, label = 'f(x) = 0')
plt.grid()
plt.title('График')
plt.xlabel('Ось абсцисс')
plt.ylabel('Ось ординат')
plt.legend()

def C_P(ax, x, a, b1, b2, array_b, k, fontsize = 12, hide_labels = False):
    ax.plot(x, f(x, a, b1), color = 'pink', label = '1 случай')
    ax.plot(x, f(x, a, b2), color = 'orange', label = '2 случай')   
    ax.grid()
    ax.plot(x, f(x, a, array_b[k][0]), color = 'purple, label = '1 случай')
    ax.plot(x, f(x, a, array_b[k][1]), color = 'black', label = '2 случай')
    ax.legend()
    ax.locator_params(nbins = 3)
    if hide_labels:
        ax.set_xticklabels([])   
        ax.set_yticklabels([]) 
    else:
        ax.set_xticklabels('Ось абсицсс', fontsize = fontsize)
        ax.set_yticklabels('Ось ординат', fontsize = fontsize)
