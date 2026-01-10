# 🧠 WHAT IS OOPS? (NO THEORY)

# Simple meaning:

# OOPS helps you group data + functions together.

# Till now you wrote:

# Data → list / dict

# Logic → function

# class students:
#     def say(self):
#         print("Hello, I am a student!")

# s = students()         #object
# s.say()


# class phones:                                 #Class  1>.
#     def mobile(stt):                          #Object 2>.
#         print("This is a mobile phone")
# v = phones()
# v.mobile()



# =====================================================================    __init__ ================================================

# class Phone:
#     def __init__ (self, brand, price):
#         self.brand = brand
#         self.price = price

#     def info(self):
#         print(self.brand, self.price)    
# p1 = Phone("Samsung:",20000)
# p1.info()


# Task 1>
# class Data:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print("Name:",self.name)   
#         print("Age:",self.age) 
#         print("--------------------")

# d1 = Data("Aniket", 20)    
# d2 = Data("Sonali:", 24)
  
# d1.info()
# d2.info()


# 🔥 Updating Object Data (VERY IMPORTANT)

class Students:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def update_age(self, new_age):
        self.age = new_age

    def show(self):
        print("Name:",self.name)  
        
        print("Age:",self.age)    

b1 = Students("Vansh",20)
    
b1.update_age(21)
b1.show()

