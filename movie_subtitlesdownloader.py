import requests
from bs4 import BeautifulSoup
import zipfile

movie = input('Enter the name of movie: ')

srlink = 'https://www.yifysubtitles.com/search?q=' + movie
# print(srlink)

source = requests.get(srlink)
print(source)

# with open('subtitles.html','wb') as st:
#     st.write(source.content)

soup = BeautifulSoup(source.content,'lxml')

media = soup.find('ul',class_='media-list')
# print(media)

mclick =soup.find_all('li',class_='media media-movie-clickable')

dicts = {}


for body in mclick:
    mdbody = body.find_all('div',class_='media-body')
    for cont in mdbody:
        links = cont.find('a').get('href')
        # print(links)
        for head in mdbody:
            titles = head.find('h3',class_='media-heading')
            # print(titles.text)
            dicts[titles.text] = links
# print(dicts)

lititles = list(dicts.keys())
print(lititles)
num = 0
for nms in lititles :
    print(str(num)+ '-' + nms)
    num += 1

tlink = int(input('Enter the number from the list that you want to download: '))
get_title = lititles[tlink]

final_link = 'https://www.yifysubtitles.com' + dicts.get(get_title)
# final_link = 'https://www.yifysubtitles.com/movie-imdb/tt1424310'
# print(final_link)

subsource = requests.get(final_link)
soup1 = BeautifulSoup(subsource.content,'lxml') #2nd soup for different link

tableE = soup1.find('div',class_='table-responsive')
tableB = tableE.find('tbody')
# print(tableB.prettify())

highR = tableB.find_all('tr',class_='high-rating') #getting all the highest rated subtitle class
movieids = []
for tink in highR:
    # print(tink)
    checkflag = tink.find('td',class_='flag-cell')
    engcheck = checkflag.find('span',class_='sub-lang',string='English')
    if engcheck is not None:
        ids = engcheck.find_parent('td').find_parent('tr')['data-id'] #finding the parent and getting the id to access the downloadable link
        movieids.append(ids)

paramid = {'data-id':movieids[0]}
# print(paramid)

dwntab = tableE.find('tr',paramid)
# print(dwntab.prettify())
dwnlink ='https://www.yifysubtitles.com'  + dwntab.find('a',class_='subtitle-download')['href'] #final download link to get the website
# print(dwnlink)

final_source = requests.get(dwnlink)
soup2 = BeautifulSoup(final_source.content,'lxml')

container1 = soup2.find('div',class_='row row-section')
# print(container1.prettify())
contTitle = container1.find('div',class_='col-md-5 col-md-pull-4 col-sm-8 movie-main-info text-center').find('h2') #gets the title to use as file name
# print(contTitle.text)

dwnldlink = container1.find('div',class_='col-xs-12',style=None).find('a',class_='btn-icon download-subtitle')['href']
print(dwnldlink)

filename = contTitle.text + 'Subtitle.zip'
# print(filename)

downloadableSub = requests.get(dwnldlink) #requests the zipfile link

with open(filename,'wb') as subs:
    subs.write(downloadableSub.content)


with zipfile.ZipFile(filename,'r') as extractsub:
    extractsub.extractall('subtitle')





