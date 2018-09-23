from picamera import PiCamera
import os

# Absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

# Initialize camera
camera = PiCamera()
camera.rotation = 180

# Take picture and save it
camera.capture(PATH + '/test_picture.png')

# Close camera
camera.close()
