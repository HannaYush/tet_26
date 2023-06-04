keys = ['Hanna', 'Alex', 'Tom', 'Bob']
val = ['123456789', '3245776876', '0987778987', '55689964']
abc = {}
fin_dict = dict(zip(keys, val))
print(fin_dict)

name = str(input ("enter name:"))

for i in keys:
    if name == i:
        print("I call")
    else:
        print("ERROR")
        