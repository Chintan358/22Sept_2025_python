# def test(a):
#     print(a*a)
#     a+=1
#     if a<20:
#         test(a)
    
# test(10)
    
    
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
    
print(fact(5))
    
    
    
    