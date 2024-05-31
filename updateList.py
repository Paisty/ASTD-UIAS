import re
import time
from bs4 import BeautifulSoup as bs
import requests as rq

start = time.time()  # stopwatch

links = []
pre = 'https://allstartd.fandom.com'


def fiveStar():  # needs to access all relevant unit links
    source: bytes = rq.get(
        "https://allstartd.fandom.com/wiki/5_Star_Units").content
    soup = bs(source, 'lxml')
    for url in soup.find_all('div', class_='ChBox_item_contet_container'):
        for href in url.find_all('a'):
            links.append(href.get('href'))


def sixStar():  # needs to access all relevant unit links
    source: bytes = rq.get(
        "https://allstartd.fandom.com/wiki/6_Star_Units").content
    soup = bs(source, 'lxml')
    for url in soup.find_all('div', class_='ChBox_item_contet_container'):
        for href in url.find_all('a'):
            links.append(href.get('href'))


def sevenStar():  # needs to access all relevant unit links
    source: bytes = rq.get(
        "https://allstartd.fandom.com/wiki/7_Star_Units").content
    soup = bs(source, 'lxml')
    for url in soup.find_all('div', class_='ChBox_item_contet_container'):
        for href in url.find_all('a'):
            links.append(href.get('href'))


def newUnits():  # needs to access all relevant unit links
    source: bytes = rq.get(
        "https://allstartd.fandom.com/wiki/New_Units").content
    soup = bs(source, 'lxml')
    for url in soup.find_all('div', class_='ChBox_item_contet_container'):
        for href in url.find_all('a'):
            links.append(href.get('href'))


def myfunc(b):  # adds the pre literal to the rest of the URL taken from previous functions(). proly use a lmbda func instead
    return pre + b


def setLinks():  # compile links into set from list -- removing dupes
    x = map(myfunc, links)
    return updateList(sorted(set(x), key=str.lower))


def updateList(newSet):  # create/overwrite unitlist.txt
    with open('unitList.txt', 'w') as l:
        l.write(f'{newSet}')
        preFormat()


# re-format list into usable strings -- rid of the '['at the beginning and end ']' along with any white space - commas are replaced with \n
def preFormat():
    with open('unitList.txt', 'r') as f:
        g = f.read()
        g = re.sub(r'[\[\] ]', '', g)
        g = re.sub(r'(\',\')', '\n', g)
        g = re.sub(r'[\']', '', g)
    with open('unitList.txt', 'w') as h:
        h.write(g)


def blacklist():
    # really sheit way of removing links I dont know how to handle yet
    with open('unitList.txt', 'r') as u:
        remove = u.read()
        remove = re.sub(
            r'(https://allstartd\.fandom\.com/wiki/Android_18_\(D\)\n)', '', remove)
        remove = re.sub(
            r'(https://allstartd\.fandom\.com/wiki/Ant_King_\(Serious\)\n)', '', remove)
        remove = re.sub(
            r'(https://allstartd\.fandom\.com/wiki/Wish\n)', '', remove)
        remove = re.sub(
            r'(https://allstartd\.fandom\.com/wiki/Path_\(Furious\)\n)', '', remove)
        remove = re.sub(
            r'(https://allstartd\.fandom\.com/wiki/Re_One-I\n)', '', remove)
        remove = re.sub(
            r'(https://allstartd\.fandom\.com/wiki/Octo_The_Greedy\n)', '', remove)
        remove = re.sub(
            r'(https://allstartd\.fandom\.com/wiki/Jeff_\(CEO\)\n)', '', remove)
        remove = re.sub(
            r'(https://allstartd\.fandom\.com/wiki/Demon_Of_Emotion\n)', '', remove)
        remove = re.sub(
            r'(https://allstartd\.fandom\.com/wiki/The_Path_\(Final\)\n)', '', remove)
    with open('unitList.txt', 'w') as u2:
        u2.write(remove)


def main() -> None:  # intended to be ran, no return value
    fiveStar()
    sixStar()
    sevenStar()
    newUnits()
    setLinks()
    blacklist()


main()
# print(f"\nset links total: {len(links)}\n data type of : {type(links)}\n")  # check new set against old list


# print(sorted(links, key=str.lower))  # sort set by alph-lowercase


# print(f"links total: {len(links)}\n with a data type of : {type(links)}\n") # check old list against new set

end = time.time()  # stopwatch
# print(f"Took {end-start} to run")
