from lib.get_coordinates import get_coordinates
from lib import file
import time
import os

#############################
## Define global variables ##
#############################

# Absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

# Define multiplier value for readings
MULTIPLIER = 10

# Define threshold value for image binarization
THRESHOLD_VALUE = 100

# Absolute path to coordinates file
COORDINATES_PATH = PATH + '/data/coordinates.p'

# Absolute path to times list file
TIMES_PATH = PATH + '/server/static/data/times.p'

# Absolute path to readings list file
READINGS_PATH = PATH + '/server/static/data/readings.p'

# Absolute path to last digit file
DIGITS_PATH = PATH + '/server/static/data/digits.p'

#############################################

# Do the following if executed by user
if __name__ == '__main__':
    # Get and save crop coordinates
    get_coordinates(COORDINATES_PATH)

    # Get current time and date
    times = [time.strftime('%H:%M')]

    # Get reading
    readings = [int(input("Leitura: "))]

    # Get digit
    digits = [int(str(readings)[-len(str(MULTIPLIER))])]

    # Create times and readings lists and last_digit file
    file.write_it(TIMES_PATH, times)
    file.write_it(READINGS_PATH, readings)
    file.write_it(DIGITS_PATH, digits)

#############################################

# Crop coordinates
COORDINATES = file.read_it(COORDINATES_PATH)

# Times list
TIMES = file.read_it(TIMES_PATH)

# Readings list
READINGS = file.read_it(READINGS_PATH)

# Digits list 
DIGITS = file.read_it(DIGITS_PATH)
