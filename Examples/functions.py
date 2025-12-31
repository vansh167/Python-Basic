# def greet():
#     print("Hello Data Science",)
# greet()    




# def greet(name):
#     print("Hello", name)
# greet("Vansh")    

# def add(a,b):
#     return(a+b)


# result = add(5,5)

# print(result)
# def classify(n):
#     if n > 0 :
#         return "Positive"
#     elif n < 0 :
#         return "Negative"
#     else :
#         return "zero"
    
    
# print(classify(22))


# def countp(data):
#     count = 0
#     neg = 0
#     for d in data:
#      if d > 0:
#         count += 1
#     return count    
    
# nums = [3, -1, 5, 0, 7]
# print(countp(nums))

# def guess(data):
#         if data > 0:
#             return "EVEN"
#         elif data < 0:
#               return "odd"
# print(guess(2)) 
# print(guess(-3))        


# def negative(neg):
#     count = 0
#     for n in neg:
#         if n < 0:
#             count += 1
#     return count
# nums = [3, -1, 5, 0, 7]        
# print(negative(nums))         



# def check(num):
#     count = 0
#     for n in num:
#         if n == 0:
#             break
#         if n > 0 and n % 2 == 0:

#          count += 1
#     return count

    
# nums = [4, 6, -2, 0, 8]
# print(check(nums))
    



# =======================================================


# def check(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# print(check(24444))

# def check(num):
#     count = 0
#     for n in num:
#         if n > 0:
#          count += 1
#     return count    
# data = [1,2,3,4,5,-5,-6,-7,-5]
# print(check(data))

# def find_max(nums):
#     max_num = nums[0]
#     for n in nums:
#         if n > max_num:
#             max_num = n
#     return max_num
# data = [3, 8, 1, 6]
# print(find_max(data))
   
# def check(nums):
#     count = 0
#     for n in nums:
#         if n == 0:
#             continue
#         if n % 2 != 0:
#             count += 1
#     return count

    
# nums = [1, 3, 0, 5, 0, 7]

# print(check(nums))                 




# day 2 of fubctiuon==============================================================

# def sign(num) :
#     if num > 0:
#         return "Positive"
#     elif num < 0:
#             return "Negative"
#     else: 
#         return "Zero"        






def check(nums):
     pos = 0
     neg = 0
     for n in nums:
          if n > 0:
               pos += 1
          elif n < 0:
               neg += 1
     return pos, neg


p, n = check([3, -1, 5, -2, 0])
print(p, n)
                    