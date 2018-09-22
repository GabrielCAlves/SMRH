import pickle

# Get coordinates for image cropping
def get_coordinates(PATH):
    # Enter coordinates
    x0 = int(input("x0: "))
    y0 = int(input("y0: "))
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))

    # Save and pickle
    coord = (x0, y0, x1, y1)
    filename = PATH + '/smrh_app/static/data/coordinates.p'

    with open(filename, 'wb') as file:
        pickle.dump(coord, file)
        file.close()

# Determine multiplier
def get_multiplier(PATH):
    # Enter multiplier
    mult = int(input("Multiplicador de leitura: "))

    # Save and pickle
    filename = PATH + '/smrh_app/static/data/multiplier.p'

    with open(filename, 'wb') as file:
        pickle.dump(multiplier, file)
        file.close()
