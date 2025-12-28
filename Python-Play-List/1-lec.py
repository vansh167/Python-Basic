# string fuinctions   



# str = "i am a coder."

# print(str.endswith("er."))   #check the last words 

#print(str.capitalize())     # ijn capitlize the first letter 
     
# print(str.replace("er","re"))  #for replacing letter

# print(str.find("re"))   #for find in string

# print(str.count("a"))   #for count total what you count 




 

# practice questions of ths 

# 1>. WAP TO INPUT USER'S FIRST NAME & PRINT ITS LENGTH
# 2>. WAP TO FIND THE OCCURRENCE OF '$' IN A STRING.


# user = input("Write $ Something here :")
# print(len(user))                         ans 1
# print(user.count("$"))                   ans 2





# Condition statment  ==============================================

# age = 16
# if(age <= 19):
#     print("can vote")
# elif(age == 18 ):
#     print("under age")
    
# else:("Nothing....See more")




# for loop===============================================================
# for row in range(5):                #(0,0,0,0,5)
#     for col in range(row + 1):           #(1,2,3,4)
#         print("*",end="")
#     print()    

# n = 5
# for i in range(n, 0, -1):
#     print("*" * i)
  

# data = [10, 20, 30]
# for i, value in enumerate(data):
#     value = value * 2
#     print(i, value)



# n = 5

# # upper half
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2*i + 1))

# # lower half
# for i in range(n-2, -1, -1):
#     print(" " * (n - i - 1) + "*" * (2*i + 1))




# data = [10, 20, 30, 40]
# for i, value in enumerate(data):
#     print(i, value)


# data = [1,2,3,4,5,6,7,8]
# for i in range(len(data)):
#     if i == 4:
#         break
# print(i)

# scores = [45, 67, 89, 34, 90, ]
# count = 0
# for s in scores:
#     if s >= 60:
#         coun9]t += 1
# print(count)

# num = int(input("Enter you number for check Here....:"))
# if num % 3 == 0 :
#     print("Fizz")
# elif num % 5 == 0 :
#     print("Buzz")
# elif num % 3 and num & 5 == 0 :
#     print("FizzBuzz")
# else:
#     print(num)

# number= [1,2,3,4,5,6,7,8,8,0,0,0,0 ]
# posti = 0
# negti = 0
# count = 0

# for n in number :
#     if n > 0:
#         posti += 1
#     elif n < 0 :
#         negti += 1
#     else:
#         count += 1


# print("Positive number :",posti)
# print("Negative number :",negti)
# print("Zero number :",count)


# Using only:

# for loop

# if / elif / else

# comparison operators (> < ==)

# % (only for divisibility)

# Count how many numbers are:

# Positive & divisible by 5

# Positive but NOT divisible by 5

# Negative even

# Zero

# numbers = [5, 10, 15, 0, -2, -4, 3, 6, -9, 0]
# positive = 0
# negative = 0
# negativeEven = 0
# zero = 0

# for n in numbers :
#     if n > 0 and n % 5 == 0:
#          positive += 1
#     elif n > 0 and n % 5 != 0 :
#          negative += 1
#     elif n < 0 and n % 2 == 0 :
#          negativeEven += 1
#     elif n == 0:
#          zero += 1     
# print(positive )
# print(negative)
# print(negativeEven)
# print(zero) a =5
# a = 5

# for i in range(1,a):
#     print(i)



# for i in range(3):                                     #rows
#      for j in range(3):                                  #column
#          print("*", end=" ")
#      print()        


# for i in range(1,4):
#      for j in range(i):
#         print("*", end=" ")
#      print()   

# for i in range(1,7):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()



# for i in range(1,2):
#     for j in range(4):
#         print(1, end=" ")
#     print()     

# rows = 5
# cols = 3

# for r in range(rows):
#     for c in range(cols):
#         print(f"Row {r}, Col {c}")

# for i in range(2, 5):
#     for j in range(1, i):
#         print(i, j)

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i, end= " ")
#     print()    

# data = [3, 7, 10, 0, -4, 8]
# positiveEven =0
# positiveOdd = 0
# zero = 0
# negative = 0

# for d in data:
#     if d > 0  and d % 2 == 0 :
#         positiveEven += 1
#     elif d > 0 and d % 2 != 0:
#         positiveOdd += 1
#     elif d == 0 :                 #
#         zero += 1
#     else:
#         negative += 1
        
# print("Positive even :", positiveEven)    
# print("Positive odd :", positiveOdd)        
# print("zero :", zero)        
# print("negative :", negative)        
             

# k = 1
# while k <= 5:
#     print(k)
#     k += 1



# =============================================================  While loop 

# i = 1
# while i <= 10:
#     if i == 6:
#        break
#     print(i)
#     i += 1

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i) 

a = 1
while a <= 10:
    print(a)
    a += 1