import re

file = open("w2.txt")

s = 0

for li in file:
	line = li.rstrip()
	l = re.findall('[0-9]+',line)
	if(len(l) != 0):
		for n in l:
			s += int(n)

print(s)