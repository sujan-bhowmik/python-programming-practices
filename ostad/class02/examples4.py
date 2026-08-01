city = "Dhaka"
print(f"city id     : {id(city)}")   # id() returns the object's memory identity

city = "Chittagong"                   # label now points to a NEW object
print(f"city id     : {id(city)}")    # different id than before

x = 1000
y = x                                 # y now points to the same object as x
print(f"x id: {id(x)}  |  y id: {id(y)}  |  same object? {x is y}")

a, b, c = 10, 20, 30
a, b = b, a                           # the classic swap, no temp variable
print(f"after swap -> a={a}, b={b}")