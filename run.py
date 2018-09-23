from lib.run_tesseract import run_tesseract
from lib.update_values import update_values
from lib.get_picture import get_picture
from datetime import datetime
from lib import file
import pickle
import cnf

# Get current time and date
current_time = datetime.now().strftime('%H:%M')
current_date = datetime.now().strftime('%y-%b-%d_%H:%M')

# picture saving PATH
PICTURE_PATH = cnf.PATH + '/smrh_app/static/images/' + current_date + '.png'

# Take a picture
get_picture(PICTURE_PATH)

# Run tesseract
digit = run_tesseract(PICTURE_PATH, cnf.COORDINATES, cnf.THRESHOLD_VALUE)

# Open files
times = file.read_it(cnf.TIMES_PATH)
readings = file.read_it(cnf.READINGS_PATH)
last_digit = file.read_it(cnf.LAST_DIGIT_PATH)
last_reading = readings[-1]

# Update values
reading = update_values(cnf.MULTIPLIER, digit, last_digit, last_reading)

# Append lists
times.append(current_time)
readings.append(reading)

# Write in files
file.write_it(cnf.TIMES_PATH, times)
file.write_it(cnf.READINGS_PATH, readings)
file.write_it(cnf.LAST_DIGIT_PATH, digit)
