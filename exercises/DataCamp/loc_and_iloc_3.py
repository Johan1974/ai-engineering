# https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=19
# exercises/DataCamp/loc_and_iloc_3.py
# `:` in loc = alle rijen; tweede indexer = kolom(men).

# Import cars data
import pandas as pd
cars = pd.read_csv('csv/cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
