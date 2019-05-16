import requests
from bs4 import BeautifulSoup
import json
import _pickle as pickle
from tqdm import tqdm

FILENAME = "articleLinks.dat"

def readFromFile(fn = FILENAME):
    with open(fn, 'rb') as filehandle:
       linkList =  pickle.load(filehandle)
       print(len(linkList))
       print("\n")
       print(type(linkList))
       # print("\n")
       # print(linkList)

# for i in tqdm(range(len(linkList[:1]))):
#        print(linkList[i])

linkList = readFromFile()
