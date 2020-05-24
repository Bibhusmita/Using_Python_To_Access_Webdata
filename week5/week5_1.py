import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input("Enter location:")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

s = 0
count = tree.findall('.//count')
print("Count:",len(count))
for i in count:
    s += int(i.text)
print("Sum:",s)
