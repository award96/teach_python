import numpy as np # 'as' renames it to something more readable
import pandas as pd
import matplotlib.pyplot as plt
import K_objects as immutable

"""
    You always want to put imports at the top of your program. What you're doing is importing other Python files into your python file.
    You get their functions, classes, and even variables. If a function is called "func" in the file you imported, to call it you would write:

    import pythonFile

    pythonFile.func()

    Python looks in your 
"""
# numpy, pandas, and matplotlib are all extremely common when crunching numbers
# numpy is used for numerical methods.
# pandas is pythons version of excel.
#   A pandas.Dataframe object works a lot like an excel sheet, though the class method names and uses take awhile to get used to
# matplotlib.pyplot is used for plotting. It's actually really hard to use and I don't like it. But it's considered standard.

x = immutable.Array()