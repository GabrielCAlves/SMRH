import pickle
from lib import files

# Get multiplier
def get_multiplier(MULTIPLIER_PATH):
    # Enter multiplier
    multiplier = int(input("Multiplicador de leitura: "))

    # Save and pickle
    files.write_it(MULTIPLIER_PATH, multiplier)
