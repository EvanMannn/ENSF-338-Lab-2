import random as rand
import timeit
setupcode='''
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

def for_loop_linear():
    y = 1000
    for i in range(1, 7):
        data = list(range(1, y+1))
        

def for_loop_binary():
    y = 1000
    for i in range(1, 7):
        data = list(range(1, y+1))

'''
y = 1000
for i in range (1, 7):
    ltime = timeit.repeat(setup=setupcode,stmt='for_loop_linear()',repeat=1000, number=100)
    ##print("The linear search took", ltime,"seconds to find the index in the", y,"element data vector")
    btime = timeit.repeat(setup=setupcode,stmt='for_loop_binary()',repeat=1000, number=100)
    ##print("The binary search took", btime,"seconds to find the index in the", y,"element data vector")
    y = y * 2





