import bs4
import requests

s = requests.get('https://islom.uz/')
b = bs4.BeautifulSoup(s.text, "html.parser")
print(s)

time = b.find_all('div', class_ = "p_clock " )
print(time)
print(type(time))
#print (b.select('.p_clock .a-link-white')[0].getText())
# print (b.select('.pray-times .a-link-white')[1].getText())
# print (b.select('.pray-times .a-link-white')[2].getText())
# print (b.select('.pray-times .a-link-white')[3].getText())
# print (b.select('.pray-times .a-link-white')[4].getText())
# print (b.select('.pray-times .a-link-white')[5].getText())
# print ("\n")
