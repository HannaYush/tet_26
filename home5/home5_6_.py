k = [1, 5, 55, 100]
for n in k:
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            print("false")

        else:
            print("true")
            break




