from smrh_lib.setup import get_coordinates, get_multiplier
import os

# Get absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

choice = int(input("1 - Coordenadas\n 2 - Multiplicador "))

if choice == 1:
    # Get coordinates
    get_coordinates(PATH)

elif choice == 2:
    # Get multiplier
    get_multiplier(PATH)
