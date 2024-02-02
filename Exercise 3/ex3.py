'''
Question 1:
A profiler is a tool that analyzes a program while its running and collects statistics about things such as execution duration,
numbers of calls to functions, memory usage, etc. These statistics are what make up the profile for the code

Question 2:
Benchmarking focuses on one singular operation and tests its speed, but profiling isn't concerned with comparing things but trying
to get an overview of the entire program. 

Question 3:
The output can be seen in the terminal

Question 4:
-   ncalls is the number of calls made to the specific function. If recursion was used then it is shown as n/m where n is the total calls
    m is the primitive calls. 
-   tottime is total time spent within that function .
-   percall is the time spent per call on th given function or tottime / ncalls.
-   cumtime is the total time spent in this function and any sub functions within it.
-   The percall that follows cumtime is same as before but now cumtime / ncalls.
-   The last column is the data about the function. 

The execution time of the program can be found in the very first line displayed in the terminal, which tells you the total function calls
followed by the execution time of the program.
'''




import timeit
import cProfile as p
import re

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

test_function()
third_function()

p.run("test_function();third_function()")
