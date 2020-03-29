
############################
#######  FUNCTIONS #########
############################

def f():
    print("hello how are u today")
    return 5

def add(x, y):
    return x + y

# is this a valid function?
def mystery(l[i], l[j]):
    return l[i] + l[j]

# is this a valid function?
def smiley(l[i], l[j]):
    return l[i] + l[j]


############################
##########  TYPES ##########
############################

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
if (grade < 60)
    print("F")
elif (grade < 70)
    print("D")
elif (grade < 80)
    print("C")
elif (grade < 90)
    print("B")
else:
    print("YOU GOT AN A!!!")

# One line if statement
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

# Short circuiting
print("illegal druggggzzz" if True else 1/0)


#andalso, orelse, and, or

############################
####### OPERATORS ##########
############################




############################
####### ERRORS #############
############################





