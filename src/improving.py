# cache

# base cases
# if n == 0:
#     return 1
# if n == 1:
#     return 1
cache = {0: 1, 1: 1}


def rec_fib(n):
    if n in cache:
        return cache[n]
    cache[n] = rec_fib(n-1) + rec_fib(n-2)

    return cache[n]


print(rec_fib(40))


def fib(n, cache=None):
    if cache is None:
        cache = {}
    if n <= 2:
        return 1
    elif n in cache:
        return cache[n]
    else:
        answer = fib(n-1, cache) + fib(n-2, cache)
        cache[n] = answer
        return answer

print(fib(50))