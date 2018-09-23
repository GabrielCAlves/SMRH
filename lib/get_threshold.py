import pickle
from lib import file

# Get threshold value
def get_threshold(THRESHOLD_PATH):
    # Enter threshold value
    threshold = int(input("Valor de threshold: "))

    # Save and pickle
    file.write_it(THRESHOLD_PATH, threshold)
