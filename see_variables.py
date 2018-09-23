from lib import file
import cnf

times = file.read_it(cnf.TIMES_PATH)
readings = file.read_it(cnf.READINGS_PATH)
last_digit = file.read_it(cnf.LAST_DIGIT_PATH)

print(times)
print(" ")
print(readings)
print(" ")
print(last_digit)
