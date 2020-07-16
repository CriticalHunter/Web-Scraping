import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
import openpyxl

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

def full_extract(url,page=1):

    my_path = "magData.xlsx"
    my_wb = openpyxl.load_workbook(my_path)
    ws = my_wb.active
    

    # soup_str = soup.prettify()                                            # Prettify the HTML, but it becomes String
    # print(soup_str)

                                                    
    tags = soup.find_all("div", class_ = "item-ttl C C2")                    # Extracts tags with tag div Class = tile-img       
    count = 0
    for tag in tags:
        #print (tag.prettify())
        count +=1
        
        link = 'https://archive.org' + tag.a.get('href')                                
        title = tag.a.get('title')
        #img_link = tag.a.div.img.get('source')
        # print(link)
        # print(title)
        # print(img_link)

        file_url = link.replace("/details/","/download/")
        #print(file_url)
        unit_dict = unit_file(file_url)
        
        ws.append([link,title,file_url + "/"+ unit_dict['.pdf'][0],unit_dict['.pdf'][1],
        file_url +"/"+ unit_dict['.xml'][0],unit_dict['.xml'][1],
        file_url +"/"+ unit_dict['.djvu'][0],unit_dict['.djvu'][1],
        file_url +"/"+ unit_dict['.zip'][0],unit_dict['.zip'][1],
        file_url +"/"+ unit_dict['.gz'][0],unit_dict['.gz'][1],
        file_url +"/"+ unit_dict['.torrent'][0],unit_dict['.torrent'][1],
        file_url +"/"+ unit_dict['.jpg'][0],unit_dict['.jpg'][1]])
        
        print ('Page ',page, ' - ',count,end="\n")
        
        # if count == 5:
        #     break
    my_wb.save("magData.xlsx")


