"""
	A function is a reusable piece of code. There is so much to talk about with functions,
	so let's start with this...

	A function has an input and an output. When this is well defined, the function can be used
	anywhere it is needed without much thought. This is what makes a function "Good" - predictability.

	Well documented code includes a text block inside each function that defines what it does and its limitations.

"""

def funct():
	"""
	Returns the string 'hello world'
		ARGS: none
		RETURNS: str - hello world
	"""
	return "hello world"

# print calls funct(), which returns the string 'hello world', which is then printed to the terminal.
print(funct())

# print(f"funct() returns:\n{funct()}"") # a more informed and formatted version of the same print statement
