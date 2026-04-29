# https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=17
# exercises/DataCamp/loc_and_iloc_1.py
#
# loc = selectie op indexlabels (hier: landcodes US, JPN, …).
# iloc = selectie op rijpositie (0 = eerste rij in de DataFrame, ongeacht label).

# Import cars data
import pandas as pd
cars = pd.read_csv('csv/cars.csv', index_col = 0)

# Observatie voor Japan: label 'JPN' in de index, of positie 2 (0-based).
print(cars.loc[['JPN']])
print(cars.iloc[[2]])

# Observaties voor Australië en Egypte: labels 'AUS' en 'EG', of posities 1 en 6.
print(cars.loc[['AUS', 'EG']])
print(cars.iloc[[1, 6]])
