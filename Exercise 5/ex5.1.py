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
'''

for i in range (1, 7):
    data = list(range(1, y+1))
    ltime = timeit.repeat(setup=setupcode,stmt='linear_search(data, rand.randint(1, 1000))',repeat=1000, number=100)
    ##print("The linear search took", ltime,"seconds to find the index", x,"in the", y,"element data vector")
    btime = timeit.repeat(setup=setupcode,stmt='binary_search(data, 0, y-1, x = rand.randint(1, 1000))',repeat=1000, number=100)
    ##print("The binary search took", btime,"seconds to find the index", x,"in the", y,"element data vector")
    y = y * 2





