import json
import pickle
import numpy as np

__location = None
__data_columns = None
__model = None


def predict_estimate_price(sqft, location, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())

    except:
        loc_index = -1

    X = np.zeros(len(__data_columns))
    X[0] = sqft
    X[1] = bath
    X[2] = bhk
    if loc_index >= 0:
        X[loc_index] = 1

    return round(__model.predict([X])[0], 2)


def get_location_names():
    return __location


def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __location

    global __model

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts...done")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(predict_estimate_price(1000, '1st block jayanagar', 2, 2))
    print(predict_estimate_price(1000, '1st phase jp nagar', 2, 2))
    print(predict_estimate_price(1000, '2nd phase judicial layout', 2, 2))
    print(predict_estimate_price(1000, '2nd stage nagarbhavi', 2, 2))
