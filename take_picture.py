from picamera import PiCamera
import cnf

# Initialize camera
camera = PiCamera()

# Take picture and save it
camera.capture(cnf.PATH + '/test_picture.py')

# Close camera
camera.close()
