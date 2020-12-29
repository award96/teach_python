

def test_function(a, b, c, d=4):
    """
    sums the input

        ARGS: a (int or float)
              b (int or float)
              c (int or float)
        Optional:
              d (int or float)
        RETURNS:
            a + b + c + d
    
    """
    result = a + b + c + d
    return result
    return "once a return happens, the function ends. This string will never be returned"

def does_nothing(x):
      # a function doesn't have to do anything, 
      # but it at least has to say pass to let
      # the computer know. 
      pass

sum1 = test_function(1, 2, 3)
sum2 = test_function(1, 2, 3, d=5)
print("\n\n5-more_functions\n")
print(f"sum1 = {sum1}")
print(f"sum2 = {sum2}")
does_nothing(sum1)

def returns_nothing(primitive, array):
      """
      Only primitives are immutable. arrays are not primitives. 
      Therefore arrays are mutable

      ARGS:
            primitive - a primitive object
            array - a list object
      RETURNS:
            None
      """
      primitive = 5
      array[0] = 5 # the 0th index of array is now equal to 5

array = [sum1, sum2] # the fact that 'array' is the same name used in 'returns_nothing' has
                     # no effect. It can be considered good practice to keep naming consistent, because functions
                     # have local scope so they wont mess anything up.
print('\n')
print(f"array before returns_nothing:\n{array}")
returns_nothing(sum1, array)
print(f"sum1 = {sum1} ... unchanged")
print(f"array after returns_nothing:\n{array}")

def uses_global_variable():
      """
            A function can reference variables outside of itself, 
            but code outside of a function cannot reference variables inside a function
      """
      print('\n')
      print(f"this function can still reference variables outside of itself: {array}")
