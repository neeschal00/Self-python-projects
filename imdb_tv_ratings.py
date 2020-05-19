'''TO GET THE IMDB RATING OF EPISODES OF THE TV SHOWS USING THE IMDB CODE OF THE TV SERIES
THIS GIVES THE DICTIONARY OF EPISODES WITH EPISODE NAME AS KEY AND RATING AS VALUE FOR EACH SEASON'''

from bs4 import BeautifulSoup
import requests

numep = []
imdbcode = input('Enter the imdb code which is (ttXXXXXXX) found in the link:')
link = 'https://www.imdb.com/title/'+imdbcode+'/episodes?season='
mainlink = link + '1'
print(mainlink)


def first(sealink):
    source = requests.get(sealink)

    soup = BeautifulSoup(source.content,'lxml')
    epicont = soup.find('div',class_='seasonAndYearNav').find('select',id='bySeason').find_all('option')

    for cont in epicont:
        numep.append(link + cont['value']) #'creating list of links'
    return numep
    print('There are '+str(len(numep))+' seasons')


def getep(adj):
    episodes = dict()
    check = []

    seas = requests.get(adj)
    # print(seas)
    soup1 = BeautifulSoup(seas.content,'lxml')
    dedu1 = soup1.find('div',class_='list detail eplist')
    # print(dedu1)
    dedu2 = dedu1.find_all('div',class_='info',itemprop='episodes')

    for names in dedu2:
        ep1 = names.find('strong').find('a',itemprop='name').text #getting the title
        # print(ep1.text)
        rat1 = names.find('div',class_='ipl-rating-star small').find('span',class_='ipl-rating-star__rating').text
        # print(rat1.text) #getting the rating
        episodes[ep1] = float(rat1)
    print(episodes)

def final():
    first(mainlink)
    for links in numep:
        getep(links)
    print('Finishes the task')
final()





