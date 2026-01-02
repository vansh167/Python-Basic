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






# def check(nums):
#      pos = 0
#      neg = 0
#      for n in nums:
#          if n > 0:
#                pos += 1
#           elif n < 0:
#                neg += 1
#      return pos, neg


# p, n = check([3, -1, 5, -2, 0])
# print(p, n)
                    



# part 3> 

# def zero(nums):
#     for n in nums:
#         if n == 0:
#             return True
#         return False
    
# def check_data(nums):
#     even = 0
#     odd = 0

#     for n in nums:
#         if n % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#     return even, odd


# even, odd = check_data([1,2,3,4,5,6,7,8,9,-7,-6,-5,-4,-3,-2,-1])
# print("Even:", even)
# print("Odd:", odd)

# def find(check):
#     zero = 0
#     for c in check:
#         if c == 0:
#             zero += 1
#             break
#         return "Found"
#     else:
#         return "Not Found"
#     return zero
# zero = find([1,2,3,4,0,6,7,66,4,])
# print(zero)


# def find(nums):
#     for n in nums:
#         if n == 0:
#             return "Found"
#     return "Not Found"
# print(find([1, 2, 3, 4, 0, 6, 7]))
# print(find([1, 2, 3, 4, 6, 7]))

# def data(nums):
#     positive = 0
#     negative = 0
#     zero = 0

#     for n in nums:
#         if n > 0:
#             positive += 1
#         elif n < 0:
#             negative += 1
#         else:
#             zero += 1

#     return {
#         "positive": positive,
#         "negative": negative,
#         "zero": zero
#     }
# result = data([1,2,3,4,5,6,7,8,-6,-4,-3,-6,-5,0,0])
# print(result)

# DAY - 3===========================================

# nums = [3, -1, 5, 0, 7]
# for i in range(len(nums)):                           #============================================================ index for all numbers
#     print(i, nums[i])

# for n in nums:
#     print(n) 

# 🧠 PART 4: LIST vs TUPLE vs DICT (INTERVIEW MUST)
# Feature	List	Tuple	Dict
# Ordered	✅	✅	❌ (logical order)
# Changeable	✅	❌	✅
# Indexed	✅	✅	❌
# Key-based	❌	❌	✅
# DS usage	Raw data	Fixed output	Summaries



def get_positive_numbers(nums):
    positives = []

    for n in nums:
        if n > 0:
            positives.append(n)

    return positives
data = [3, -1, 0, 2, 3, 4, 6, 5, -2]
print(get_positive_numbers(data))
