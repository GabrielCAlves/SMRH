from smrh_lib.functions import get_picture, run_tesseract, update_values
import pickle
import time
import os

# Get absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

# Execute until ok
while True:
    try:
        # Get current time and date
        time = time.strftime('%H:%M')
        date = time.strftime('%y-%b-%d_%H:%M')

        # picture saving PATH
        picture = PATH + '/smrh_app/static/images/' + date + '.png'

        # Take a picture
        get_picture(picture)

        # Run tesseract
        digit = int(run_tesseract(PATH, picture))

    except:
        # Delete useless picture
        if os.path.exists(picture):
            os.remove(picture)

    else:
        filename1 = PATH + '/smrh_app/static/data/times.p'
        filename2 = PATH + '/smrh_app/static/data/readings.p'
        filename3 = PATH + '/smrh_app/static/data/last_digit.p'

        # If files do not exist, create them
        if !os.path.exists(filename1):
            with open(filename1, 'wb') as file:
                file.close()

        if !os.path.exists(filename2):
            with open(filename2, 'wb') as file:
                file.close()

        # Open files
        with open(filename1, 'rb') as file:
            times = pickle.load(file)

        with open(filename2, 'rb') as file:
            readings = pickle.load(file)

        with open(filename3, 'rb') as file:
            last_digit = pickle.load(file)

        # Update values
        reading = update_values(digit, last_digit)

        # Append lists
        times.append(time)
        readings.append(reading)

        # Write in files
        with open(filename1, 'wb') as file:
            pickle.dump(times, file)

        with open(filename2, 'wb') as file:
            pickle.dump(readings, file)

        with open(filename3, 'wb') as file:
            pickle.dump(digit, file)

        break;
