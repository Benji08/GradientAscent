import numpy as np
import timeit
import random
import matplotlib.pyplot as plt


def hessian(x, y):
    hessian = np.array([[1200*x*x-400*y+2, -400*x],[-400*x, 200]])
    gradient = np.array([400 * x**3 + 2*x - 2 - 400*x*y , 200*(y - x*x)])
    hessian = np.linalg.inv(hessian)
    d = hessian.dot(gradient)
    return d

def newton(x, y, b, i_counter = 100000, epsilon = 10**-12):
    i = 0
    d = hessian(x, y)
    while i<i_counter and (abs(d[0]*b)>epsilon or abs(d[1]*b)>epsilon):
        i+=1
        d = hessian(x, y)
        x = x - d[0]*b
        y = y - d[1]*b
    print(i)


def visualisation(x, y, b, i_counter = 100000, epsilon = 10**-12):
    i = 0
    d = hessian(x, y)
    list_points_x = []
    list_points_y = []
    while i<i_counter and (abs(d[0]*b)>epsilon or abs(d[1]*b)>epsilon):
        i+=1
        d = hessian(x, y)
        list_points_x.append(x)
        list_points_y.append(y)
        x = x - d[0]*b
        y = y - d[1]*b
    plt.plot(list_points_x, list_points_y, label = "points")
    plt.title("gradient descent")
    plt.xlabel("X")
    plt.ylabel("Y", rotation=0)
    plt.legend()
    plt.grid(True)
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    plt.savefig("plot.png")


for j in range(10):
    x=random.randint(-5, 5)
    y=random.randint(-5, 5)
    blist = [0.1, 0.5, 1]
    i=0.0001
    print(x, y)
    for i in range(3):
        print(timeit.timeit(stmt='newton(x, y, blist[i], 1000000, 10**-12)',globals=globals(), number=4)/4)
    print("------------------------------------------------------------------------------")

#visualisation(2, -3, 0.0001, 1000000, 10**-12)
#newton(2, -3, 0.0001, 1000000, 10**-12)
