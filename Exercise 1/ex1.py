"""
Part 1:
This code calculates the fibonnaci sequence value 
at a given index of the fibonacci sequence

Part 2:
Yes, it is an example of a divide and conquer algorithm 
because it splits the process into pieces.

Part 3:
The complexity of the algorithm is O(2^n)

Part 5:
The complexity of the improved algorithm is O(n)


"""

import timeit
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

#Part 4:
def memoize(func):
    cache = dict()
    
    def memoized_func(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    
    return memoized_func

blah = '''
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def memoize(func):
    cache = dict()
    
    def memoized_func(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    
    return memoized_func
    '''

improved_memoize = memoize(func)
time_fib = []
improved_time_fib = []

for i in range(0,35):
    time_fib.append(timeit.timeit(setup = blah, stmt = 'func(i)', globals=globals(), number = 1))

for i in range(0,35):
    improved_time_fib.append(timeit.timeit(setup= blah, stmt='improved_memoize(i)', globals=globals(), number = 1))

print(time_fib)

#print(improved_time_fib)


#plt.scatter(range(0,35),time_fib)

plt.scatter(range(0,35),improved_time_fib)
plt.xlabel("n value")
plt.ylabel("computation time")
plt.title("fibonacci sequence function without memoization")
plt.show()
