from smrh_lib.setup import get_coordinates, get_multiplier
import pickle
import time
import os

# Get absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

# Get coordinates
get_coordinates(PATH)

# Get multiplier
get_multiplier(PATH)

filename1 = PATH + '/smrh_app/static/data/times.p'
filename2 = PATH + '/smrh_app/static/data/readings.p'
filename3 = PATH + '/smrh_app/static/data/last_digit.p'

# Get current time and date
times = [time.strftime('%H:%M')]

# Get reading
readings = [int(input("Leitura: "))]

# Get digit
digit = int(input("Dígito: "))

# Create times and readings lists and last_digit file
with open(filename1, 'wb') as file:
    pickle.dump(times, file)
    file.close()

with open(filename2, 'wb') as file:
    pickle.dump(readings, file)
    file.close()

with open(filename3, 'wb') as file:
    pickle.dump(digit, file)
    file.close()
