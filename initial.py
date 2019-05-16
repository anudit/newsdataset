import requests
from bs4 import BeautifulSoup
import json
from tqdm import trange
import csv

FILENAME = "articleLinksCity.csv"

def writeToFile(arr = [], fn = FILENAME):
    with open(fn, 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(["title","category", "link"])
        for row in arr:
            writer.writerow(row)

def readFromFile(fn = FILENAME):
    with open(fn, 'r') as readFile:
        reader = csv.reader(readFile)
        l = []
        for row in reader:
            try:
                l.append(row)
            except:
                continue
        return l

links = []
currentPageUrl = "https://timesofindia.indiatimes.com/city"

r = requests.get(currentPageUrl)
soup = BeautifulSoup(r.content, features="html.parser")

selectedLinks = soup.select("a[href*=cms]")


for i in trange(len(selectedLinks)):

    href = selectedLinks[i]['href']
    testLink = ""
    if(str(href).find("videoshow") >= 0 or str(href).find("photogallery") >= 0 or str(href).find("articleshow") == -1):
        continue
    elif(str(href).find("https://timesofindia.indiatimes.com") == -1):
        testLink = "https://timesofindia.indiatimes.com" + selectedLinks[i]['href']
    else:
        testLink = selectedLinks[i]['href']

    try:
        request = requests.get(testLink)
        st1 = testLink.split('/')
        title = st1[-3]
        title = ' '.join([x.capitalize() for x in title.split('-')])
        category = st1[3]

        if request.status_code == 200:
            links.append([title, category, testLink])
            # print("add:"+testLink)
        else:
            continue
    except:
        continue

combinedData = readFromFile() + links
writeToFile(combinedData)
