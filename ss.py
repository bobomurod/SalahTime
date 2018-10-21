from bs4 import BeautifulSoup
import requests
import os

url = 'https://www.islom.uz/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
<<<<<<< HEAD
path = ''

=======
path = '~'
>>>>>>> b04e9482ee969d70ea5ecfc62457812619165a79

namaazNames = soup.select('div.p_v')
namaazNames = [namaazName.text for namaazName in namaazNames]
namaazTimes = soup.select('div.p_clock')
namaazTimes = [namaazTime.text for namaazTime in namaazTimes]
del namaazNames[1]
del namaazTimes[1]

for namaazName, namaazTime in zip(namaazNames, namaazTimes):
    with open(path + namaazName + '.txt', 'w') as file:
        file.write(namaazTime)

with open("Тонг.txt", "r") as my_new_handle:
    for the_line in my_new_handle:

        print("Bomdot",the_line)
with open("Пешин.txt", "r") as my_new_handle:
    for the_line in my_new_handle:

        print("Пешин:",the_line)
with open("Аср.txt", "r") as my_new_handle:
    for the_line in my_new_handle:

        print("Аср:",the_line)
with open("Шом.txt", "r") as my_new_handle:
    for the_line in my_new_handle:

        print("Шом:",the_line)
with open("Хуфтон.txt", "r") as my_new_handle:
    for the_line in my_new_handle:

        print("Хуфтон:",the_line)
        