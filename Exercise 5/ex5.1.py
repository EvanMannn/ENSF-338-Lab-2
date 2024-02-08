import timeit
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
for i in range (1, 7):
    l = timeit.repeat(setup=(setupcode) , stmt='linear(y)',repeat=1000, number=100, globals=locals())
    ltime = sum(l) / len(l)
    print("The linear search took", ltime,"seconds to find the index in the", y,"element data vector\n")
    b = timeit.repeat(setup=(setupcode), stmt='binary(y)',repeat=1000, number=100, globals=locals())
    btime = sum(b) / len(b)
    print("The binary search took", btime,"seconds to find the index in the", y,"element data vector\n")
    y = y * 2





