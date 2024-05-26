import time
from bs4 import BeautifulSoup as bs
import requests as rq

start = time.time()  # stopwatch

links = []


def fiveStar():  # needs to access all relavent unit links
    source: bytes = rq.get(
        "https://allstartd.fandom.com/wiki/5_Star_Units").content
    soup = bs(source, 'html5lib')
    for url in soup.find_all('div', class_='ChBox_item_contet_container'):
        for href in url.find_all('a'):
            links.append(href.get('href'))


def sixStar():  # needs to access all relavent unit links
    source: bytes = rq.get(
        "https://allstartd.fandom.com/wiki/6_Star_Units").content
    soup = bs(source, 'html5lib')
    for url in soup.find_all('div', class_='ChBox_item_contet_container'):
        for href in url.find_all('a'):
            links.append(href.get('href'))


def sevenStar():  # needs to access all relavent unit links
    source: bytes = rq.get(
        "https://allstartd.fandom.com/wiki/7_Star_Units").content
    soup = bs(source, 'html5lib')
    for url in soup.find_all('div', class_='ChBox_item_contet_container'):
        for href in url.find_all('a'):
            links.append(href.get('href'))


def newUnits():  # needs to access all relavent unit links
    source: bytes = rq.get(
        "https://allstartd.fandom.com/wiki/New_Units").content
    soup = bs(source, 'html5lib')
    for url in soup.find_all('div', class_='ChBox_item_contet_container'):
        for href in url.find_all('a'):
            links.append(href.get('href'))


def setLinks():  # compile links into set from list -- removing dups
    return updateList(sorted(set(links), key=str.lower))


def updateList(newSet):  # create/overwrite unitlist.txt
    with open('unitList.txt', 'w') as l:
        l.write(f'{newSet}')


def main() -> None:  # intended to be ran, no return value
    fiveStar()
    sixStar()
    sevenStar()
    newUnits()
    setLinks()


main()
# print(f"\nset links total: {len(links)}\n data type of : {type(links)}\n")  # check new set against old list


# print(sorted(links, key=str.lower))  # sort set by alph-lowercase


# print(f"links total: {len(links)}\n with a data type of : {type(links)}\n") # check old list against new set

end = time.time()  # stopwatch
# print(f"Took {end-start} to run")
