"""
	Variables are necessary to keep track of data, objects, whatever. Each variable
	in Python has a name and a pointer. The name is how you call the variable ('a' in the lines below)
	and the pointer 'points' to the object in memory. The pointer can change as you reassign the variable (as I do below)

	This is important: A variable has a pointer, not an object. If the object the pointer references changes, the next time 
	you use the variable it will have changed as well. Some objects are called Primitives, and are immutable. This means that
	when you set x = 5, you cannot do anything to '5' to change it. You can only reassign the variable, ie x = 6
"""

a = 5
print(a)
a = "applesauce"
# 5 has not changed, the pointer associated with a has changed
print(a)
def variable_test():
	# a variable defined inside of a function is 'local scoped'
	# this means that a = True only inside of this function. Outside a
	# continues to equal whatever it did equal.
	a = True

# a = applesauce
print(a)
variable_test()
# a still equals applesauce because the function cannot change variables outside of its scope
print(a)

# this is how to print things in a more organized way
print('\n') # \n creates a new line regardless of where you put it
print(f"{a}") # f before a string makes it possible to put variables inside brackets within the string
# here's how you might use that
print(f"\nThis string has much better formatting\na = {a}")
print("""
	\n
	A multiline string for printing!
""")