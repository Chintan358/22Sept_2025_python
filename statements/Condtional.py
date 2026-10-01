# if-else , match-case

# age = 17
# if age>18:
#     print("elegeble for voting")
# else:
#     print("not elegeble for voting")


a = 100
b = 1000
c = 1000


# if a>b and a>c:
#     print("A is greater")
# elif b>c and b>a:
#     print("b is greate")
# elif c>a and c>b:
#     print("c is greater")
# else:
#     print('something went wrong')

# if a>b:
#     if a>c:
#         print("a is greater")
#     else:
#         print("c is greater")
# else:
#     if b>c:
#         print("b is greater")
#     else:
#         print("c is greater")


# marks = int(input("enter marks : "))
# 0-100 other wise invalid
# 91-100 : A
# 71-90 : B
# 51-70 : C
# 35-50 : D
# 0 - 34 : F

# if marks>90 and marks<=100:
#     print("A")
# elif marks>70 and marks<=90:
#     print("B")
# elif marks>50 and marks<=70:
#     print("C")
# elif marks>=35 and marks<=50:
#     print("D")
# elif marks>=0 and marks<=34:
#     print("f")
# else:
#     print("invalid marks")



# choice = int(input("enter choice :"))

# match(choice):
#     case 1 : print("Gujarati")
#     case 2 : print("Hindi")
#     case 3 : print("english")
#     case _ : print("Invalid choice")


cont = 'y'
while cont=='y':
    a = int(input("enter number : "))
    b = int(input("enter number : "))
    choice = input("enter opration to b perform : ")

    match(choice):
        case '+': print("addtion is :",a+b)
        case '-': print("substraction is :",a-b)
        case '*': print("multiplcation is :",a*b)
        case '/': print("division is :",a/b)
        case _ : print("invalid operation")
    
    cont = input("do you want to continue? press y or n :")