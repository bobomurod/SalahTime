import bs4
import requests

s = requests.get('https://islom.uz/')
b = bs4.BeautifulSoup(s.text, "html.parser")
print (b.select('.pray-times .a-link-white')[0].getText())
print (b.select('.pray-times .a-link-white')[1].getText())
print (b.select('.pray-times .a-link-white')[2].getText())
print (b.select('.pray-times .a-link-white')[3].getText())
print (b.select('.pray-times .a-link-white')[4].getText())
print (b.select('.pray-times .a-link-white')[5].getText())
print ("\n")

# `.pray-times
# .a-link-white







// this tis comment 


# url = "http://www.old.islom.uz/azon/gettable.php?GMT=26&type=1&alphatype=3&bgcolor=FFFFFF&background=&bordercolor=666666&bordergcolor1=FFFFFF&bordergcolor2=CCCCCC&titlebg=999999&titlecolor=FFFFFF&fontcolor=000000&fontsize=11"

# findthis = "<u>ВРЕМЯ НАМАЗОВ</u>"
# soup = bs4.BeautifulSoup(findthis, 'lxml')
# print (soup.text)
