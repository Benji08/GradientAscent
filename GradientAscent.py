import numpy as np
import timeit
import random
import matplotlib.pyplot as plt

def gradient(x, y):
    d = np.array([400 * x**3 + 2*x - 2 - 400*x*y , 200*(y - x*x)])
    return d


def gradient_ascent(x, y, b, i_counter = 100000, epsilon = 10**-12):
    i = 0
    d = gradient(x, y)
    while(i<i_counter and (abs(d[0]*b)>epsilon or abs(d[1]*b)>epsilon)):
        i+=1
        d = gradient(x, y)
        x = x - d[0]*b
        y = y - d[1]*b
    print(i)


def visualisation(x, y, b, i_counter = 100000, epsilon = 10**-12):
    i = 0
    d = gradient(x, y)
    list_points_x = []
    list_points_y = []
    while(i<i_counter and (abs(d[0]*b)>epsilon or abs(d[1]*b)>epsilon)):
        i+=1
        d = gradient(x, y)
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
    plt.xlim([-5, 5])
    plt.ylim([-5, 5])
    plt.savefig("plot.png")



for j in range(10):
    x=random.randint(-5, 5)
    y=random.randint(-5, 5)
    blist = [0.0001, 0.0003, 0.0005]
    print(x, y)
    for i in range(3):
        print(timeit.timeit(stmt='gradient_ascent(2, 2, blist[i], 1000000, 10**-12)',globals=globals(), number=4)/4)
    print("------------------------------------------------------------------------------")


#gradient_ascent(-2, 3, 0.00192, 1000000, 10**-12)
#visualisation(4, -3, 0.0001, 1000000, 10**-12)
