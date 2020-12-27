import requests
from bs4 import BeautifulSoup
import sys

sys.dont_write_bytecode = True

url = f"https://www.worldometers.info/coronavirus"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
data = soup.find('tbody').find_all('tr')

info = []
indices = [2,3,4,5,6,7,9,13,15,16]

for d in data:
    d = d.text.split('\n')
    d = list(map(lambda x:'not available' if x==' ' or x=='' else x, d))
    d = [d[i] for i in indices]
    info.append(d)
