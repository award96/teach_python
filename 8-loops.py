def for_loop(n):
	print(type(range(n)))
	print(range(n))
	for i in range(n):
		print(i)
		
def while_loop(n):
	while n > 0:
		print(n)
		n -= 1
for_loop(5)
while_loop(5)