import random

def Convert(string):
    list1 = []
    list1[:0] = string
    return list1

choice=input("What do you want to do\n1:Encode\n2:Decode\n")
alpha="qwertyuiop[]asdfghjkl;'\\zxcvbnm,./1234567890-=!~#}{?|£$%^&*()<> "

alpha=Convert(alpha)

key=alpha
random.shuffle(key)
print(key)

inp=input("enter your Text here:\n")
if choice == "1":
    inpA=""
    for i in inp:
        pos = alpha.index(i)
        print(i,key[pos])
        inpA = inpA + key[pos]
    print(inpA)
elif choice == "2":
    print()