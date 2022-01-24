def collatz(n):
    print(n, end=" ")
    if n == 1:
        return n
    elif n % 2 == 0:
        return collatz(n // 2)
    else:
        return collatz(n * 3 + 1)

collatz(17)