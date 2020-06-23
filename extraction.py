import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
import csv

from per_file import unit_file

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

with open('cms_scrape.csv', 'w', newline='') as csv_file:
    fieldname = ['title','link','.pdf', 'pdf size', '.xml', 'xml size', '.djvu','djvu size', '.zip','zip size', 
    '.gz', 'gz size', '.torrent', 'torrent size', '.jpg', 'jpg size']
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldname)

    csv_writer.writeheader()

    # soup_str = soup.prettify()                                            # Prettify the HTML, but it becomes String
    # print(soup_str)

                                                    
    tags = soup.find_all("div", class_ = "item-ttl C C2")                    # Extracts tags with tag div Class = tile-img       
    count = 0
    list_dict = []
    for tag in tags:
        #print (tag.prettify())
        count +=1
        
        link = 'https://archive.org' + tag.a.get('href')                                
        title = tag.a.get('title')
        img_link = tag.a.div.img.get('source')
        # print(link)
        # print(title)
        # print(img_link)

        file_url = link.replace("/details/","/download/")
        #print(file_url)
        unit_dict = unit_file(file_url)
        
        csv_writer.writerow({'link': link, 'title' : title, '.pdf' : file_url + "/"+ unit_dict['.pdf'][0], 'pdf size' : unit_dict['.pdf'][1],
         '.xml' : file_url +"/"+ unit_dict['.xml'][0], 'xml size' :  unit_dict['.xml'][1],
        '.djvu' : file_url +"/"+ unit_dict['.djvu'][0], 'djvu size' :  unit_dict['.djvu'][1],
         '.zip' : file_url +"/"+ unit_dict['.zip'][0], 'zip size' :  unit_dict['.zip'][1],
          '.gz' : file_url +"/"+ unit_dict['.gz'][0], 'gz size' : unit_dict['.gz'][1],
           '.torrent' : file_url +"/"+ unit_dict['.torrent'][0], 'torrent size' :  unit_dict['.torrent'][1],
         '.jpg' : file_url +"/"+ unit_dict['.jpg'][0], 'jpg size' :  unit_dict['.jpg'][1]})
        
        list_dict += [unit_dict]
        print (count,end="\n")
        print(" ")
        if count == 10:
            break



