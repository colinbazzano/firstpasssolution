"""Big O Exercises
Above the exercise is the time and space complexity

In the format of:

Time: O()
Space: O()

def foo():
    pass
"""
# Time: O(n)
# Space: O(1)


def foo(n):
    for i in range(n):
        print(i)
# -----------------------------------------------------------------------------------------

# Time: O(n)
# Space: O(n)


def foo2(n):
    collection = list(range(n))
    for i in collection:  # O(n) space
        print(i)
# -----------------------------------------------------------------------------------------
# Time: O(n)
# Space: O(n)


def foo3(n):
    print(n)
    if n > 0:
        foo(n-1)

# -----------------------------------------------------------------------------------------
# Time: O(n)
# Space: O(1)


def foo4(n):
    for i in range(n):
        print(i)

    n = n * n
    return n
# -----------------------------------------------------------------------------------------
# Time: O(3n) -- > O(n)
# Space: O(1)
# THROW THIS IN PYTHON TUTOR


def foo5(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
    for k in range(n):
        print(k)
    return n
# -----------------------------------------------------------------------------------------
# Time: O(n^2 + n) --> O(n^2)
# Space: O(1)


def foo6(n):
    for i in range(n):
        print(i)
        for j in range(n):
            print(j)
    for k in range(n):
        print(k)
    return n
# -----------------------------------------------------------------------------------------
# Time: O(n)
# Space: O(1)


def foo7(n):
    i = 0
    while i < n:
        print(i)
        i += 1
# -----------------------------------------------------------------------------------------
# Time: O(n/2) --> O(n)
# Space: O(1)


def foo8(n):
    i = 0
    while i < n:
        i += 1
        n -= 1
# -----------------------------------------------------------------------------------------
# Time: O(log n) - We are dividing by 2, cutting in half, which would be log n
# Space: O(1)


def foo9(n):
    i = 0
    while i < n:
        i += 1
        n /= 2


def anagrams(word):
