# Arithmetic expressions - numbers, operators, expressions

print 3, -1, 3.14159, -2.8

# numbers - two types, an integer or a decimal number
# two corresponding data types int() and float()

print type(3), type(3.14159)
print type(3.0)


# we can convert between data types using int() and float()
# note that int() takes the "whole" part of a decimal number and doesn't round
# float() applied to integers is boring

print int(3.14159), int(-2.8)
print float(3), float(-1)


# floating point number have around 15 decimal digits of accuracy
# pi is 3.1415926535897932384626433832795028841971...
# square root of two is 1.4142135623730950488016887242096980785696...

# approximation of pi, Python displays 12 decimal digits

print 3.1415926535897932384626433832795028841971

# appoximation of square root of two, Python displays 12 decimal digits

print 1.4142135623730950488016887242096980785696

# arithmetic operators
# +		plus		addition
# -		minus		subtraction
# *		times		multiplication
# /		divided by 	division
# **    power		exponentiation

print 1 + 2, 3 - 4, 5 * 6, 2 ** 5

# Division in Python 2
# If one operand is a decimal (float), the answer is decimal

print 1.0 / 3, 5.0 / 2.0, -7 / 3.0

# If both operands are ints, the answer is an int (rounded down)

print 1 / 3, 5 / 2, -7 / 3


# expressions - number or a binary operator applied to two expressions
# minus is also a unary operator and can be applied to a single expression

print 1 + 2 * 3, 4.0 - 5.0 / 6.0, 7 * 8 + 9 * 10

# expressions are entered as sequence of numbers and operations
# how are the number and operators grouped to form expressions?
# operator precedence - "please excuse my dear aunt sallie" = (), **, *, /, +,-

print 1 * 2 + 3 * 4
print 2 + 12


# always manually group using parentheses when in doubt


print 1 * (2 + 3) * 4
print 1 * 5 * 4

#number of feets in 13 miles
print 13*5280
#number of seconds in 7 hours , 21 minutes and 37 seconds 
print 7*60*60 +21*60+37
#perimeter of a rectangle
print 2*(4+7)
#area of the rectangle
print 4*7
#perimeter of the cirle
print 2*3.14*8
# area of the circle
print 3.14*(8**2)
#print value of dollar
print 1000*((1+0.01*7)**10)
#print string
print "My name is "+" Joe "+" Warren"
print "Joe Warren is "+str(52)+" years old."
#print the distance between two points
print ((2-5)**2+(2-6)**2)**0.5




