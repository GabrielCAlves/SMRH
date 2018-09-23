from lib.get_coordinates import get_coordinates
from lib.get_multiplier import get_multiplier
from lib.get_threshold import get_threshold
from lib import files
import time
import os

#############################################################################
#############################################################################
#############################################################################
### Set variable paths: #####################################################
#############################################################################

# Absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

# Absolute path to multiplier file
MULTIPLIER_PATH = PATH + '/data/multiplier.p'

# Absolute path to threshold value file
THRESHOLD_PATH = PATH + '/data/threshold.p'

# Absolute path to coordinates file
COORDINATES_PATH = PATH + '/data/coordinates.p'

# Absolute path to times list file
TIMES_PATH = PATH + '/server/static/data/times.p'

# Absolute path to readings list file
READINGS_PATH = PATH + '/server/static/data/readings.p'

# Absolute path to last digit file
DIGITS_PATH = PATH + '/server/static/data/digits.p'

#############################################################################
#############################################################################
#############################################################################
### Do the following if executed by user: ###################################
#############################################################################

if __name__ == '__main__':
    # Enter 's' to skip
    choice = input('Deseja pular as coordenadas? [s/n] ')
    if(choice == 's' || choice == 'S'):
        # Get and save crop coordinates
        get_coordinates(COORDINATES_PATH)

    # Enter 's' to skip
    choice = input('Deseja pular o multiplicador? [s/n] ')
    if(choice == 's' || choice == 'S'):
        # Get and save multiplier
        get_multiplier(MULTIPLIER_PATH)

    # Enter 's' to skip
    choice = input('Deseja pular o threshold? [s/n] ')
    if(choice == 's' || choice == 'S'):
        # Get and save threshold
        get_threshold(THRESHOLD_PATH)

    # Get current time and date
    times = [time.strftime('%H:%M')]

    # Get reading
    readings = [int(input("Leitura: "))]

    # Get digit
    digits = [int(str(readings)[-len(str(MULTIPLIER))])]

    # Create times and readings lists and last_digit file
    files.write_it(TIMES_PATH, times)
    files.write_it(READINGS_PATH, readings)
    files.write_it(DIGITS_PATH, digits)

#############################################################################
#############################################################################
#############################################################################
#############################################################################
### Define global variables: ################################################
#############################################################################

# Multiplier for readings
MULTIPLIER = files.read_it(MULTIPLIER_PATH)

# Threshold value
THRESHOLD = files.read_it(THRESHOLD_PATH)

# Crop coordinates
COORDINATES = files.read_it(COORDINATES_PATH)

# Times list
TIMES = files.read_it(TIMES_PATH)

# Readings list
READINGS = files.read_it(READINGS_PATH)

# Digits list
DIGITS = files.read_it(DIGITS_PATH)
