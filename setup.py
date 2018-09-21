import pickle
import os

# Get absolute path to project folder
PATH = os.path.dirname(os.path.realpath(__file__))

print("SMRH - Sistema de Recursos Hídricos\n")
x0 = int(input("x0: "))
y0 = int(input("y0: "))
x1 = int(input("x1: "))
y1 = int(input("y1: "))

coord = (x0, y0, x1, y1)
filename = PATH + '/smrh_app/static/data/coord.p'

with open(filename, 'wb') as file:
    pickle.dump(coord, file)
    file.close()
