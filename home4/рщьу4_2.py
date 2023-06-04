fib1 = fib2 = 1
x = int(input("num:"))
print(fib1, fib2, end="")
for i in range(2, x):
    fib1, fib2 = fib2, fib1 +fib2
    print(fib2, end="")

