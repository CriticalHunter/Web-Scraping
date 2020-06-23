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

print(len(list(soup.children)))                                       # List of direct childrens
print(len(list(soup.descendants)))                                    # List of all descendants

txts = (soup.get_text())                                              # Extracts all text elements into a string
#print((txts)

soup_str = soup.prettify()                                            # Prettify the HTML, but it becomes String
#print(soup_str)

                                                   
tags = soup.find_all("div", {"class": "tile-img"})                    # Extracts tags with tag div Class = tile-img       


#print(soup.find_all(string='Atlanta'))                               # Seraches for string, instead of tags
#soup.find(id="link3")                                                # Finds if any element is there with id = Link3

#To iterate over parents of a single tag : #############


count = 0
for tag in tags:
    print(tag)
    count +=1
    link = tag.get('href', None)                                      # Extracts href property objects of each tags
    link1 = tag.get('href') 
 #   print(link)   
print (count)
# ##########Using Regex inside find_all ###############
# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)
# # body
# # b
