#coding:utf-8
from bs4 import BeautifulSoup
import urllib

url = "http://www.boxofficemojo.com/movies/?page=daily&id=avatar.htm"
html = urllib.urlopen(url)
print 1
content = html.read()
html.close()
soup = BeautifulSoup(content,"html.parser")
print 1
tds = soup.findAll("td")
m = 0
#20 is Friday
for i in tds[20:]:
	m += 1
	boxs = i.findAll("font")
	if len(boxs) < 3:
		continue
	box_leiji = boxs[-1]
	print box_leiji.text
	# if m > 50:
	# 	break
# print tds#18hao
