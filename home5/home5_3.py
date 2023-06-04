num = int(input("num"))
if str(num) == str(num)[::-1]:
    num += 1
while(str(num) != str(num)[::-1]):
    num += 1

print(num)
