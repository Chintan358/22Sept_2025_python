# student = {
#     "name":"Vansh",
#     "email":"vansh@gmail.com",
#     "phone":"1234567899",
#     "abc":"Vansh",
#     "lang":["gujarati","Hindi"],
#     123 : "fff",
#     True:"dfdf",
#     12.56:"fdsfd",
#     (10,2030):"dfffgd"
# }

# print(student)

# d = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(d["brand1"])
# print(d.get("brand1"))
# print(d.get("name","fdfds"))

# print(d.keys())
# print(d.values())
# print(d.items())



# d['brand']="Tata"
# d.update({"brand":"abc"})
# d['color']="red"
# print(d)

# d.pop("brand")
# d.popitem()
# d.clear()
# del d
# del d['brand']
# print(d)

# for i in d.items():
#     print(i)


# for i,j in d.items():
#     print(i)
#     print(j)


# st = {
#     "name":"qaid",
#     "email":"qaid@gmial.com",
#     "address":{
#         "country":"india",
#         "state":"gujarat",
#         "city":"surat"
#     },
#     "lang":["gujarati","Hindi"]
# }

# print(st['address']['country'])
# print(st['lang'][0])


# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# for i,j in myfamily.items():
#     print(i)
#     for k,l in j.items():
#         print(k)
#         print(l)
        
        
# a = {1,2,3}
# b = "a"

# k = dict.fromkeys(a,b)
# print(k)


d = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


# d['brand']="aaa"
d.setdefault("brand1","aaa")
print(d)