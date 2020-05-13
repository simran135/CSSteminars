#KEYWORDS IN PYTHON SHOULDNT BE USED AS VARIABLES NAMES
#TUPLE/LIST INDEXING
#SCOPE OF FUNCTION/VARIABLE BINDINGS
#BINDING TO A TUPLE (FUNCTION THAT RETURNS MULTIPLE VALUES)
#Look for things that say #QUESTION: to see if we are including this topic this week

############################
####  FLOAT COMPARISON #####
############################

'''
 Reminders from lesson 1:
 Int: an integer which is a number without a decmial point (ex. 1, -1, 3)
 Float: a member of the reals, has a decimal point (Ex. 2.0, 1.1, -3.409876)
 x = y : x is assigned the value that y has
 Boolean variables: True, False
 x == y : boolean expr, if x and y are the same then this evaluates to True
    otherwise it evaluates to False
'''

print(0.1 + 0.1 == 0.2)        # True, but...
print(0.1 + 0.1 + 0.1 == 0.3)  # False!
print(0.1 + 0.1 + 0.1)         # prints 0.30000000000000004 (uh oh)
print((0.1 + 0.1 + 0.1) - 0.3) # prints 5.55111512313e-17 (tiny, but non-zero!)

print("The problem....")
d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2)                # False (never use == with floats!)

print()
print("The solution...")
epsilon = 10**-10
print(abs(d2 - d1) < epsilon)  # True!

print()
print("Once again, using a useful helper function, almostEqual:")

def almostEqual(d1, d2):
    epsilon = 10**-10
    return (abs(d2 - d1) < epsilon)

d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2)            # still False, of course
print(almostEqual(d1, d2)) # True, and now packaged in a handy reusable function!

############################
########  IF ELSE ##########
############################

print("----------------")
print("IF STATEMENTS\n")

# if (this boolean expression evaluates to True):
#   this block of code gets executed

if True:
    print("true")

if False:
    print("false")

if (3 == 3):
    print("true")
else:
    print("false")

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

if (grade < 60):
    print("F")
if (grade < 70):
    print("D")
if (grade < 80):
    print("C")
if (grade < 90):
    print("B")
if (grade < 100):
    print("YOU GOT AN A!!!")

# ONE LINE IF STATEMENT

age = 15
print('kid' if age < 18 else 'adult')
print("illegal stuff" if True else 1/0)

# What do these print?
if ("9" > "10"):
    print("9 > 10")
else:
    print("9 < 10")

if True:
    print("is True true guys?...it seems so")

if False:
    print("Entered if statement")

############################
#######  FUNCTIONS #########
############################

'''
Vocab:
    - function name
    - parameters
    - arguments
    - function call
    - return value
    - return type
    - statement
    - expression
    - global variables
    - local variables
'''

y = 7

# Can you make the return type of this function a float? An int?
def functionName(x, z):
    result = x + z + y
    return result

print(functionName(1, 3))
print(functionName(2, 4))
print(functionName(True, False))

# What do these functions return?

def isEven(x):
    print("hey")
    return (x % 2 == 0)
    print("wassup")

print(isEven(5))
print(isEven(4))

#------------------------

def printing(y):
    print(y)

a = printing(1)
print(a)



# is this a valid function?
def mystery(i + j, x):
    return i + j + x

# is this a valid function?
def mystery(smiley, i):
    return smiley + i

mystery(5, 6)

# QUESTION: MIGHT NEED TO BE TAKE OUT
def multipleValues(a, b, c):
    return a, b, c

a = multipleValues(1,2,3)
print(a)
print(a[0])