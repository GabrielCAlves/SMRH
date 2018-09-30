from lib.run_tesseract import run_tesseract
from lib.update_values import update_values
from lib.get_picture import get_picture
from datetime import datetime
from lib import files
import pickle
import cnf

# Get current time
CURRENT_TIME = datetime.now().strftime('%H:%M')

# CURRENT_DATE = datetime.now().strftime('%y-%b-%d_%H:%M')
# PICTURE_PATH = cnf.PATH + '/server/static/images/' + CURRENT_DATE + '.png'

# picture saving PATH
PICTURE_PATH = cnf.PATH + '/server/static/images/last_picture.png'

all_digits = []

# Run 3 times
for x in range(3):
    # Take a picture
    get_picture(PICTURE_PATH)

    # Run tesseract
    CURRENT_DIGIT = int(run_tesseract(cnf.PATH, PICTURE_PATH, cnf.COORDINATES, cnf.THRESHOLD))
    all_digits.append(CURRENT_DIGIT)

# Find value
if all_digits[0] == all_digits[1]:
    CURRENT_DIGIT = all_digits[0]

elif all_digits[1] == all_digits[2]:
    CURRENT_DIGIT = all_digits[1]


# Update values
CURRENT_READING = int(update_values(cnf.MULTIPLIER, CURRENT_DIGIT, cnf.DIGITS[-1], cnf.READINGS[-1]))

# Append lists
cnf.TIMES.append(CURRENT_TIME)
cnf.READINGS.append(CURRENT_READING)
cnf.DIGITS.append(CURRENT_DIGIT)

# Write in files
files.write_it(cnf.TIMES_PATH, cnf.TIMES)
files.write_it(cnf.READINGS_PATH, cnf.READINGS)
files.write_it(cnf.DIGITS_PATH, cnf.DIGITS)
