number = 159
temp = number
sum = 0
while number!=0:
    rem = number%10
    sum+=pow(rem,3)
    number  =number//10
    
if temp==sum:
    print("armstrong")
else:
    print("Not armstrong")
    
    
# 100 - 999 : 