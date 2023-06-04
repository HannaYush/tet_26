list = [2, 11, 6, 24]

for i in list:
    if i <= 10:
        list.remove(i)
        print(list)



def square(n):
            list_fin = []
            list_square = map(lambda n: n ** 2, list)
            list_fin.append(list_square)

            return list_fin


print(square(list))




