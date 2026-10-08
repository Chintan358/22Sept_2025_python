number = 339
result = 0
multiplyr = 1
while number!=0:
    rem = number%8
    result+=(rem*multiplyr)
    multiplyr*=10
    number = number//8
    
print(result)
    