def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Test
n = int(input("Enter number of terms: "))
fibonacci(n)
