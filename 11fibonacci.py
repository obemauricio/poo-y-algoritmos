def fibonacci(n):
    print(n)
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + (n - 2)

n = int(input("introduce un numero: "))
print(fibonacci(n))
