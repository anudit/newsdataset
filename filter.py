import pandas as pd
import csv

def writeToFile(arr = [], fn = "FAKE.CSV"):
    with open(fn, 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(["title","category", "link"])
        for row in arr:
            writer.writerow(row)

df = pd.read_csv('articleLinks.csv', delimiter = ',')
print(df.info())

unique_dat = []
unique_keys = df.title.unique()

for title in unique_keys:
    q = "title == \'" + str(title) + "\'"
    tdf = df.query(q)
    unique_dat.append([list(tdf.title)[0],list(tdf.category)[0],list(tdf.link)[0]])

print(len(df.title))
print(len(unique_dat))
writeToFile(unique_dat, fn = "articleLinksBig.csv")
