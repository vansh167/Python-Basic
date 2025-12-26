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
for row in range(5):                #(0,0,0,0,5)
    for col in range(row + 1):           #(1,2,3,4)
        print("*",end="")
    print()    

n = 5
for i in range(n, 0, -1):
    print("*" * i)
  

data = [10, 20, 30]
for i, value in enumerate(data):
    value = value * 2
    print(i, value)



n = 5

# upper half
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2*i + 1))

# lower half
for i in range(n-2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2*i + 1))
