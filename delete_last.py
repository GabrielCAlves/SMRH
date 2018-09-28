import cnf
from see_variables import see

see()

del cnf.TIMES[-1]
del cnf.READINGS[-1]
del cnf.DIGITS[-1]

see()
