
import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_price(location,sqft,bath,bhk,balcony):
    loc_index = -1
    location_lower = location.lower()

    try:
        loc_index = __data_columns.index(location_lower)
    except:
        loc_index=-1

    arr = np.zeros(len(__data_columns))
    arr[-4] = bhk
    arr[-3] = sqft
    arr[-2] = bath
    arr[-1] = balcony
    if loc_index >= 0:
        arr[loc_index] = 1

    return round(__model.predict([arr])[0],2)
   




def load_artifacts():
    print("loading artifacts")
    global __data_columns
    global __locations
    global __model

    with open("Bangalore-Home-Price-Prediction/Prediction App/server/artefacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[:-4]

    with open("Bangalore-Home-Price-Prediction/Prediction App/server/artefacts/BLR_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)
    
    print("Loading artifacts..Done")

def location_names():
    return __locations

def get_data_columns():
    return __data_columns

    
# if __model is None:
#     with open('Bangalore-Home-Price-Prediction/Prediction App/server/artefacts/BLR_home_prices_model.pickle', 'rb') as f:
#         __model = pickle.load(f)
#     print("loading saved artifacts...done")

if __name__=="__main__":
    load_artifacts()
    print(location_names())
    print(get_price('Whitefield',2000,3,3,3))
    print(get_price('2nd Phase Judicial Layout',3000,4,3,3))
