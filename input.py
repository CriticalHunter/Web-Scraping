from extraction import extract_data

base_url = "https://archive.org/details/"
topic = input("Enter the Topic ")
url = base_url+topic+"?&sort=-downloads&page="

try:
    start_page = int(input("Enter Start Page "))
except:
    start_page = 1
try:
    End_page = int(input("Enter Start Page "))
except:
    End_page = 1

for pages in range(start_page,End_page+1):
    url_current = url + str(pages)
    extract_data(url_current)

