str='ABCD'
length=4
for i in range(length):
    for j in range(length-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(str[j],end=" ")
    print()
for i in range(length):
    for j in range(i):
        print(" ",end="")
    for j in range(length-i):
        print(str[j],end=" ")
    print()
    