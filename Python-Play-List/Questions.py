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


for i in range(6):
    j = 1
    for j in range(1,i+1):
        print(j, end=' ')
        j = j+1
    i = i+1
    print()    
