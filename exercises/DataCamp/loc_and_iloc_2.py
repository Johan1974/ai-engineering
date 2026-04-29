# https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=18
# exercises/DataCamp/loc_and_iloc_2.py
#
# loc[rijlabels, kolomlabels] — eerste argument = rijen, tweede = kolommen.

# Import cars data
import pandas as pd
cars = pd.read_csv('csv/cars.csv', index_col = 0)

# Alleen drives_right voor Marokko (rij MOR, één kolom).
print(cars.loc[['MOR'], ['drives_right']])

# Sub-DataFrame: twee landen, twee kolommen.
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])
