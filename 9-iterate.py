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
	for val in lst:
		print(val)
print(type(test_list))
range_iter(test_list)
val_iter(test_list)