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


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def update_age(self, new_age):
#         self.age = new_age

#     def show(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# s1 = Student("Vansh", 20)
# s2 = Student("Bhawika", 20)

# s1.update_age(21)
# s1.show()

# s2.show()



# Task of this question

# class Bank:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def update_balance(self, new_balance):
#         self.balance += new_balance
#     def account(self):
#         print("Name:",self.name)  
#         print("Balance:",self.balance) 
# a = Bank("Vansh",10000000000)
# a.account()          
# a.update_balance(10000000500) 
# a.account()          



# Starting((((((((((((((( Encapsulation))))))))))))))) (Data Protection) now — this is real OOPS and very important for interviews + MNC coding style.===============================


# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Deposit amount must be positive")
#             return
#         self.balance += amount 

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdraw amount must be positive")       
#             return
#         if amount> self.balance:
#             print("Insufficient balance")
#             return
#         self.balance -= amount

#     def show(self):
#         print("Name:",self.name)    
#         print("Balance:", self.balance)
#         print("----------")

# b = BankAccount("Bhawika",1000)
# b.show()
# b.deposit(500)
# b.show()
# b.withdraw(200)
# b.show()
