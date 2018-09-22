from picamera import PiCamera
from PIL import Image
import pytesseract
import pickle

# Take a picture and save it
def get_picture(picture):
    # take picture and store
    camera = PiCamera()
    camera.rotation = 180
    camera.capture(picture)
    camera.close()

# Run OCR - Tesseract
def run_tesseract(PATH, picture):
    # Open image
    img = Image.open(filename)

    # Open crop coordinates
    filename = PATH + '/smrh_app/static/data/coordinates.p'
    with open(filename, 'rb') as file:
        coord = pickle.load(file)

    # Crop image
    cropped = img.crop(coord)

    # Apply threshold
    thresh = 100
    fn = lambda x : 255 if x > thresh else 0
    final_image = cropped.convert('L').point(fn, mode='1')

    # OCR
    return pytesseract.image_to_string(final_image, config='-psm 10 nobatch digits')

# Update values
def update_values(PATH, digit, last_digit, last_reading):
    # Get multiplier
    filename = PATH + '/smrh_app/static/data/multiplier.p'

    with open(filename, 'rb') as file:
        multiplier = pickle.load(file)

    # Test conditions
    if last_digit == 9:
        if digit == 0:
            return last_reading + multiplier
        else:
            return last_reading + (last_digit - digit) * multiplier
    else:
        return last_reading + (digit - last_digit) * multiplier
