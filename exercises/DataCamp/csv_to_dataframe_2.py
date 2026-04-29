# DataCamp exercise reference:
# https://campus.datacamp.com/courses/intermediate-python/dictionaries-pandas?ex=13

# Load pandas and give it the common alias "pd"
import pandas as pd

# Read the CSV file into a DataFrame.
# index_col=0 tells pandas to use the first column as row labels (index).
cars = pd.read_csv('csv/cars.csv', index_col=0)

# Display the full DataFrame in the console.
print(cars)