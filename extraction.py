import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://archive.org/details/maximumpc?&sort=-downloads&page=1'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

html = urllib.request.Request(url, headers = hdr)                     # Header is added so that this program behaves like a Browser
html_read = urllib.request.urlopen(html, context = ctx).read()        # reads all HTML data, but in a single line
soup = BeautifulSoup(html_read, 'html.parser')                        # Structures the HTML data, human readable


# soup_str = soup.prettify()                                            # Prettify the HTML, but it becomes String
# print(soup_str)

                                                   
tags = soup.find_all("div", class_ = "item-ttl C C2")                    # Extracts tags with tag div Class = tile-img       
count = 0
for tag in tags:
    #print (tag.prettify())
    count +=1
    
    link = tag.a.get('href')                                    # Extracts href property objects of each tags
    title = tag.a.get('title')
    img_link = tag.a.div.img.get('source')
    print(link)
    print(title)
    print(img_link)
print (count)
# ##########Using Regex inside find_all ###############
# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)
# # body
# # b
