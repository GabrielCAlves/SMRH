from picamera import PiCamera
from PIL import Image
import pytesseract
import time
import os

# Get absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

# Take a picture and save it
def get_picture():
    # Get current time
    date = (time.strftime('%y-%b-%d_%H:%M'))
    picture = PATH + '/smrh_app/static/images/' + date + '.png'

    camera = PiCamera()
    camera.rotation = 180
    camera.capture(picture)
    camera.close()

# Run OCR - Tesseract
def run_tesseract(picture):
    # Open image
    img = Image.open(filename)
