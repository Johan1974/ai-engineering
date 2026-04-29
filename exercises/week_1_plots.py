

import matplotlib.pyplot as plt
import pandas as pd


year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.629, 5.263, 6.972]   


plt.plot(year, pop, color='green', marker='o', linestyle='solid')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Growth')
plt.show()

# Print the last item from year and pop
print(year[-1])
print(pop[-1])



# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)
plt.xlabel('Years')
plt.ylabel('Population')


# Display the plot with plt.show()
plt.show()