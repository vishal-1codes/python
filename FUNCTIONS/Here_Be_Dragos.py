#If you have a function of your very own named sqrt and you import math, your function is safe: there is your sqrt and there is math.sqrt. If you do from math import *, however, you have a problem: namely, two different functions with the exact same name.

import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print(everything) # Prints 'em all!