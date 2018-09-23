from lib import file
import cnf

times = file.read_it(cnf.TIMES_PATH)
readings = file.read_it(cnf.READINGS_PATH)

print(times)
print(" ")
print(readings)
