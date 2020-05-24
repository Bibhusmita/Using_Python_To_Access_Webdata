import json
import urllib.request, urllib.parse, urllib.error
import ssl

url = input("Enter location:")


print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')


info = json.loads(data)

count = 0
s = 0
for item in info["comments"]:
  s += int(item["count"])
  count += 1

print("Count:",count)
print("Sum:",s)
