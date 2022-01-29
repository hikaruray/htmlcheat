from bs4 import BeautifulSoup
from urllib import request

# -------------------------------
# SCRAPE HTML TAGS FROM SITE

# -------------------------------
url = 'http://www.htmq.com/html5/'
response = request.urlopen(url)
soup = BeautifulSoup(response, 'html.parser')
response.close()

#locate data & get 1 href data
outer = soup.find_all('div', class_='itemsbody')
url= outer[2].find_all('a')

#loop to get all href data
ucount=0
flist0=[]
for i in range(0,len(outer)):
    tags = outer[ucount].find_all('a')
    for i in range(0,len(tags)):
        flist0.append(tags[i].get('href'))
    ucount +=1

#make url list
source_url=[]
for data in flist0:
    url = 'http://www.htmq.com/html5/'
    full=f"{url}{data}"
    source_url.append(full)

#get 1 htmltag 
tags = outer[2].find_all('a')

#loop to gett all htmltag

ocount=0
flist1=[]
for i in range(0,len(outer)):
    tags = outer[ocount].find_all('a')
    for i in range(0,len(tags)):
        flist1.append(tags[i].text)
    ocount +=1

#get inner text 
itag=outer[0].find_all('a')

#loop all inner text
ccount=0
flist2=[]
for i in range(0,len(outer)):
    itags = outer[ccount].find_all('a')
    for i in range(0,len(itags)):
        flist2.append(itags[i].next_sibling)
    ccount +=1


# access tag name urls and get siyorei texts
new_url=source_url[60] #used 60 as example
response = request.urlopen(new_url)
soup = BeautifulSoup(response, 'html.parser')
response.close()

ex = soup.find_all('div', class_='siyorei_source')

#get all siyoreis from tagnames
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

# <figure>
#  …… 図表であることを示す

# HTMLソース
# 	<p>カエルの生態に関しては、<a href="#kaeru">こちらの画像</a>でご確認いただけます。</p>

# 	<figure id="kaeru">
# <img src="../images/kaeru.gif" alt="葉っぱを傘代わりにするカエル">
# <figcaption>カエルの生態</figcaption>
# </figure>

# <p>カエルは雨降りが好きなので…</p>	