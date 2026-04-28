
#%%
import matplotlib.pyplot as plt
import pandas as pd

#%%
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.629, 5.263, 6.972]   

#%%
plt.plot(year, pop, color='green', marker='o', linestyle='solid')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Growth')
plt.show()
# %%
