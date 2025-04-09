'''
Function
Block of statements that performs a specific task'''
'''
def funct_name(param1,param2):    #def means function definition with parameters
    #some work
    return val
    
func_name(arg1,arg2...) #function call ; arguments as values

'''

# def sum(a,b):
#     add=a+b
#     return add

# value=sum(3,4)
# print(value)

# ====================

# def calc_sum(a,b):
#     return a+b

# sum=calc_sum(223434,3434233247)

# print(sum)
# =========================

# def print_hello():
#     print("hello")

# print_hello()
# ==========================

# def print_hello():
#     print("hello")

# output=print_hello()
# print(output) #output is none bcz there is no return value
# ======================

# def calc_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     return avg

# average = calc_avg(10,10,10)
# print(average)
# ===============================
'''
Built-in functions
ex: print() range() len() etc............

user defined functions
that we are going to create
'''
'''
Default parameters
Assigning a default value to parameter, which is used when no argument passed
'''
# def calc_sum(a=10,b=2):
#     return a+b
# value=calc_sum()
# print(value)
# ========================

# Print the elements in single line

# movies = ["ironman","strangerthings","america","shaktiman","KGF"]

# def print_list(list):
#     print(len(list))
#     for item in list:
#         print(item,end=" ") 

# print_list(movies)

# =========================

# Factorial using function

# 1.with loops
# n=5
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# print(fact)
# ========================
# 2. with function

# def calc_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
# factorial=calc_fact(4)
# print(factorial)
# ===========================

# convert $ to rupees

# def converter(usd_val):
#     inr_val= usd_val * 83
#     print(usd_val, "USD=", inr_val, "INR")

# converter(1) 

# n = int(input("Enter a number: "))
# def even_odd(n):
#     rem = n % 2
#     if rem == 0:
#         print("EVEN NUMBER")
#     else:
#         print("ODD NUMBER")
# even_odd(n)

'''
Recursion :
recursion is function call itself
'''

# def show (n):
#     if n > 10:  # base case to stop recursion
#         return
#     print(n)
#     show(n+1)
#     # print("end")  #call stack

# show(6)

# ===========================
# def show(n):
#     if(n==0):              
#         return
#     print(n)
#     show(n-1)
#     print("end")    #call stack
# show (4)
# ===============================

# factorial of n numbers
# =============================
# n = 4
# def fact(n):
#     if (n == 1 or n == 0):   #base condition or stopping condition
#         return 1
#     return fact(n-1) * n 

# factorial = fact(n)
# print(factorial)
# ======================================

# calculate sum of numbers

# n = 10
# def calc_sum(n):
#     if( n == 0):   #base condition or stopping condition
#         return 0
#     # print(n)
#     return calc_sum(n-1) + n
# sum = calc_sum(n)
# print(sum)
# ================================

# recursion of list items

# def print_list(list, idx=0):
#     if (idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# drinks = ["water","juice","rum","gin","wisky"]
# print_list(drinks)
# =========================

# def order(item, *, quantity=1):
#     return f"{quantity} x {item}"

# print(order("apple"))
# print(order("banana", quantity=3))
# print(order("mango", quantity=5))

# =========================================

# def get_coordinates():
#     return 10, 20

# x, y = get_coordinates()
# print(x, y)

# ====================================
# add = lambda x, y: x + y
# print(add(2, 9))

# ====================================

# def apply(func, value):
#     return func(value)

# def square(x):
#     return x * x

# print(apply(square, 4))

# =============================

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))
# ======================

# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("hello"))  # Output: "olleh"
# =========================

# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("racecar"))
# =================================

