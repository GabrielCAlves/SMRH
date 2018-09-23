import pickle

def read_it(FILE_PATH):
    with open(FILE_PATH, 'rb') as temp_file:
        return pickle.load(temp_file)

def write_it(FILE_PATH, variable):
    with open(FILE_PATH, 'wb') as temp_file:
        pickle.dump(variable, temp_file)
        temp_file.close()
