from picamera import PiCamera
from PIL import Image
import pytesseract
import pickle

# Get coordinates for image cropping
def get_coordinates(PATH):
    # Enter coordinates
    x0 = int(input("x0: "))
    y0 = int(input("y0: "))
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))

    # Save and pickle
    coord = (x0, y0, x1, y1)
    filename = PATH + '/smrh_app/static/data/coordinates.p'

    with open(filename, 'wb') as file:
        pickle.dump(coord, file)
        file.close()

# Determine multiplier
def get_multiplier(PATH):
    # Enter multiplier
    mult = int(input("Multiplicador de leitura: "))

    # Save and pickle
    filename = PATH + '/smrh_app/static/data/multiplier.p'

    with open(filename, 'wb') as file:
        pickle.dump(multiplier, file)
        file.close()

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
def update_values(digit, last_digit):
    # Get multiplier
    filename = PATH + '/smarh_app/static/data/multiplier.p'

    with open(filename, 'rb') as file:
        multiplier = pickle.load(file)

    # Test conditions
    if last_digit == 9:
        if digit == 0:
            return multiplier
        else:
            return (last_digit - digit) * multiplier
    else:
        return (digit - last_digit) * multiplier
