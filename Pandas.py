#Pandas is a Python library used to store, organize, analyze, and work with data..

import pandas as pd

data = {
    "Name": ["Rahul", "Aman", "Priya"],
    "Age": [20, 21, 19]
}

df = pd.DataFrame(data)

print(df)