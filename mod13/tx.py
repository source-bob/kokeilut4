import pandas as pd

data = pd.read_csv('C:/Users/onion/Desktop/databases/countries.csv', sep=',', header=0, on_bad_lines='skip')
base = pd.DataFrame(data)
osa = base
print(osa)