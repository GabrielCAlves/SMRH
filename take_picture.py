from picamera import PiCamera
import cnf

# Initialize camera
camera = PiCamera()
camera.rotation = 180

# Take picture and save it
camera.capture(cnf.PATH + '/test_picture.png')

# Close camera
camera.close()
