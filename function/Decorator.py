# def before(func):
#     def exceute():
#         print("Calling before ...")
#         func()
#     return exceute

# def after(func):
#     def exceute():
#         func()
#         print("Calling after ...")
#     return exceute


# def test():
#     print("test calling")
    
# test()


def add(func):
    def execute(*a):
        func(*a)
        sum=0
        for i in a:
            sum+=i
        print(sum)
    return execute


def mul(func):
    def execute(*a):
        func(*a)
        sum=1
        for i in a:
            sum*=i
        print(sum)
    return execute
    
@mul
@add
def calc(a,b):
    print("Calculation...")
    
    
calc(10,20)


#create a function that take value
#@numbersonly
#@charsonly