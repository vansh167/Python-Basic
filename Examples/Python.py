# num1 = int( input("Enter a value :"))
# num2 = int( input("Enter a value :"))

# sum = num1 + num2/2
# print(sum)


# string ===========================================

# str1 = "This is a string."
# str2 = """Apna College"""
# str3 = 'Hi Vanssh'

# print(str1, str2, str3)

# str1 = "This is a string.\ntdbjkwnbdkjwqndkldmqwld"  \n   \t
# print(str1)

# str1 = "vansh\t"
# str2 = "dhiman"
# final = str1+str2
# print(final)

# sr1 = "Vansh"
# sr2 = "Dhiman"
# lenth = len(sr1)
# print(lenth)

# ================================indexing======================   str[0]

# str1 = "HAllo"

# print(str1[- 3:-1])

# ===================================Practice Questions ===================


# name = input("Enter Your Name :")
# # str1 = len(name)
# print(len(name))



# # =====================================conditions

# age = 15
# if(age >= 18):
#     print("Can Vote")


# else:
#     print("Cannot Vote Yet")
# print(age)


# ===========================nestng=
# age = 18
# if(age >= 18):
#     if(age >= 80):
#         print("You are too old to vote")
#     else:
#         print("Can drive")
# else:
#     print("Cannot Vote Yet")
# print(age)

# # ======================================= QQ

# num = int(input("Enter a number :"))

# if(num % 7 == 0):
#     print("Even Number")
# else:
#     print("odd Number")

# ==========================================

# marks = [23,23,43,12,55]

# # print(marks[0:2]) 

# marks.append(99)
# marks.sort()

# print(marks)
# # student = ["vansh", 35,]
# # print(student[1])
# # ============================================tuple=

# tup = (92,1,3,1,3,4,5)

# print(tup.count(1))


# ================================= Questions
# movies = []
# movie1 = input("Enter your favourite movie :")
# movie2 = input("Enter your favourite movie :")
# movie3 = input("Enter your favourite movie :")
 
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)


# print(movies)

# ================================== Palindrom
# string = [1,2,3]
# string2 = [1,2,3]
# string2.reverse()
# if(string == string2[::-1]):
#     print("Palindrom")
# else :
#     print("Not a Palindrom")


# ===================================== 

# grade = ["A","F","B","C","E","D"]
# grade.sort()
# print(grade[2:4])




# # ==================================== lecture 4

# info = {
#     "key" : "value",
#     "hi" : {
#     "name" : "Vansh",
#     "age" : 19,
#     "marks" : [99,45,67]}
# }
# print(info.values())



# collection = {"hello", "hi", "hey", "hello", "hi"} 
# print(collection.union())
# print(collection.intersection())


# nums = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter a number to search :"))
# i = 0 #initionalization
# while i < len( nums):
#     if(nums[i] == x):
#         print("Found at index ", i)
#     i += 1

# i = 1
# while i <= 5:
#     print(i)
#     if( i == 3):
#       break
#     i += 1

# i = 0
# while i <= 5:
#     if( i % 2 == 0):
#         continue
#     print(i)
#     i += 1


# str = "149162536"
# for char in str :
#     print(char)
# else:
#     print("Loop is ended")    

# str = "apne college"

# for char in str :
#     if(char == 'o'):
#         break
#     print(char)


# num = [ 1,4,9,16,25,36,49,64,81,100]
# for el in range(1,5,2) :

    
#     print(el)

# for i in range(3, 100, 1):
#     print(i)


# for i in  range(1,101):
#  print(i)

# for el in range(10):
#     pass                                                              #pass

# # print("hihhiihiih") 
# # n = 78
# # sum = 0
# # for i in range( n+1):
# #     sum += i

# #     print(sum)
# # i=1
# # while i <= n:
# #     sum += i
# #     i += 1 
# # print(i)    

# # countValue = "Vansh dhiman"
# # a = countValue.count("a")
# # print(a)

# # countVelue = "vansh dhiman"
# # target = 'a'
# # countOf = 0
# # for el in countVelue:
# #     if el == target:
# #         countOf += 1
# # print(countOf)        
    
# # def sum(a, b):
# #     b = a+b
# #     print(b)

# # a =5
# # b = 4
# # sum(a, b)
# print(57+71+64+68+46+58+48)
# print(64+55+87+75+29+25+30+25)
# a = 390
# b = 412
# # b = 55
# # c = 87
# # d = 75
# # e = 29+25
# # f = 30+25
# def calcu(b):
#     sum = b
#     avg = sum/6
#     print(avg)
#     return avg

# calcu(b) 


# print(412/600*100)


# def cal(a, b):
#     print(a*b)
#     return a*b

# # cal(2,)



# cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennnai"]
# print(cities[0], end="")
# print(cities[4])

# def printl(list):
#     print(len(list))

# printl(cities)    
# #


# age = input()
# type(age)



# a = 10
# b = 10
# print(a is b)
# print(a == b)


# a = 250
# b = 250
# print(a == b)
# x = 500
# y = 500
# print(x is y)

# if"Ai":
#     print("yes")

# data = [10, 20, 30, 40, 50, 50 ]

# for x in data:
#     print(x)

# for i in  range(1,10,2):
#     print(i)

# i = 1
# while i <= 3:
#     print(i)
#     i += 1

# for i in range(1,4,1):
#     print(i)    



def positive(data) :
    result = []
    for num in data:
        if num > 0:
            result.append(num)
    return result        

data = [3, -1, 0, 5, -2, 7, 0, 9]
print(positive(data))