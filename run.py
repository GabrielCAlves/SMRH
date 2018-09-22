from smrh_lib.functions import get_picture, run_tesseract, update_values
import pickle
from datetime import datetime
import os
from picamera import PiCamera
from PIL import Image

# Get absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

try:
    # Get current time and date
    time = datetime.now().strftime('%H:%M')
    date = datetime.now().strftime('%y-%b-%d_%H:%M')

    # picture saving PATH
    global picture
    picture = PATH + '/smrh_app/static/images/' + date + '.png'

    # Take a picture
    camera = PiCamera()
    camera.rotation = 180
    camera.capture(picture)
    camera.close()

    # Run tesseract
    digit = int(run_tesseract(PATH, picture))

except:
    if os.path.exists(picture)
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

    break;
