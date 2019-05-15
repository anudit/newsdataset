import requests
from bs4 import BeautifulSoup
import json

FILENAME = "articleLinks.dat"

r = requests.get("https://timesofindia.indiatimes.com/india")
soup = BeautifulSoup(r.content, features="html.parser")
links = []
for link in soup.select("a[href*=cms]"):
    href = link['href']
    if(str(href).find("videoshow") >= 0 or str(href).find("photogallery") >= 0 or str(href).find("articleshow") == -1):
        continue
    elif(str(href).find("https://timesofindia.indiatimes.com") == -1):
        links.append("https://timesofindia.indiatimes.com" + link['href'])
    else:
        links.append(link['href'])

links = set(links) #remove duplicates
print(links)
