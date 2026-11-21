# print("program started")
# try:
#     a = 10
#     b = a/5
#     print(b)
# except Exception as e:
#     print(e)
# print("program ended")


print("program started")
try:
    a = 10
    b = a/2
    print(b)
    
    a  = [10,20,30]
    print(a[0])  
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
else:
    print("ok")
finally :
    print("always executable")
print("program ended")