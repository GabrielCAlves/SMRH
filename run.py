import smrh
import time
import glob
import os

# Get absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

# Get current time
time = time.strftime('%H:%M')

# Take a picture
smrh.get_picture()

# Find last file
list_of_files = glob.glob(PATH + '/smrh_app/static/images/*.png')
latest_file = max(list_of_files, key=os.path.getctime)

# Run tesseract
digit = int(smrh.run_tesseract(latest_file))
