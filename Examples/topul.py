string = [1,2,3]
a = string.copy()
a.reverse()
if(string == a[::-1]):
    print("Palindrom")
else :
    print("Not a Palindrom")

# ================================== Palindrom
string = [1,2,3]
string2 = [1,2,3]
string2.reverse()
if(string == string2[::-1]):
    print("Palindrom")
else :
    print("Not a Palindrom")


# ================================= Questions
movies = []
movie1 = input("Enter your favourite movie :")
movie2 = input("Enter your favourite movie :")
movie3 = input("Enter your favourite movie :")
 
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)


print(movies)

# =============================

marks = [23,23,43,12,55]

print(marks[0:2])               # slicingg

marks.append(99)                #append
marks.sort()                    #sorting

print(marks)
student = ["vansh", 35,]
print(student[1])

# ===================================== 

grade = ("A", "B", "C", "A", "D", "A", "A",)
a = grade.count("A")
print(a)



# ===================================== 

grade = ["A","F","B","C","E","D"]
grade.sort()
print(grade[2:4])
# # ============================================tuple=

tup = (92,1,3,1,3,4,5)
print(tup.count(1))
