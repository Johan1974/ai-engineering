# 🐍 Python Basics Cheat Sheet

### 1. Variabelen & Types
```python
x = 5               # Integer
y = 3.14            # Float
name = "Johan"      # String
is_active = True    # Boolean

# Check het type
type(x)             # <class 'int'>
```

### 2. Math Operators
| Operator | Actie | Voorbeeld |
| :--- | :--- | :--- |
| `+` | Optellen | `5 + 2 = 7` |
| `-` | Aftrekken | `5 - 2 = 3` |
| `*` | Vermenigvuldigen | `5 * 2 = 10` |
| `/` | Delen | `5 / 2 = 2.5` |
| `%` | Modulo (Restwaarde) | `5 % 2 = 1` |
| `**` | Machtverheffen | `5 ** 2 = 25` |

### 3. Strings
```python
s = "python is leuk"

s.upper()           # "PYTHON IS LEUK"
s.lower()           # "python is leuk"
s.capitalize()      # "Python is leuk"
s.replace("u", "o") # "python is leok"
```

### 4. Lists
```python
fam = [1.73, 1.68, 1.71, 1.89]

fam[0]              # 1.73 (Eerste item)
fam[-1]             # 1.89 (Laatste item)
fam[1:3]            # [1.68, 1.71] (Slicing)

# Aanpassen
fam[0] = 1.75       # Verander item
fam + [1.92]        # Lijsten samenvoegen
del(fam[2])         # Item verwijderen
```

### 5. Libraries & Help
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

help(max)           # Toon documentatie
dir(fam)            # Toon alle methodes
```