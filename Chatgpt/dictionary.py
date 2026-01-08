# def count(data):
#     return {"total":len(data)}
# print(count([1,3,2,4,4]))



# data = [1,2,3,4,5,56,2,2,3,4,2]                                 # len useage 
# a = len(data)
# print(a)



# def count(data):
#     return len(data)

# data=[1,2,3,4,54]    
# print(count(data))



# def two():
#     return 5,9
# a,b = two()
# print(a,b)



# def total():
#     return  {"Total:":1}

# print(total())    


# def dic(data):
#     even = 0
#     odd = 0

#     for n in data:
#         if n == 0:
#             continue
#         if n % 2 == 0 :
#             even += 1
#         else:
#             odd += 1
#     return {
#         "even": even,
#         "odd": odd
#     }        

# print(dic([1,2,3,445,5,5,56,6,6,6,3]))




# def count(num):
#     total = 0
#     neg = 0
#     for n in num:
#         if n > 0:
#             total += 1
#         elif n < 0:
#             neg += 1    
#     return {"total":total,
#             "Negative":neg}
        
# # key = [1, -2, 3, 0, 5]


# print(count([1, -2, 3, 0, 5]))
 

# def count(nums):
#     total = 0
#     for n in nums:
#         if n / 2 == 0:
#              total += 1
#     return n          
        

# key = [1, -2, 3, 0, 5]     

# print(count(key))



def count(num):
    total = 0
    neg = 0 
    for n in num:
        if n > 0:
            total += 1
        elif n < 0:
            neg += 1
    return{
        "Positive": total,
        "Negative":neg
    }           
print(count([1,2,4,3,5,4,-2,-3,-4,-5])) 
