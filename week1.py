'''
Summary:

1) Introduce functions (similar to functions in math)
    - Describe input/output
    - Difference between a print and return statement
    - Variable assignment: doesn't matter what the name 
        of the variable is in the input
2) Types and operators: 
    - Arithmetic	+, -, *, /, //, **, %
    - Take a short quiz
3) Logical operators and short circuiting
	- and, or, not
    - Truth tables
    - Follow up with examples in the section
'''

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

b = add(1,3)

############################
###  TYPES & OPERATORS #####
############################

# Category	Operators
# Arithmetic	+, -, *, /, //, **, %, - (unary), + (unary)
# Relational	<, <=, >=, >, ==, !=
# Assignment	+=, -=, *=, /=, //=, **=, %=, <<=, >>=
# Logical	and, or, not


# Arithmetic	+, -, *, /, //, **, %, - (unary), + (unary)
print("----------------")
print("Some basic types in Python:")
print(type(2))           # int
print(type(2.2))         # float
print(type(2.0))         # what type?

print("The / operator does 'normal' float division:")
print(" 5/3  =", ( 5/3))
print()
print("The // operator does integer division:")
print(" 5//3 =", ( 5//3))
print(" 2//3 =", ( 2//3))
print("-1//3 =", (-1//3))
print("-4//3 =", (-4//3))

# a = (a // b) * b + a % b 
print(" 6%3 =", ( 6%3))
print(" 5%3 =", ( 5%3)) 
print(" 2%3 =", ( 2%3))
print(" 0%3 =", ( 0%3)) 
print("-4%3 =", (-4%3))
print("-4%3 =", (-16%3))
print(" 3%0 =", ( 3%0))

# Relational	<, <=, >=, >, ==, !=
# Assignment	+=, -=, *=, /=, //=, **=, %=, <<=, >>=

# Logical	and, or, not
# Swetha's PDF for boolean explanation
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
########## QUIZ ############
############################

print("----------------")
print("QUIZ TIME:\n")

# Do the types match? Will these all compile?
print(3 * 2)
print(3 * "abc") 
print(3 + 2)
print("abc" + "def") #string concatenation
print(3 + "def")

print("Precedence:")
print(2+3*4)  #14 = 2 + 12
print(5+4%3)  #6 = 5 + 1
print(2**3*4) #

print()

print("Associativity:")
print(5-4-3)   

############################
# BOOLEAN SHORT-CIRCUITING #
############################

# and statement
def yes():
    return True

def no():
    return False

def crash():
    return 1/0 # crashes!

print(no() and crash()) 
print(crash() and no()) 
print(yes() and crash()) 

# or statement
def yes():
    return True

def no():
    return False

def crash():
    return 1/0 # crashes!

print(yes() or crash()) # Works!
print(crash() or yes()) # Crashes!
print(no() or crash())








