from lib.get_coordinates import get_coordinates
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

# Do the following if executed by user
if __name__ == '__main__':
    # Get and save crop coordinates
    get_coordinates(COORDINATES_PATH)

# Defines coordinates for image cropping
with open(COORDINATES_PATH, 'rb') as file:
    COORDINATES = pickle.load(file)
