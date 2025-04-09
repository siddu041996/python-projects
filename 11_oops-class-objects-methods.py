# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Alice"))

# squares = [x**2 for x in range(10)]
# print(squares)

try:
    result = 10 / 2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful")
finally:
    print("This will always execute")
