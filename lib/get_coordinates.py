import pickle
from lib import files

# Get coordinates for image cropping
def get_coordinates(COORDINATES_PATH):
    # Enter coordinates
    x0 = int(input("x0: "))
    y0 = int(input("y0: "))
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))

    # Save and pickle
    coordinates = (x0, y0, x1, y1)
    files.write_it(COORDINATES_PATH, coordinates)
