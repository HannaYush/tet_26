a = str(input("num1 + num2"))

b = list(a)
print(b)


a_a = a.replace("+", " ")
print(a_a)

sum_a = sum(int(x) for x in a_a.split())
print(sum_a)
