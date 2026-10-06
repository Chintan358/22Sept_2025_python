# number = 159
# temp = number
# sum = 0
# while number!=0:
#     rem = number%10
#     sum+=pow(rem,3)
#     number  =number//10
    
# if temp==sum:
#     print("armstrong")
# else:
#     print("Not armstrong")
    
    
# 100 - 999 : 

for i in range(100,1000):
    number = i
    temp = number
    sum = 0
    while number!=0:
        rem = number%10
        sum+=pow(rem,3)
        number  =number//10
        
    if temp==sum:
        print(f"{temp} : armstrong")
    else:
        pass
        # print(f"{temp} : Not armstrong")