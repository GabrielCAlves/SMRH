from smrh_lib.functions import get_picture, run_tesseract
import time
import glob
import os

# Get absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

# Get current time
time = time.strftime('%H:%M')
date = time.strftime('%y-%b-%d_%H:%M')

# picture saving PATH
picture = PATH + '/smrh_app/static/images/' + date + '.png'

# Take a picture
get_picture(picture)

# Find last file
list_of_files = glob.glob(PATH + '/smrh_app/static/images/*.png')
latest_file = max(list_of_files, key=os.path.getctime)

# Run tesseract
digit = int(run_tesseract(PATH, latest_file))
