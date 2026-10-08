number = 339
result = 0
multiplyr = 1
while number!=0:
    rem = number%2
    result+=(rem*multiplyr)
    multiplyr*=10
    number = number//2
    
print(result)
    