def myFn():
    print("You have called my function")

# nothing is executed due to nothing being called
def add(x, y):
    z = x + y
    print(z)

# this calls the function, which causes it to work
myFn()
add(2, 3)
add(4, 7)

# changing values of x and y change the values inside of add()
a = 10
b = 20
add(a, b)
