import pandas as pd



df = pd.read_csv("Virat_Kohli.csv.xls")

print(df)

print(df.head(10))

print(df.tail(10))

df.info()

print(df.shape)
print(df.describe)

print(df["Opposition"].describe())

run_frequency = df["Opposition"].value_counts()
print(run_frequency)

run_frequency = df["Runs"].value_counts()
print(run_frequency)


print(df["Opposition"] == "v Australia")
new_df = df[["Runs", "SR", "Opposition"]]
print(new_df)

vs_aussies = df[df["Opposition"] == "v Australia"]
print(vs_aussies)

# Find all the matches where virat kohli scored a century

# Find all the matches where virat's strike rate was > 100

#Find all the matches where virat played with srilanka and scored a century

tons = df[df["Runs"] >= 100]
print(tons)

stk = df[df["SR"] > 100]
print(stk)

sril_cent = df[
    (df["Opposition"] == "v Sri Lanka") & (df["Runs"])]

print(sril_cent)


def find_centuries(x):
    if x >= 100:
        return "OG"
    else:
        return "NOOB"

df["Centuries"] = df["Runs"].apply(find_centuries)
print(df.tail())


tr = df["Runs"].sum()
print("Total number of runs: ", tr)