import pandas as pd

data = {
    "apples": [4, 3, 6, 1],
    "oranges": [3, 7, 4, 1]
}

index_titles = [
    "Aaron", "Shaun", "James", "Wilson"
]

df = pd.DataFrame(data, index = index_titles)

# print(df)
# print(type(df))
# print(df.loc["Aaron"])  # row inndexing
# print(df.loc["Aaron"]["apples"])
# print(df["oranges"].iloc[0:])   #column indexing

import matplotlib.pyplot as plt

df = pd.read_csv("Virat_Kohli.csv.xls")
df[ 'Inns'].plot( Inns= 'second inns')