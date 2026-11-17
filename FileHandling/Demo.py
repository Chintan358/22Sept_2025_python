# f = open("D://test.txt",'w')
# f.write("Hello python")
# f.close()

# l = [
#     "hello python\n","hello tops\n","hello world\n"
# ]

# f = open("test.txt",'w')
# f.writelines(l)
# f.close()


# f = open("test.txt",'a')
# f.write("Hello")
# f.close()

# f = open("test.txt",'r')
# # data = f.read()
# data = f.readlines()
# print(data)
# f.close()


# f = open("test.txt",'r')
# while True:
#    data = f.readline()
#    if "python" in data:
#     print(data)
#    if not data:
#        break 
# f.close()


# f = open("test.txt",'r')
# while True:
#    data = f.readline()
#    if data.startswith("h"):
#     print(data)
#    if not data:
#        break 
# f.close()


# with open("home.txt",'w') as f:
#     f.write("hello")
    
# with open("test.txt",'r') as f:
#     f.seek(10)
#     print(f.tell())
#     data = f.read()
#     print(data)
#     print(f.tell())

# with open("index.txt",'r+') as f:
#     f.write("something")

# with open("index.txt",'w+') as f:
#     f.write("something")
#     f.seek(0)
#     data = f.read()
#     print(data)


# with open("a.jpg",'rb') as f:
#     data= f.read()
#     print(data)

import json
d = {
    "name":"qaid",
    "email":"qaid@gmil.com",
    "phone":"7485859685"
}
# with open("demo.json",'w') as f :
#     json.dump(d,f)


# with open("demo.json",'r') as f :
#     data = json.load(f)
#     print(data)