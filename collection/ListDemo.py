# l = [10,20,30,40,50,50,'A',52.66,True]
# print(type(l))
# print(l)
# print(len(l))


#access list
# l = list((10,20,30,40,50,60,40))
# print(l)
# print(l[2:7:3])
# print(l[::-1])

#Change list
# sub = ["python","java","php","android","node"]
# k = ["abc","xyz"]
# sub[1]="abc"
# sub[1:3]=['a','b','c']
# sub.insert(1,"abc")
# sub.append("dfsfd")
# sub.extend(k)
# print(sub)


#remove 

# l =['A','B','C','D','E']
# l.remove("A")
# l.pop(1)
# l.clear()
# del l
# print(l)


#lOOP LIST

l =['A','B','C','D','E']

# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])

# i=0
# while i<len(l):
#     print(l[i])
#     i+=1

#List Comprehension
l = [1,2,3,4,5,6,7,8,9]
# k = []
# for i in l:
#     k.append(i*i)
# print(k)

# k = [i*i for i in l]
# k = [i for i in l if i%2==0]
# print(k)


sub = ["python","java","php","android","node"]
# k = []
# for i in sub:
#     if i.startswith("p"):
#         k.append(i)

# k = [i for i in sub if i.startswith("p")]
# k = [i for i in sub if "a" in i]
# print(k)


#sorting
# i = [10,20,58,46,12,36,98,74,52]
# i.sort()
# i.sort(reverse=True)
# i.reverse()

# k = sorted(i)

# print(k)


#copy

a = [10,20,30,40,20]

# b  =a.copy()
# b = list(a)
# b = a[::]
b  = a
# b.append(500)


# print(a)
# print(b)

# print(a.count(20))
# print(a.index(20))

for i in [10,20,30,54]:
    print(i)