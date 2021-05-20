#%%
import numpy as np
a = np.array([2, 2])
b = np.array([4, 4])
np.linalg.norm(a - b)

#%%
import pandas as pd
url = ( 
    "https://archive.ics.uci.edu/ml/machine-learning-databases"
    "/abalone/abalone.data"
)
abalone = pd.read_csv(url, header=None)


#%%
abalone.columns = [
    "Sex",
    "Length",
    "Diameter",
    "Height",
    "Whole weight",
    "Shucked weight",
    "Viscera weight",
    "Shell weight",
    "Rings",
]

X = abalone.drop("Rings", axis=1)
X = X.values
y = abalone["Rings"]
y = y.values

#%%
new_data_point = np.array([
    0.569552,
    0.446407,
    0.154437,
    1.016849,
    0.439051,
    0.222526,
    0.291208,
])

distances = np.linalg.norm(X - new_data_point, axis=1)

k = 3
nearest_neighbor_ids = distances.argsort()[:k]
nearest_neighbor_ids
