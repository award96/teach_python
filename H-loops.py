def for_loop(n):
	print("\n\nlet's see what a for loop is\n")
	print(f"type(range(n)) = {type(range(n))}")
	print(f"range(n) = {range(n)}")
	for i in range(n): 
		# I've never used range outside of this purpose, though I'm guessing it has other uses
		print(i)
		
def while_loop(n):
	"""
		while loops are more flexible than for loops, but you have to do more boiler plate.
		A common use of while loops is using boolean variables to control the flow of logic, 
		ie the basic idea would be
			while x:
				x = do_something(x)
	"""
	print("\n\nlet's see what a while loop is\n")
	while n > 0:
		print(f"n = {n}")
		n -= 1
for_loop(5)
while_loop(5)