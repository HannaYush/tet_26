
n = list(input("num"))

n.sort(reverse=True)
print(n)
for obj in n:
    for elem in obj:
        print(elem.replace('"', ''))



