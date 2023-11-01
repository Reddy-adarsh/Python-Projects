import pandas as pd
df = pd.read_csv("sample.csv")
df.head(10)

list  = []

for i in df["name"]:
    if i["name"] == "Adarsh":
        list.append(i)


def concat_str(str1,str2):
    return str1+' '+str2