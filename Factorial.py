def factorial(num):
    if num < 0:
        return "Cannot compute the factorial of negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, num + 1):
            factorial = factorial * i
        return factorial

# Tests
print(factorial(-8))
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(5))
print(factorial(6))