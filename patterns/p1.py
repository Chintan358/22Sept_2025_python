# *****
# *****
# *****
# *****
# *****

# for j in range(5):
#     for i in range(5):
#         print("*",end="")
#     print()


# for j in range(5):
#     print(5*"*")
  
  
# *
# **
# ***
# ****
# *****


# for j in range(5):
#     for i in range(j+1):
#         print("*",end="")
#     print()

# for j in range(5):
#     print("*"*(j+1))
  
  
# *****
# ****
# ***
# **
# *

# lines=9
# for j in range(lines):
#     for i in range(lines-j):
#         print("*",end="")
#     print()


#     *
#    **
#   ***
#  ****
# *****

# lines=5
# for j in range(lines):
#     for k in range((lines-1)-j):
#             print(" ",end="")
#     for i in range(j+1):
#         print("*",end="")
#     print()

# lines=5
# for j in range(lines):
#     print(" "*((lines-1)-j),"*"*(j+1))

# *****
#  ****
#   ***
#    **
#     *


# lines=5
# for j in range(lines):
#     for i in range(j):
#             print(" ",end="")
#     for i in range(lines-j):
#         print("*",end="")
#     print()

# lines=5
# for j in range(lines):
#     print(" "*j,(lines-j)*"*")
    


# * * * * *
#  * * * * 
#   * * *
#    * *
#     *

# lines=5
# for j in range(lines):
#     print(" "*j,(lines-j)*"* ")

#    *
#   * *
#  * * *
# * * * *


#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *


# lines=5

# for j in range(lines):
#     print(" "*((lines-1)-j),"* "*(j+1))
# for j in range(1,lines):
#     print(" "*j,(lines-j)*"* ")
    


#      *
#     * *
#    *   *
#   *     *
#  *       *
#   *     *
#    *   *
#     * *
#      *



# 1
# 12
# 123
# 1234
# 12345


# for j in range(5):
#     for i in range(j+1):
#         print(i+1,end="")
#     print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10

# k=1
# for j in range(5):
#     for i in range(j+1):
#         print(k,end=" ")
#         k+=1
#     print()
    


# 54321
# 4321
# 321
# 21
# 1

# lines = 5
# for j in range(lines):
#     for i in range(lines-j,0,-1):
#         print(i,end="")
#     print()

# 0
# 10
# 010
# 1010
# 01010


for j in range(5):
    for i in range(j+1):
        print((j+i)%2,end="")
    print()


