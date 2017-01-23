

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html, 'html.parser')


nameList = bsObj.findAll('span', {'class':'green'})
name_list = bsObj.findAll(text='the prince')
print(len(name_list))

# for name in nameList:
#     print(name.get_text())
#     print (name)

allText = bsObj.findAll(id='text')
# print(allText[0].get_text())



html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'html.parser')
# for child in bsObj.find('table',{'id':'giftList'}).children:
#     print(child)

for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_sibling:
    print(sibling)