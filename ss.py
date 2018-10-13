from bs4 import BeautifulSoup
import requests

url = 'https://www.hujjat.org/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
path = '/home/ulugbek/python/SalahTime/'

namaazNames = soup.select('div.NamaazTimeName')
namaazNames = [namaazName.text for namaazName in namaazNames]
namaazTimes = soup.select('div.NamaazTime')
namaazTimes = [namaazTime.text for namaazTime in namaazTimes]
del namaazNames[1]
del namaazTimes[1]

for namaazName, namaazTime in zip(namaazNames, namaazTimes):
    with open(path + namaazName + '.txt', 'w') as file:
        file.write(namaazTime)