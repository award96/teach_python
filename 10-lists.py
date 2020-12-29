"""
    Lists are the most common non-primitive. They represent lists of things, ie [0, 2, 4, 6, 8]
    They are mutable
    Objects have methods. These are things that can be done by or to the object, by the object.
    Object methods are almost always written 
    object.method()
    the exception being the len(object) method which returns the length of the list or string.

    The main 'methods' lists have:
    len(list) - the number of values in the list
    list.append(x) - increase the length of the list by one. Put x at the end of the list.
    list[index] - index is an integer. Return the value from that location in the list

    lists are indexed 0 to len(list) - 1
    [0, 1, 2, 3] -> a list of length 4. list[1] returns 1.
"""
lst = [0, 1, 2, 3]
print(f"\ntype(x) = {type(lst)}")
print(f"lst = {lst}")
print(f"lst[0] = {lst[0]}")
print(f"lst[1] = {lst[1]}")
print(f"lst[-1] = {lst[-1]}") # negative indices go through the list in reverse. -1 is the last value. -2 is the second to last value
