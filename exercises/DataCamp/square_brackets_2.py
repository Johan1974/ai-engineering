# https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=16
# exercises/DataCamp/square_brackets_2.py
#
# Oefening: observaties (rijen) uit een DataFrame halen met vierkante haken en een slice.
# Bij cars[0:3] gaat het om rij-posities, niet om de waarden in de index (US, AUS, …).
# Alternatief met dezelfde betekenis: cars.iloc[0:3] en cars.iloc[3:6].

# --- Data inlezen ---
# Import cars data
import pandas as pd
# Eerste kolom uit de CSV wordt de rij-index (landcode).
cars = pd.read_csv('csv/cars.csv', index_col = 0)

# --- Eerste drie rijen ---
# Slice [start:stop): stop telt niet mee → rijen op positie 0, 1 en 2.
print(cars[0:3])

# --- Rijen 4 t/m 6 ---
# Posities 3, 4 en 5 (dus de vierde t/m zesde observatie in de tabel).
print(cars[3:6])
