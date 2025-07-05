import json
import pickle
import numpy as np

__location = None
__data_columns = None
__model = None



def get_estimated_price(location,sqft,bhk,bath):
    x = np.zeros
    return __model.predict([x])


def get_locaton_names():
    return __location


def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __location

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    with open("./artifacts/banglore_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts...done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_locaton_names())