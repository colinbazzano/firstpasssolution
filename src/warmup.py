# First Pass Solution for Fibonacci


import math


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


print(fib(10))

# Define these runtimes


def foo(n):
    sq_root = int(math.sqrt(n))
    for i in range(0, sq_root):
        print(i)


foo(10)

# My guess is that this is Linear.
