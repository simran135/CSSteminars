
#KEYWORDS IN PYTHON SHOULDNT BE USED AS VARIABLES NAMES
#TUPLE/LIST INDEXING
#SCOPE OF FUNCTION/VARIABLE BINDINGS
#BINDING TO A TUPLE (FUNCTION THAT RETURNS MULTIPLE VALUES)


############################
#######  FUNCTIONS #########
############################
print("----------------")
print("Functions in Python:")

def f():
    print("hello how are u today")
    return 5

def add(x, y):
    return x + y

# is this a valid function?
# def mystery(l[i], l[j]):
#     return l[i] + l[j]

# is this a valid function?
def mystery(smiley, i):
    return smiley + i

mystery(5, 6)

#MIGHT NEED TO BE TAKE OUT
def multipleValues(a, b, c):
    return a, b, c

a = multipleValues(1,2,3)
print(a)
print(a[0])

############################
##########  TYPES ##########
############################
print("----------------")
print("Some basic types in Python:")
print(type(2))           # int
print(type(2.2))         # float

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
########  IF ELSE ##########
############################

print("----------------")
print("IF STATEMENTS\n")

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

# What do these print?
l = ["1", "9", "10"]
if l[1] < l[2]:
   print (l[1], "<", l[2])
else:
   print (l[1], ">", l[2])

if True:
    print("is True true boys?...it seems so")

if False:
    print("Entered if statement")

# SHORT CIRCUITING

# What would these print?
print("illegal druggggzzz" if True else 1/0)

def yes():
    return True

def no():
    return False

def crash():
    return 1/0 # crashes!

print(no() and crash()) 
print(crash() and no()) 
print(yes() and crash()) 


#andalso, orelse, and, or

############################
####### OPERATORS ##########
############################
print("----------------")



############################
####### ERRORS #############
############################





