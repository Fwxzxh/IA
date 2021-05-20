#%%
import pandas as pd
url = ( 
    "https://archive.ics.uci.edu/ml/machine-learning-databases"
    "/abalone/abalone.data"
)
abalone = pd.read_csv(url, header=None)

#%%
abalone.head()

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

abalone = abalone.drop("Sex", axis=1)

#%%
import matplotlib.pyplot as plt
abalone["Rings"].hist(bins=15)
plt.show()

#%%
correlation_matrix = abalone.corr()
correlation_matrix["Rings"]

