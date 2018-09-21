from picamera import PiCamera
from PIL import Image
import pytesseract
import pickle
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

    # Open crop coordinates
    filename = PATH + '/smrh_app/static/data/coord.p'
    with open(filename, 'rb') as file:
        coord = pickle.load(file)

    # Crop image
    cropped = img.crop(coord)

    # Aplicar threshold
    thresh = 100
    fn = lambda x : 255 if x > thresh else 0
    final_image = cropped.convert('L').point(fn, mode='1')

    # OCR
    return pytesseract.image_to_string(final_image, config='-psm 10 nobatch digits')
