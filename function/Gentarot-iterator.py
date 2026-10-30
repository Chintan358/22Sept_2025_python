# l = [10,20,30,40,50,60]

# k = iter(l)
# print(next(k))
# print(next(k))


# def test():
#     return "hello"
#     return "test"

# def test():
#     yield "Hello"
#     yield "test"

# k = test()
# print(next(k))
# print(next(k))


def sqaure(a):
    for i in range(a):
        yield i*i
    
k = sqaure(5)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
