from picamera import PiCamera
from PIL import Image
import pytesseract
import time
import os

def get_picture():
    date = (time.strftime('%y-%b-%d_%H:%M'))
