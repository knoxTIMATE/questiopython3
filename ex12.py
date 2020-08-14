from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')


number=[]

for tag in tags:
    print ('--------------------------------------------')
    print (tag)
   
    print (tag.contents[0])
    number.append(int(tag.contents[0]))
    print(tag.attrs )
    print ('--------------------------------------------')



total = sum(number)
print (total)