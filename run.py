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

# Take a picture
get_picture(PICTURE_PATH)

# Run tesseract
CURRENT_DIGIT = run_tesseract(PICTURE_PATH, cnf.COORDINATES, cnf.THRESHOLD)

# Update values
CURRENT_READING = update_values(cnf.MULTIPLIER, CURRENT_DIGIT, cnf.DIGITS[-1], cnf.READINGS[-1])

# Append lists
cnf.TIMES.append(CURRENT_TIME)
cnf.READINGS.append(CURRENT_READING)
cnf.DIGITS.append(CURRENT_DIGIT)

# Write in files
files.write_it(cnf.TIMES_PATH, cnf.TIMES)
files.write_it(cnf.READINGS_PATH, cnf.READINGS)
files.write_it(cnf.DIGITS_PATH, cnf.DIGITS)
