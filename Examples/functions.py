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


def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check(24444))
