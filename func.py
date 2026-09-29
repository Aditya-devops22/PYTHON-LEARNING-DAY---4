def greet():
    print("Hello Adi")

greet()

#funtion with multiple lines

def student_info():
    print("Name: Adi")
    print("Course: Computer Science")
    print("Year: 4th")

student_info()

#why functions are useful
# Instead of dumping everything into one giant program:
# you can organise it:

def deposit():
    pass

def withdraw():
    pass

def check_balance():
    pass


def show_menu():
    pass

show_menu()
deposit()
withdraw()
check_balance()

#Function with a parameters

def greet (name):
    print("Hello", name)

greet ("Adi")
greet("shruu")

#Multiple Parameters

def introduction(name,age):
    print("Name:",name)
    print("Age:",age)

introduction("Adi",22)

# Function for Addition

def add():
    a = 10
    b = 20
    print(a + b)

add()

def add(a,b):
    print(a + b)

add (40,32)
add(54,32)
add(12,67)


#3 func with argument
def greeting(name):
    print("Name:",name)

greeting("Adi") #adi is argument

#return arguments

def add (a,b):
    return a + b

result = add(3,6)
print(result)

def greet(name = "User"):
    print("Hello",name)

greet()
greet("Shruu")


def info(name,age):
    print(name,age)

info(age = 21 , name = "adi")

#variable- length arguments
#1.*arg(multiple values)

def add(*nums):
    total= 0
    for n in nums:
        total = total + n
    return total
    
print(add(1 ,2 ,3 ,4 ,5))

   #2. **kwarge(key-value)

def display(**data):
    print(data)

display(name= "Shruu", age = 20)


#scope
   #1.local scope

def test():
    x = 10
    print(x)

test()

    #2.Global scope

x = 10 

def show():
    print(x)

show()

# lambda func

cube = lambda x: x*x*x
print(cube(5))

# Recursion
def factorial(n):
    if (n == 0 or n ==1):
        return 1
    else :
        return n *factorial(n-1)
    
print(factorial(5))


def fibonacci(n):
    if (n == 0 or n ==1):
        return 1
    else:
        return fibonacci (n-1)+ fibonacci(n-2)

print(fibonacci(9))


