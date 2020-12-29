"""
	Functions can be treated just like objects, though they are quite different
	This is useful, but also dangerous. Functions are not objects, so while this 
	easy-breazy approach is useful for code readability, it can have damaging affects
	in a larger program where errors might hide.
"""

def a(n):
	
	if n == 5:
		# if n is even when given to this function, neither function will return anything. There will be an error.
		return n
	# return the function b evaluated for n + 1.
	# returning the result of another function is called recursion. Recursive solutions to problems often turn complicated
	# things into simple solutions
	return b(n+1)

def b(n):
	return a(n+1)

print(f"type(a) = {type(a)}")
print(f"a = {a}")
print(f"type(b) = {type(b)}")
print(f"b = {b}")

print(a(1))
"""
a(1) returns b(2) which returns a(3) which returns b(4) which returns a(5) which equals n (and n equals 5)
"""
#print(a(2)) # what happens when this function is run? What will the error be? What would happen if python didn't call this an error?
x = a
print(x(-1))