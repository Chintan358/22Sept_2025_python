st = "the quick brown fox jumps over the lazy dog"
d = {}

for i in st:
    if d.get(i) is None:
        d.update({i:1})
    else :
        k = d.get(i)
        k+=1
        d.update({i:k})
    
print(d)
print(len(d))