s = str(input("enter same str:"))
def remove_char(s_s):
    result = s_s[1: -1]
    return result
print(remove_char(s))

if len(s) <= 2:
    print("ERROR")
