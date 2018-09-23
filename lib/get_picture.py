from picamera import PiCamera

# Take a picture and save it
def get_picture(PICTURE_PATH):
    # Initialize camera
    camera = PiCamera()

    # Take picture and save it to path provided
    camera.capture(PICTURE_PATH)

    # Close camera
    camera.close()
