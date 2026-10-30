l = [1,3,5,6,98,7,4,5,4,65,41]
# k = []
# def check_odd(a):
#     if a%2!=0:
#         return a

# for i in l:
#     a =  check_odd(i) 
#     if a is not None:
#         k.append(a)

# k = filter(check_odd,l)
k = filter(lambda a:a%2!=0,l)
# print(list(k))


subjects = ["java","python","node", "php","android","react"]

# k = filter(lambda a : a.startswith("p"),subjects)
# k = filter(lambda x :"a" in x ,subjects)
k = filter(lambda x: x.startswith("p") or "a" in x,subjects)
print(list(k))