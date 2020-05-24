from urllib.request import urlopen
from bs4 import BeautifulSoup
url = input('Enter Url: ')
count = int(input("Enter count: "))
position = int(input("Enter position:"))
t = []
print("Retrieving:",url)
for i in range(count):
    html = urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")

    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)
    
    print("Retrieving:",s[position-1])
    url = s[position-1]
print(t[position-1])