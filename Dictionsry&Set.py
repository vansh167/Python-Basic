info = {
    "key" : "value",
    "hi" : {
    "name" : "Vansh",
    "age" : 19,
    "marks" : [99,45,67]}
}
print(info)

# METHODS

print(info.keys())
print(info.values())
print(info.items())
print(info.get("key"))
print(info.update(new_key = "new_value"))


# ======================================================= SET ================
myset = {1,2,3,4,5,5,5,5,5}
# Methods================================================     ================

myset.add(6)
myset.remove(3)
# myset.clear()
myset.pop()
print(myset)


collection = {"hello", "hi", "hey", "hello", "hi"} 
print(collection.union())                                                      #union
print(collection.intersection())                                               #intersection

# ========================================================= Questions
# store the following word in a python dictoinary 

words = {
    "table ": "A piece of furniture with a flat top and one or more legs, providing a level surface on which objects may be placed.",
   " cat" : "animal"
}
print(words)

# =========================================================================

subject = {
    "pyhon","java","c++","html","css","javascript","java"
    "c++","html","css","javascript","java"
}
print(subject)  # sets do not allow duplicate values

# ====================================================================

subjects = {}
x = int(input("Enter phy"))
subjects.update({"phy": x})

x = int(input("Enter chem"))
subjects.update({"chem": x}) 

x = int(input("Enter math"))
subjects.update({"math": x})

print(subjects)
# =====================================================================
values = { 
    ("float",9.0),
    ("int", 9)
}
print(values)

