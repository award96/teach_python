"""
    int - Integers, whole numbers
    float - decimal numbers (includes whole numbers ie 3.0)
    str - strings, text
    bool - True or False

    Primitives are the building blocks for objects. They are immutable, which means that you cannot change
    the value of a primitive, only what primitive your variable is pointing to. This is incredibly useful, because
    you can guarantee that x will still equal 3 after you run a function that takes x as a parameter. The same is not true for 
    objects. When you give a function an object it may be changed.

    type() is a function built into python that returns the type of the object.

"""


x = 5
print(type(x)) # int
y = 5.5
print(type(y)) # float
s = "text"
print(type(s)) # str
boolean = False
print(type(boolean)) # bool

# calling the int() method on a float will chop off the decimal. It does not round, it just throws away the decimal
j = int(y) 
# calling float() on an int will add a decimal of .0 to the end of the number
k = float(x)
print(j)
print(k)

num = "5"
# the int() method can also parse strings
num = int(num)
print(type(num)) # int
print(num)