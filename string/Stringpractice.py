st = "Sun rises in East ss fddf"

# "ss East in rises sun"
# "ss tsaE ni sesir nus"
# "nus sesir ni tsaE ss"
# "ss rises in easr sun"

# words = st.split(" ")
# k = ""
# for i in words[::-1]:
#     k+=i+" "
# print(k)

# print(st[::-1])

# words = st.split(" ")
# k=""
# for i in words:
#     k+=i[::-1]+" "
# print(k)

words = st.split(" ")
# temp = words[0]
# words[0] = words[4]
# words[4] = temp

words[0],words[len(words)-1]=words[len(words)-1],words[0]
k=""
for i in words:
    k+=i+" "
print(k)