import pandas as pd
df = pd.read_csv("sample.csv")
df.head(10)

list  = []

for i in df["name"]:
    if i["name"] == "Adarsh"
    list.append(i)