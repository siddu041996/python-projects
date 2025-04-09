#variables

str1="sid"
str2="ravi"

num1=12
float2=3.4

#list = collection of multiple datatypes in square brackets (mutable)

first_list = [str1,"devops",float2,67]
print(first_list)

#tuple = collection of multiple datatypes in round brackets (immutable)
first_tuple = (str1,"devops",float2,67)
print(first_tuple)

#Dictionary (key-value pair) in curly brackets
first_dictionary = {"name":"sidd", "float":8.9, "tuple":[str1,"devops"]}
print(first_dictionary)

print(type(first_dictionary))
print(type(first_tuple))
print(type(first_list))

#Boolean
x= True
y= False
print(x)
print(y)
print(type(x))
print(type(y))