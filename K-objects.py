"""
    Objects are by far the best way to program, because you can define strict methods that change the properties of the object, and prevent 
    bad use of your object. If you had something that was best represented by multiple variables, why not wrap those variables up in an object?
    You have more flexibility for how you can represent something once you no longer have to worry about keeping track of all its peices.

    Just like there is a fundamental idea behind functions, there is a fundamental idea behind objects

    Functions:

        Defined Acceptable Inputs --> Function --> Defined Acceptable Outputs

    under this paradigm you don't have to worry about how a function works, whether it will break, etc. 
    You just have to know two things about it - input & output

    Objects:

        Abstract Representation (the idea)      || wall behind which the user does not see ||       Actual implementation (the code)

    An object usually represents something besides a collection of variables and methods. It could be a special type of list, a customer's information, a dataset.
    The user does not need to know how the dataset structures each column, and assigns it a name. The user just has to call "dataset.list_columns()".

    The way you keep that wall up is by holding your "representation invariant". That is, the set of statements which if True, your actual implementation of the 
    object will correctly abstractly represent the real thing. IE for a "customer" object

    Rep Invariant:
        name: str
        transaction_history: list of Transaction objects
        phone_number: str
        unpayed_flag: int - has to be 0 or 1

    If the phone-number rep breaks, and a phone number is stored as an int - then the method "Customer.text_reminder(appointment_date)"
    would send an HTTP request to 3rd party robo-texting software with incorrectly formatted data. Now you're relying on that 3rd party software to
    be well designed to at least warn you the request didn't work.
    These sorts of cascading errors leaking in are what eat up time. Writing a class is mostly boilerplate, 
    once you get used to it, it takes no time at all.


    Here's how you define an object. They are called Classes.

"""

# let's make a variation on Python's built in list Class, except we make it immutable. 
# That way if we pass it into a function, that function can't change the values within the list.
# This is a useful exercise because thinking about how lists work behind the scenes 
# let's you understand how to use them better

class Array: # name the object
    def __init__(self, values=None): # when you create a new Array, this is the method that is called
        # The underscores before and after denote it as a 'special' reserved name. Examples of other such names include
        # __main__, __repr__, __str__, __iter__, __next__ and more

        # any function inside a class that starts with an underscore cannot be called outside of the class.
        # this prevents users from doing something they shouldn't 
        print("initializing array...")

        # if the user instantiated the array with incorrect values, tell them.
        if type(values) != list or type(values) != None:
            # raise creates an Error. You can even define your own error classes.
            raise ValueError(f"Type(values) = {type(values)}\nInstantiate the array with type list or None")

        # What python's list class does is create space in memory for the values, and keep track of where in memory
        # each index is. Python's built in stuff is heavily optimized and we could never approach its speed without coding it
        # in the language Python is written in, C
        # So let's just keep things simple

        # Note we use the double underscore to denote that users should not access these variables.
        # If they access our variables directly we cannot guarantee 
        # Though because python is a more free-spirited programming language, 
        # the following code would work outside the class.

        # x = Array([0,1,2,3])
        # print(x.__values)


        if values: # None is equivalent to false
            self.__values = values
        else:
            self.__values = []

        self.__length = len(self.values)


        # what does self mean?
        """
            self refers ot the specific instance of the object. In other words if I write
            x = Array(), x is the self.

            Now no matter where I am in the class methods I write below, self.__values always refers to the
            same thing
        """
    def __check_index(self, index):
        """
        Throws an error if the index does not correspond to an array element.
        By making this a separate method we can just call it whenever.
            ARGS:
                index - anything at all
            THROWS:
                ValueError - if index is not a natural number
                IndexError - if index is outside the array
        """
        # These inputs cannot be processed
        if type(index) != int:
            raise ValueError("Index must be of type int")
        if index < 0 :
            raise ValueError("Index must be greater than 0")
        if index >= self.__length:
            raise IndexError("IndexError, Index is too large")

    def add(self, new_val, index=None):
        if index:
            self.__check_index(index)
            self.__values[index] = new_val
        else:
            self.__values.append(new_val)

    def get(self, index):
        """
            Returns the value at the specified index

            Args:
                index: int - greater than 0, less than the length of the array
            Returns:
                value: the value stored in that index
        """
        # These inputs cannot be processed
        if type(index) != int:
            raise ValueError("Index must be of type int")
        if index < 0 :
            raise ValueError("Index must be greater than 0")
        if index >= self.__length:
            raise IndexError("IndexError, Index is too large")

        this_val = self.__values[index]
        # to guarantee that our array is immutable, we must copy down
        # any non-primitive values. 
        # list.copy(deep=True) returns a list with a different spot in memory.
        # deep=True means that if the values of the list are also objects, those are
        # copied as well.

        # The way our Array class is currently written, we cannot guarantee immutability. we have broken
        # our rep invariant. This is because if a value in the list were say, a dict (dictionary), it would not copy
        # the object, but rather it would copy a pointer to that object, while still referring to the same object.

        # How would you fix this? Create an if statement for every Class? 
        # That wouldn't work, there must be hundreds of widely used classes
        # Code like this would not solve the problem, it would only pass the same pointer along further:
        #   x = this_val
        #   return x
        if type(this_val) == list:
            return this_val.copy(deep=True)
        if type(this_val) == Array:
            return this_val.copy()
        return this_val
    
    def copy(self):
        new_list = []
        for index in range(self.__length):
            new_list.append(self.get(index))
        return new_list

    def length(self):
        return self.__length # we don't have to copy it because it's a primitive