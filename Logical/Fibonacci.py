# 0 1 1 2 3 5 8 13 21 34 55 89 144 233


length = 15

a = 0  #1  1  2
b = 1  #1  2  3
print(a,b,end=" ")
for i in range(length):
    c = a+b   # 5
    print(c,end=" ")
    a = b
    b = c