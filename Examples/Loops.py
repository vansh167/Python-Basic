count = 1
while  count <= 5 : 
    print("hello world")
    count += 1
# print(count)
# ========================================
# reverce number 
i = 10
while i >= 1 :
    print(i)
    i -= 1
# ======================================== Questions 
# print number 1 - 100.

num = 1
while num <= 100:
    print(num)
    num += 1



i = 3
v = 1
while v <= 10:
    print(i, "X", v, "=", i * v)
    v += 1


# Q4 print name numbers  in list to simple 
  

nums = [1,4,9,16,25,36,49,64,81,100]
heros = ["Ironman","Thor","Hulk","CaptainAmerica","BlackWidow ","Hawkeye"]
idx = 0
while idx < len(heros):
    print(heros[idx])
    idx += 1  


# Q4
#  
# 
nums = (1,4,9,16,25,36,49,64,81,100, 36)
x = int(input("Enter a number to search :"))

i = 0 #initionalization
while i < len( nums):
    if(nums[i] == x):
        print("Found at index ", i)
    i += 1 

# ==========================================Break keyword 
while i <= 5:
    print(i)
    if( i == 3):
      break
    i += 1
#  ========================================== Continue keyword

i = 0
while i <= 5:
    if( i % 2 == 0):
        continue
    print(i)
    i += 1


# =============================================================================== FOR LOOP 
nums = [1,4,9,16,25,36]
for el in nums :
    print(el)
else:
    print("Loop is ended")    



str = "149162536"
for char in str :
    print(char)
else:
    print("Loop is ended")        


#  ===================================== Range method 
# 
for i in range(3, 100, 3):  #start , end , step
    print(i)   