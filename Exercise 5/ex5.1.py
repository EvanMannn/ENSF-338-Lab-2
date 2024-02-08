import timeit
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
setupcode='''
import random as rand
def linear_search(data, x):
 
    for i in range(len(data)):
 
        if data[i] == x:
            return i
    return -1
def binary_search(data, low, high, x):
 
    if high >= low:
 
        mid = (high + low) // 2
 
        if data[mid] == x:
            return mid
 
        elif data[mid] > x:
            return binary_search(data, low, mid - 1, x)
        else:
            return binary_search(data, mid + 1, high, x)
 
    else:
        return -1

def linear(y):
    data = list(range(1, y+1))
    x = rand.randint(1, y)
    linear_search(data, x)

        

def binary(y):
    data = list(range(1, y+1))
    x = rand.randint(1, y)
    binary_search(data, 0, y-1, x)

'''
y = 1000
ltime= []
btime = []
ylist = [1000, 2000, 4000, 8000, 16000, 32000]
for i in range (1, 7):
    l = timeit.repeat(setup=(setupcode) , stmt='linear(y)',repeat=100, number=10, globals=locals())
    ltime.append(sum(l) / len(l)) 
    print("The linear search took an average of", ltime[i-1],"seconds to find the index in the", y,"element data vector\n")
    b = timeit.repeat(setup=(setupcode), stmt='binary(y)',repeat=100, number=10, globals=locals())
    btime.append(sum(b) / len(b))
    print("The binary search took an average of", btime[i-1],"seconds to find the index in the", y,"element data vector\n")
    y = y * 2

inter_linear = interp1d(ylist, ltime, kind='linear')
inter_binary = interp1d(ylist, btime, kind='quadratic')

xnew = np.linspace(min(ylist), max(ylist), 100)

plt.plot(ylist, ltime, "o", label='Linear Search')
plt.plot(ylist, btime, "o", label='Binary Search')
plt.plot(xnew, inter_linear(xnew), label='Linear Interpolation')
plt.plot(xnew, inter_binary(xnew), label='Binary Interpolation')
plt.legend()
plt.ylabel("Time (s)")
plt.xlabel("Number of Elements in Dataset")
plt.title("Linear Search vs Binary Search")
plt.grid(True)
plt.show()

#The





