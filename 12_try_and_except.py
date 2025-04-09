class MyCustomException(Exception):
    pass

try:
    raise MyCustomException("An error occurred")
except MyCustomException as e:
    print(e)
