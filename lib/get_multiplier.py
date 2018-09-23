import pickle
from lib import file

# Get multiplier
def get_multiplier(MULTIPLIER_PATH):
    # Enter multiplier
    multiplier = int(input("Multiplicador de leitura: "))

    # Save and pickle
    file.write_it(MULTIPLIER_PATH, multiplier)
