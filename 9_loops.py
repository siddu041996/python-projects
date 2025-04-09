''' while loop '''

# count = 1
# while (count<=5):
#     print(count)
#     count+=1
# print(count)

# print numbers
# i = 5
# while (i>=1):
#     print(i)
#     i-=1
# print(i)

# Multiplication of tables
# n=int(input("Enter number :"))
# i=1
# while (i<=10):
#     print(n*i)
#     i+=1
# print("end")

# Print numbers from list

# num=[1,3,9,16,25,36,49,64,81,100]  # num[0],num[1],..........,num[len(index)-1]
# index=0
#traverse
# while index < len(num):
#     print(num[index])
#     index += 1


# Find the number from _test tuple

''' [
    Break : used to terminate the loop
     continue : terminates the current iyeration execution and continue with next iteration of the loop.
 ] '''

# And usage of break

# num=(1,3,9,16,25,36,49,64,81,100)
# x=int(input("enter value to search: "))
# i=0
# while i < len(num):
#     if(x == num[i]):
#         print("number found at : ",i)
#         break
#     else:
#         print("Finding")
#     i += 1
# print("end of loop")

# Usage of continue

# i = 0
# while i <= 5:
#     if (i == 3):
#         i+=1
#         continue
#     print(i)
#     i+=1

# odd numbers using while and continue

# i=0
# while i < 10:
#     if(i%2 == 0):
#         i+=1
#         continue
#     print(i)
#     i+=1

# Even numbers using while and continue

# i=0
# while i < 10:
#     if(i%2 != 0):
#         i+=1
#         continue
#     print(i)
#     i+=1


''' Loops in python:

Loops are used for sequential traversal. for traversing list, tuple,strings etc'''


# for loop

# numbers = [1,4,6,87,34,45] #list
# for val in numbers:
#     print(val) 

# fruits = {"mango","apple","watermelon"}  #set
# for val in fruits:
#     print(val) 

# string = "namma bengaluru"
# for char in string:
#     print(char)

# for with optional else

# string1 = "namma bengaluru"
# for char in string1:
#     print(char)
# else:
#     print(string1)

# find number     (linear search)
# num = [1,3,5,7,45,67,78,34,23,2,2]

# x=int(input("enter number to search: "))

# idx = 0

# for el in num:
#     if (el == x):
#         print("number found at idx", idx)
#     idx += 1

''' range : range function returns a sequence of numbers, starting from 0 (default) and increament by one (default) 
and stop before a specified number'''

# range (start?,stop?,step?)  
# end number not get print

# for val in range(10, 30, 2):  # range(start,stop,step)
#     print(val)

# for val in range(10): #range(stop)
#     print(val)

# for val in range(2,10): #range(start,stop)
#     print(val)

#multiplication of tables

# n = int(input("enter value of table: "))

# for i in range(1,11):
#     print(n*i)

''' 
pass statement
pass is a null statement that does npthing, it is usedas a placeholder for future code
'''

# for el in range(5):
#     #empty
#     pass
# print("future work")

# sum of n numbers

# n = int(input("enter number: "))

# sum = 0

# for i in range(1, n+1):
#     sum += i
#     print(i)
# print("total sum is :", sum)

# multiplication using while

# n = int(input("enter number: "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("total sum is :", sum)

# factorial number  ( factorai of 5 = 1*2*3*4*5)

# n = int(input("enter number: "))
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("total fact is :", fact)

# factorial number using for loop  ( factorai of 5 = 1*2*3*4*5)

# n = int(input("enter number: "))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
#     i += 1
# print("total fact is :", fact)

# for i in range(5):
#     print(i)

count = 0
while count > 5:
    print(count)
    count += 1
print(count)