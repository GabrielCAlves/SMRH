from lib.get_coordinates import get_coordinates
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

# Absolute path to multiplier file
MULTIPLIER_PATH = PATH + '/data/multiplier.p'

# Absolute path to times list file
TIMES_PATH = PATH + '/server/static/data/times.p'

# Absolute path to readings list file
READINGS_PATH = PATH + '/server/static/data/readings.p'

# Absolute path to last digit file
LAST_DIGIT_PATH = PATH + '/server/static/data/last_digit.p'

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
    last_digit = str(readings)[-len(str(MULTIPLIER))]

    # Create times and readings lists and last_digit file
    with open(TIMES_PATH, 'wb') as file:
        pickle.dump(times, file)
        file.close()

    with open(READINGS_PATH, 'wb') as file:
        pickle.dump(readings, file)
        file.close()

    with open(LAST_DIGIT_PATH, 'wb') as file:
        pickle.dump(last_digit, file)
        file.close()

#############################################

# Defines coordinates for image cropping
with open(COORDINATES_PATH, 'rb') as file:
    COORDINATES = pickle.load(file)
