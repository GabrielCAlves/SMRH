from picamera import PiCamera
from PIL import Image
import pytesseract
import time
import os

PATH = os.path.dirname(os.path.realpath(__file__))

def get_picture():
    date = (time.strftime('%y-%b-%d_%H:%M'))
    picture = PATH + '/smrh_app/static/images/' + date + '.png'

    camera = PiCamera()

    camera.rotation = 180
    camera.capture(picture)
    camera.close()
