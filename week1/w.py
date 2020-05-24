import re

if __name__ == '__main__':
    file = open('w2.txt')
    sm = sum([for int(n) in re.findall('[0-9]+',file.read())])
    print(sm)