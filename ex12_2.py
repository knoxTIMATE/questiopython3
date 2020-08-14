import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
'''
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')
'''
counter = 1
for i in range(4):
    if counter == 1:
        url = input('Enter - ')
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
    counter = 0
    
    else:
        
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        for index, tag in enumerate(tags):
            if index == 2:
                print ()
                print ()
                print (index)
                #print (tag)
                print (tag.get('href', None))
                url = tag.get('href', None)
                #counter = 0
                if i==3:
                    print ('Last name:',tag.contents[0])
                print ()
                print ()
