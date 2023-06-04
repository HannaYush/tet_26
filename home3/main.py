a = list(input("enter str"))

a_a = filter(str.isdecimal, a)
a_f = "".join(a_a)
print(list(a_f))
