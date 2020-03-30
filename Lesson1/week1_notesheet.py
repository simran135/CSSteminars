############################
####  FUNCTIONS INTRO ######
############################
print("----------------")
print("Functions in Python:")

def f():
    print("hello how are u today")
    return 5

def void_function():
  print("this function doesn't return anything")

def add(x, y):
    return x + y

add(1,3)

############################
###  TYPES & OPERATORS #####
############################

# Category	Operators
# Arithmetic	+, -, , /, //, *, %, - (unary), + (unary)
# Relational	<, <=, >=, >, ==, !=
# Assignment	+=, -=, *=, /=, //=, **=, %=, <<=, >>=
# Logical	and, or, not


# Arithmetic	+, -, , /, //, *, %, - (unary), + (unary)
print("----------------")
print("Some basic types in Python:")
print(type(2))           # int
print(type(2.2))         # float
print(type(2.0))         # float

print("The / operator does 'normal' float division:")
print(" 5/3  =", ( 5/3)) # 1.6666666666666667
print()
print("The // operator does integer division:")
print(" 5//3 =", ( 5//3)) # 1
print(" 2//3 =", ( 2//3)) # 0
print(" -4//3 =", (-4//3)) # -1 (Rounds down towards negative infinity)


# a = (a // b) * b + a % b 
print(" 6%3 =", ( 6%3)) # 0
print(" 5%3 =", ( 5%3)) # 2
print(" 2%3 =", ( 2%3)) # 2
print(" 0%3 =", ( 0%3)) # 0
print(" 3%0 =", ( 3%0)) # ZeroDivisionError

# Logical	and, or, not
print(type(2 < 2.2))     # bool (boolean)
print(bool(0))           # False
print(bool(5))           # True
print(bool(1))           # True

print(type("hello"))     # str
print(type("2.2"))       # str (string or text)

print("Some builtin constants:")
print(True)
print(False)
print(None)

print("And some more constants in the math module:")
import math
print(math.pi)
print(math.e)


############################
###  SHORT CIRCUITING ######
############################

# and statement
def yes():
    return True

def no():
    return False

def crash():
    return 1/0 # crashes!

print(no() and crash()) # False
print(crash() and no()) # crashes!
print(yes() and crash()) # crashes!

# or statement
def yes():
    return True

def no():
    return False

def crash():
    return 1/0 # crashes!

print(yes() or crash()) # Works!
print(crash() or yes()) # Crashes!
print(no() or crash()) # crashes!

############################
##### IF ELSE INTRO ########
############################

# this prints 3 equals 3
if (3 == 3):
    print("3 equals 3")
else:
    print("3 doesn't equal 3")

# Reminder: 3=3 is illegal 
# (you can't assign a value to an int, 
# you can only assign a value to a variable such as x = 3)

grade = 74
if (grade < 60):
    print("F")
elif (grade < 70):
    print("D")
elif (grade < 80):
    print("C")
elif (grade < 90):
    print("B")
else:
    print("YOU GOT AN A!!!")

# the code above prints C
# if you have an elif statement, you can only go into one case
# before exiting the if-elif-else block