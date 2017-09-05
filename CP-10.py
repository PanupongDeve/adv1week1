from urllib import request
import re

def getNameFromHtml(html):
	f = request.urlopen(html)
	text = f.read().decode('utf-8')
	line = text.split("\n")
	nameList = line[32:78]
	nameList = nameList[2:47]
	f.close()
	return nameList

def filter_html_v1(pat,arrayText,len):
	result = []
	for i in range(len):
		match = re.findall(pat,arrayText[i])
		if(match):
			result.append(match[0])
		else:
			result.append(arrayText[i])
	return result

def filter_html_v2(pat,arrayText,len):
	result = []
	for i in range(len):
		match = re.findall(pat,arrayText[i])
		if(match):
			result.append(match[0][1])
		else:
			result.append(arrayText[i])
	return result
def showList(lists):
	for list in lists:
		print(list)

nameList = getNameFromHtml('http://fivedots.coe.psu.ac.th')

pat = "<li>(.*)"
nameList = filter_html_v1(pat,nameList,len(nameList))
pat = "(.*) -->"
nameList = filter_html_v1(pat,nameList,len(nameList))
pat = '<a href="(.*)">(.*)</a>'
nameList = filter_html_v2(pat,nameList,len(nameList))
showList(nameList)

		