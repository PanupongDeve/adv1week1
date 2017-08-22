from urllib import request
import re

f = request.urlopen('http://fivedots.coe.psu.ac.th')

text = f.read().decode('utf-8')

line = text.split("\n")

nameList = line[32:78]

nameList = nameList[2:47]

# print(nameList[43])

for i in range(44):
	print(nameList[i]+"\n")

regList = [None]*44

# print(regList)

for i in range(44):
	regList[i] = re.search(r"<li>(.*)",nameList[i])
	print(regList[i].group(1))


# regList2 = [None]*44

# for i in range(44):
# 	regList2[i] = re.search(r"<a>(.*)</a>",regList[i])
# 	print(regList2[i].group(1))