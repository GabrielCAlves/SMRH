from lib.run_tesseract import run_tesseract
from lib.update_values import update_values
from lib.get_picture import get_picture
from picamera import PiCamera
from datetime import datetime
from PIL import Image
import pytesseract
import pickle
import cnf
import os

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
with open(cnf.TIMES_PATH, 'rb') as file:
    times = pickle.load(file)

with open(cnf.READINGS_PATH, 'rb') as file:
    readings = pickle.load(file)

with open(cnf.LAST_DIGIT_PATH, 'rb') as file:
    last_digit = pickle.load(file)

last_reading = readings[-1]

# Update values
reading = update_values(cnf.MULTIPLIER, digit, last_digit, last_reading)

# Append lists
times.append(current_time)
readings.append(reading)

# Write in files
with open(cnf.TIMES_PATH 'wb') as file:
    pickle.dump(times, file)
    file.close()

with open(cnf.READINGS_PATH, 'wb') as file:
    pickle.dump(readings, file)
    file.close()

with open(cnf.LAST_DIGIT_PATH, 'wb') as file:
    pickle.dump(digit, file)
    file.close()
