list1 = ['lemon', 'apple', 'apple', 'pomello', 'pomello', 'pomello']
list2 = {}
for i in list1:
    if i in list2.keys():
        list2[i] += 1
    else:
        list2[i] = 1
key = max(list2, key=list2.get)
print(key, list2[key])







