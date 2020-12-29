"""
		an if statment executes the block of code indented below it only if the statement equals True
"""
if True:
    print("\nTrue")

if False:
    print("\nFalse")

print("\nthis statement is not indented and will be printed regardless")

if False == False:
    print("\n== is a logical operator")
    x = 3 == 3
    print(f"\nx = {x}")

if type("string") != int:
    print("\n!= is the logical operator that means 'is not equal to'")

if not False:
    print("\nnot False is the same as True")

if 2==2.0 or 's' == 'S' and True:
    print("\n2 equals 2.0 BUT s does not equal S.\nSince the logical operator was 'or', only one needed to be True")
    print("if either statment to the left or right of 'and' was false, the whole statment would be false")

