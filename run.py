from smrh_lib.functions import get_picture, run_tesseract, update_values
import pickle
from datetime import datetime
import os
from picamera import PiCamera
from PIL import Image
import pytesseract

# Get absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

try:
    # Get current time and date
    time = datetime.now().strftime('%H:%M')
    date = datetime.now().strftime('%y-%b-%d_%H:%M')

    # picture saving PATH
    picture = PATH + '/smrh_app/static/images/' + date + '.png'

    # Take a picture
    camera = PiCamera()
    camera.capture(picture)
    camera.close()

    # Run tesseract
    # Open image
    img = Image.open(picture)

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
    digit = pytesseract.image_to_string(final_image, config='-psm 10 nobatch digits')

except:
    if os.path.exists(picture):
        os.remove(picture)

else:
    filename1 = PATH + '/smrh_app/static/data/times.p'
    filename2 = PATH + '/smrh_app/static/data/readings.p'
    filename3 = PATH + '/smrh_app/static/data/last_digit.p'

    # Open files
    with open(filename1, 'rb') as file:
        times = pickle.load(file)

    with open(filename2, 'rb') as file:
        readings = pickle.load(file)

    with open(filename3, 'rb') as file:
        last_digit = pickle.load(file)

    # Update values
    reading = update_values(PATH, digit, last_digit, readings[-1])

    # Append lists
    times.append(time)
    readings.append(reading)

    # Write in files
    with open(filename1, 'wb') as file:
        pickle.dump(times, file)
        file.close()

    with open(filename2, 'wb') as file:
        pickle.dump(readings, file)
        file.close()

    with open(filename3, 'wb') as file:
        pickle.dump(digit, file)
        file.close()
