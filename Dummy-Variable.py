import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Gender': ['Male', 'Female', 'Female', 'Male']
}

df = pd.DataFrame(data)

dummy = pd.get_dummies(df['Gender'])

print(dummy)
