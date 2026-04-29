# https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=19&skip_variants_modal=true
# exercises/DataCamp/loc_and_iloc_3.py
#
# Oefening: met loc alle rijen behouden (`:`) en kolommen kiezen.
# Eerste indexer = rijen (`:` = geen filter op rijlabels), tweede = kolomnamen.
# Eén string als kolom → Series; lijst met één of meer namen → DataFrame.

# Import cars data
import pandas as pd
cars = pd.read_csv('csv/cars.csv', index_col = 0)

# drives_right als Series (enkele kolomselector = string).
print(cars.loc[:, 'drives_right'])

# Zelfde kolom als DataFrame: kolomnamen in een lijst, ook als het er maar één is.
print(cars.loc[:, ['drives_right']])

# Twee kolommen tegelijk als sub-DataFrame.
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
