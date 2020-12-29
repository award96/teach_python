"""
	iterating is going over the values of an object in order. Many objects are iterable in different ways.
"""


test_list = ["apple", "banana", "orange", 5]

def range_iter(lst):
	print("\n\nrange_iter function:\n")
	print(f"len(lst) = {len(lst)}")
	for i in range(len(lst)):
		print(f"i = {i}")
		print(f"lst[i] = {lst[i]}")

def val_iter(lst):
	# value iteration is less verbose, but you don't have a reference to what index you're on
	# look up "enumerate python" to see a hybrid of the two. It doesn't add anything new, just 
	# can be used by preference for readability.
	print("\n\nval_iter function:\n")
	for val in lst:
		print(f"val = {val}")
print("First we create a list, then we iterate through it.")
print(type(test_list))
print(f"test_list = {test_list}")
range_iter(test_list)
val_iter(test_list)