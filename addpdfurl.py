import requests
from bs4 import BeautifulSoup
from urlparse import urlparse
import urllib
import sys,codecs

purl=[]
bib=[]
bibpd=[]

url = 'http://openaccess.thecvf.com/ICCV2013.py'
res = requests.get(url)
parsed=urlparse(url)
s =url.replace(parsed.path,'')

content = res.content
soup = BeautifulSoup(content, 'html.parser')
ptags = soup.find_all('dd')
for ptag in ptags:
    url = ptag.a['href']
    if url.find('papers')>=0:
        purl.append(s+'/'+ url)

print len(purl)

for i in range(len(purl)):
        tags = soup.find_all('div' , class_='bibref')
        for tag in tags:
            bib.append(tag.text)
        print bib[i][:-3] + ',\nurl = {' + purl[i][:-4] + '}\n}'
        bibpd.append(bib[i][:-3] + ',\nurl = {' + purl[i][:-4] + '}\n}\n')
        
w=codecs.open('C:\users\shinoda\desktop\ICCV\\iccv2013.bib','w','utf-8')
w.writelines(bibpd)
w.close()
