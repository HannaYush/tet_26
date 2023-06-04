list1 = [1, 3, 5, 7, 9]
list2 = [1, 5, 2, 4, 8, 6]
list3 = []


for i in list1:
    for x in list2:
        if i == x:
            list3.append(i)
            break

print(list3)
