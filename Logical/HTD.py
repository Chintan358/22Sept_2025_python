number = "9BB"

l = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

c = 0
sum=0
for i in number[::-1]:
    sum+=(l.index(i)*pow(16,c))
    c+=1
    
print(sum)