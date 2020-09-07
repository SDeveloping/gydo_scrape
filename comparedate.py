from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "https://www.gymnasiumdorfen.de/"
page = requests.get(url=url)
print(page)

soup = BeautifulSoup(page.text, 'html.parser')

container = soup.find_all(class_='ce-container')
newdate = container[0].get_text().split("\n")[2].split(" ")[0]

"""
Datum aus Datei lesen und in var speichern
Newsdate mit altem Datum vergleichen
1. newsdate == olddate -> nix neues
2. newsdate > olddate -> neues post
--> print
--> newsdate speichern
"""

with open("datelog.txt", mode="r") as result:
    olddate = result.read()

d_olddate = datetime.strptime(olddate, "%d.%m.%Y")
d_newdate = datetime.strptime(newdate, "%d.%m.%Y")

if d_olddate == d_newdate:
    print("Nix neues")
else:
    print("Neuer Beitrag")
    with open("datelog.txt", mode="w") as result:
        result.write(newdate)

print(newdate)
