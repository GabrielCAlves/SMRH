import cnf
from lib.files import write_it
from see_variables import see

times = cnf.TIMES
readings = cnf.READINGS
digits = cnf.DIGITS

del times[-1]
del readings[-1]
del digits[-1]

write_it(cnf.TIMES_PATH, times)
write_it(cnf.READINGS_PATH, readings)
write_it(cnf.DIGITS_PATH, digits)

see()
