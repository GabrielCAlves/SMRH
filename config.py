from smrh_lib.functions import get_coordinates, get_multiplier

# Get absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

choice = int(input("1 - Coordenadas\n 2 - Multiplicador "))

if choice == 1:
    get_coordinates(PATH)

elif choice == 2:
    get_multiplier(PATH)
