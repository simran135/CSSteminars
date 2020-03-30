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


print("----------------")
print("QUIZ TIME:\n")

# Do the types match? Will these all compile?
print(3 * 2)
print(3 * "abc")
print(3 + 2)
print("abc" + "def")
print(3 + "def")

print("Precedence:")
print(2+3*4)  # prints 14, not 20
print(5+4%3)  # prints  6, not 0 (% has same precedence as *, /, and //)
print(2**3*4) # prints 32, not 4096 (** has higher precedence than *, /, //, and %)

print()

print("Associativity:")
print(5-4-3)   # prints -2, not 4 (- associates left-to-right)

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









