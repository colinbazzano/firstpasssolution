# Print that factorial of n


def rec_factorial(n):
    print(n)
    # base case
    if n <= 1:
        return 1
    # what step can we do recursively
    return n * rec_factorial(n - 1)


print(rec_factorial(5))
