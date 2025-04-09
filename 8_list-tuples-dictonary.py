# List -- built-in datatype -Mutable
# tuple -- built-in datatype - immutable

# str="siddu"
# print(str[0])
# str[0]="N"
# print(str)

# ===================================
# student = ["siddu",23,"cse"] 
# print(student[1])
# student[0]="bhargav"
# print(student)
# ========================================
# slicing

# marks=[98,23,34,56,67,23]
# print(marks[1:4])  #positive slicing
# print(marks[-3:-1])  #negetive slicing

# ===================================

# List Methods
# ========================
# list =[2,23,12,24,56]

# print(list.append(9))
# print(list.sort())
# print(list.sort(reverse=True))
# print(list)

# ========================
# list=["mango","apple","lemon"]
# list=["z","l","d","u"]
# list.sort()
# #list.reverse()
# list.insert(0,"s")  #insert value at index
# print(list)  
# list.remove("l")  #remove first occurance of elements
# print(list)
# list.pop(2)  #remove elements at index 
# print(list)
# ===========================================

#Tuples

# tup=(12,23,14,56)
# print(type(tup))
# print(tup)

# =======================================

# list1 = [1,2,3,2,1]
# list1 = [1,2,3,4,5]

# copy_list1=list1.copy()
# copy_list1.reverse()


# if (copy_list1 == list1):
#     print("palindrome")
# else:
#     print("Not Palindrome")

# ===========================================

# Dictionary
# Mutable
#key value fairs
#can tuples be value in dictionary (bcz they are unmutable), but not list

# info = {
#     "name" : "siddu",
#     "subject" : ["python","java"],
#     "classes" : {"youtube" : ["apnacollege","durgasoft"],"udemy": 23},
#     "range" : 80,
#     "completion" : "half",
#     ("python","java") : "classes",
#     ("python","java",".net") : "classes"
# }
# print(info)

# info["languages"] = ["english","hindi"]

# print(info["classes"]["youtube"])
# print(type(info))
# ============================================
# # Empty dictonary
# dict = {}
# print(dict)
# print(type(dict))

# Dictionory Methods:
# dict.keys()
# dict.values()
# dict.update()
# print(info.items())
# dict.get()
# =================================================

# Set in Python
# ================
# collection of the unordered items
# Each element in the set must be unique and immutable
#set is mutable but elements unmutable
# duplicate value not get print (repeated elemnts stored only once)

# set = {1,2,2,2,3,"world","new","hi"}

# print(set)
# print(type(set))
# =============================
# empty set

# # Empty dictonary
# dict = set()
# print(dict)
# print(type(dict))
# ==============================

# set methods

# set.add(3) adds an element
# set.remove(3) removes the element
# set.clear() empties the set
# set.pop() remove random element
# set.union() combines both set values and return new set
# set.intersection()  combines common values and give new set
# ===========================

# set1= {9,2,3,2,3,4}
# set2 = {2,3,1,3,2,4,5,6}

# print(set2.union(set1))
# print(set2.intersection(set1))
# ========================================