import requests
from bs4 import BeautifulSoup
import json
import _pickle as pickle
from tqdm import tqdm

FILENAME = "articleLinks.dat"

def writeToFile(arr = [], fn = FILENAME):
    with open(fn, 'wb') as filehandle:
        pickle.dump(links, filehandle)

def readFromFile(fn = FILENAME):
    with open(fn, 'rb') as filehandle:
       return pickle.load(filehandle)

print(len(readFromFile()[0]))
