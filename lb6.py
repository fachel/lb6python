def main():
    n = 10
    a = 1
    fib1 = fib2 = 1
    fib_sum = 0
    j = 2
    for i in range(n):
        a += 1
    if a % 2 == 0:
        n = 5
    else:
        n = 10
    while j < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        j += 1
    if fib_sum % 2 == 0:
        fib_sum -= 1
    else:
        fib_sum += 2
    return fib_sum


print(main())
