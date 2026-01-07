# Exercise 1: Print first 10 natural numbers using while loop

# num = 0
# while num < 10:
#     num += 1
#     print(num)  

# Exercise 2: Print the following pattern  : 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i, end="")
#     print()    


# for i in range(6):
#     j = 1
#     for j in range(1,i+1):
#         print(j, end=' ')
#         j = j+1
#     i = i+1
#     print()    

# Exercise 3: Calculate sum of all numbers from 1 to a given number
# user = int(input("Enter your number here:"))
# sum = 0
# for i in range(1,user+1):
#       sum += i 

# print(sum)


# Exercise 4: Print multiplication table of a given number


# user = int(input("Enter your number here:"))

# for i in range(user, 11):

#       sum = user*i

# print(i,sum)

n = 5
# upper half
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2*i + 1))

# lower half
for i in range(n-2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2*i + 1))


for i in range(5):
    print(i)
