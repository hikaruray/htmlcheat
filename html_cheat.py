from bs4 import BeautifulSoup
from urllib import request

url = 'http://www.htmq.com/html5/'
response = request.urlopen(url)
soup = BeautifulSoup(response, 'html.parser')
response.close()

outer = soup.find_all('div', class_='itemsbody')

ucount=0
flist0=[]
for i in range(0,len(outer)):
    tags = outer[ucount].find_all('a')
    for i in range(0,len(tags)):
        flist0.append(tags[i].get('href'))
    ucount +=1

source_url=[]
for data in flist0:
    url = 'http://www.htmq.com/html5/'
    full=f"{url}{data}"
    source_url.append(full)

ocount=0
flist1=[]
for i in range(0,len(outer)):
    tags = outer[ocount].find_all('a')
    for i in range(0,len(tags)):
        flist1.append(tags[i].text)
    ocount +=1

ccount=0
flist2=[]
for i in range(0,len(outer)):
    itags = outer[ccount].find_all('a')
    for i in range(0,len(itags)):
        flist2.append(str(itags[i].next_sibling))
    ccount +=1

example=[]
urlcount=0

for i in range(0,len(source_url)):
    new_url=source_url[urlcount]
    response = request.urlopen(new_url)
    soup = BeautifulSoup(response, 'html.parser')
    response.close()
    ex = soup.find_all('div', class_='siyorei_source')
    example.append(ex[0].text)
    urlcount+=1

# print(flist1[30]+"\n"+flist2[30]+"\n"+example[30])
print(flist1[1])
print(flist2[1])
print(example[1])

