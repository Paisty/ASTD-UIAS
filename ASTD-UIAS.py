from bs4 import BeautifulSoup as BS
import time
import requests as rq
import re


start = time.time()  # stopwatch


with open('unitList.txt', 'r') as links:  # read file
    readLinks = [url.strip('\n') for url in links]


def unitList(read=readLinks):  # using as Main

    unitWipe()    # wipe files

    for unitList in read:     # unitList runs list through BS
        unitPage = rq.get(unitList).content
        soup = BS(unitPage, 'lxml')
        unitTitle(soup)
        unitCost(soup)
        unitDamage(soup)
        unitSpaInit(soup)
        unitStatusInit(soup)
        unitTypeInit(soup)
        unitEnchantInit(soup)


def unitStatusInit(_):  # Init narrows search before searching begins
    for _ in _.find_all(id='mw-customcollapsible-statsBoxMax'):
        unitStatus(_)


def unitTypeInit(_):  # Init narrows search before searching begins
    for _ in _.find_all(attrs={'data-source': 'tower_type'}):
        unitType(_.text.rstrip('\n'))


def unitEnchantInit(_):  # Init narrows search before searching begins
    for _ in _.find_all(attrs={'data-source': 'enchant'}):
        unitEnchant(_)


def unitTitle(_):
    # grab unit title -- needs attention -> add damage modifier to name
    for _ in _.find_all('h2', class_='pi-item pi-item-spacing pi-title pi-secondary-background'):
        unitKey(_.text + ':')


def unitCost(_):
    # grab unit cost -- needs attention -> find a way to remove non-orb stats
    for _ in _.find_all(id='mw-customcollapsible-statsBoxMax'):
        _ = _.find(
            'span', class_='Fw(b)-Th-L C(Cash) Tsh(Game) Fw(500)-Th-L')
        scrubCost(_)


def unitDamage(_):
    # grab unit damage -- needs attention -> find a way to remove non-orb stats
    for _ in _.find_all(id='mw-customcollapsible-statsBoxMax'):
        _ = str(_('span', class_='mw-collapsible'))
        scrubDamage(_)


def unitSpaInit(_):
    for _ in _.find_all(id='mw-customcollapsible-statsBoxMax'):
        customSearch(_)


def customSearch(_):
    # custom if/else statement for soup
    if re.search('Stats-Box-ON-ORB', str(_)):
        for _ in _.find_all(id='Stats-Box-ON-ORB'):
            unitSpaOrb(_)
    else:
        unitSpa(_)


def unitSpa(_):
    # grab unit SPA -- needs attention -> find a way to remove non-orb stats (change str(read when applicable)
    #    for _ in _.find_all(id='mw-customcollapsible-statsBoxMax'):
    _ = str(_('div', class_="style_Stats-Box__container"))
    for attackSpeed in re.findall(r'(SPA:.*<)', _):
        scrubSpa(attackSpeed)


def unitSpaOrb(_):
    _ = str(_('div', class_="style_Stats-Box__container"))
    for attackSpeed in re.findall(r'(SPA:.*<)', _):
        scrubSpaOrb(attackSpeed)


def unitStatus(_):
    if re.search(r'(black flame)|(Black Flame)', str(_)):
        unitSts('BF')
    elif re.search(r'(bleed)|(Bleed)', str(_)):
        unitSts('Bld')
    elif re.search(r'(sunburn)|(SunBurn)', str(_)):
        unitSts('Sbrn')
    elif re.search(r'(burn)|(Burn)', str(_)):
        unitSts('Brn')
    elif re.search(r'(rupture)|(Rupture)', str(_)):
        unitSts('Rup')
    elif re.search(r'(poison)|(Poison)', str(_)):
        unitSts('Psn')
    else:
        unitSts('N/A')


def unitType(_):
    if re.search('Ground', str(_)):
        unitTyp(_)
    elif re.search('Air', str(_)):
        unitTyp(_)
    elif re.search('Hill', str(_)):
        unitTyp(_)
    elif re.search('Hybrid', str(_)):
        unitTyp(_)
    elif re.search('Controllable', str(_)):
        unitTyp(_)
    else:
        unitTyp('N/A')


def unitEnchant(_):
    if re.search('Electric', str(_)):
        unitEnch('Electric')
    elif re.search('Holy', str(_)):
        unitEnch('Holy')
    elif re.search('Dark', str(_)):
        unitEnch('Dark')
    elif re.search('Fire', str(_)):
        unitEnch('Fire')
    elif re.search('Water', str(_)):
        unitEnch('Water')
    elif re.search('Nature', str(_)):
        unitEnch('Nature')
    else:
        unitEnch('N/A')


def scrubDamage(_):
    # scrub text; remove unwanted characters
    _ = re.sub(r'[\[\]]', '', str(_))
    _ = re.sub(
        r'<span class="mw-collapsible" id="mw-customcollapsible-Music">', '', str(_))
    _ = re.sub(r'<.*', '', str(_))
    _ = re.sub(r'[., ]', '', str(_))
    _ = re.sub(r'\(.*.\)', '', str(_))
    unitDValue(_)


def scrubCost(_):
    # scrub text; remove unwanted characters
    _ = re.sub(
        r'<span class=\"Fw\(b\)-Th\-L C\(Cash\) Tsh\(Game\) Fw\(500\)-Th\-L\">', '', str(_))
    _ = re.sub(r'[,</span>None]', '', str(_))
    unitCValue(_)


def scrubSpa(_):
    # scrub text; remove unwanted characters
    _ = re.sub(r'[.NoneSPA: ]', '', str(_))
    _ = re.sub(r'<.*', '', str(_))
    unitSValue(_)


def scrubSpaOrb(_):
    # scrub text; remove unwanted characters ORBS
    _ = re.sub(r'[.NoneSPA: ]', '', str(_))
    _ = re.sub(r'<.*', '', str(_))
    unitSValueOrb(_)


def unitWipe():
    # wipe unit files -- needs attention
    print('', file=open('Damage.csv', 'w'), end='')
    print('', file=open('Cost.csv', 'w'), end='')
    print('', file=open('SPA.csv', 'w'), end='')
    print('', file=open('Status.csv', 'w'), end='')
    print('', file=open('Type.csv', 'w'), end='')
    print('', file=open('Enchant.csv', 'w'), end='')


def inputNewline():
    # create a /n for values -- needs attention
    print('', file=open('Damage.csv', 'a'))
    print('', file=open('Cost.csv', 'a'))
    print('', file=open('SPA.csv', 'a'))


def unitKey(file):
    with open('Damage.csv', 'a') as f:
        f.write(f'\n{file}')
    with open('Cost.csv', 'a') as f:
        f.write(f'\n{file}')
    with open('SPA.csv', 'a') as f:
        f.write(f'\n{file}')
    with open('Status.csv', 'a') as f:
        f.write(f'\n{file}')
    with open('Enchant.csv', 'a') as f:
        f.write(f'\n{file}')


def unitDValue(damage):
    with open('Damage.csv', 'a') as f:
        f.write(f'{damage},')


def unitCValue(cost):
    with open('Cost.csv', 'a') as f:
        f.write(f'{cost},')


def unitSValue(spa):
    with open('SPA.csv', 'a') as f:
        f.write(f'{spa},')


def unitSValueOrb(_):
    with open('SPA.csv', 'a') as f:
        f.write(f',{_},')


def unitSts(_):
    with open('Status.csv', 'a') as f:
        f.write(f'{_},')


def unitTyp(_):
    with open('Type.csv', 'a') as f:
        f.write(f'{_},')


def unitEnch(_):
    with open('Enchant.csv', 'a') as f:
        f.write(f'{_},')


def scrubCsvD():
    with open('Damage.csv', 'r') as D:
        scrubD = D.read()
        scrubD = re.sub(r'\n', '', scrubD, count=1)
        scrubD = re.sub(r',{3,}$', ',', scrubD, count=0, flags=re.M)
        scrubD = re.sub(r':.*,{3}', ',', scrubD)
        scrubD = re.sub(r':', '', scrubD)
        scrubD = re.sub(r',{2,}', ',', scrubD)
    with open('Damage.csv', 'w') as D:
        D.write(scrubD)


def scrubCsvC():
    with open('Cost.csv', 'r') as C:
        scrubC = C.read()
        scrubC = re.sub(r'\n', '', scrubC, count=1)
        scrubC = re.sub(r',{2,}', ',', scrubC)
        scrubC = re.sub(r':', '', scrubC)
    with open('Cost.csv', 'w') as C:
        C.write(scrubC)


def scrubCsvS():
    with open('SPA.csv', 'r') as S:
        scrubS = S.read()
        scrubS = re.sub(r'\n', '', scrubS, count=1)
        scrubS = re.sub(r':.*?.,{2}', ',', scrubS, re.U)
        scrubS = re.sub(r':', ',', scrubS)
        scrubS = re.sub(r',,', ',', scrubS)
    with open('SPA.csv', 'w') as S:
        S.write(scrubS)


def scrubSts():
    with open('Status.csv', 'r') as S:
        scrubS = S.read()
        scrubS = re.sub(r'\n', '', scrubS, count=1)
        scrubS = re.sub(r':', ',', scrubS)
        scrubS = re.sub(r'(Card Collector, Ci)', 'Card Collector Ci', scrubS)
        scrubS = re.sub(r'(N/A,\n)', '\n', scrubS)
    with open('Status.csv', 'w') as S:
        S.write(scrubS)


def scrubType():
    with open('Type.csv', 'r') as S:
        scrubT = S.read()
        scrubT = re.sub(r'\n', '', scrubT, count=2)
        scrubT = re.sub(r'Tower Type', '', scrubT)
        scrubT = re.sub(r',', '', scrubT)
        scrubT = re.sub(r'\n$', '', scrubT, flags=re.M)
    with open('Type.csv', 'w') as S:
        S.write(scrubT)


def scrubEnchant():
    with open('Enchant.csv', 'r') as S:
        scrubE = S.read()
        scrubE = re.sub(r'\n', '', scrubE, count=1)
        scrubE = re.sub(r'Enchant', 'w', scrubE)
        scrubE = re.sub(r',', '', scrubE)
        scrubE = re.sub(r':', ',', scrubE)
    with open('Enchant.csv', 'w') as S:
        S.write(scrubE)


unitList()
scrubCsvD()
scrubCsvC()
scrubCsvS()
scrubSts()
scrubType()
scrubEnchant()


end = time.time()
print(f'Time taken to run the code was {end-start} seconds')


# def unitDamage(list):
#    # grab unit damage -- interesting way to do dmg
#    for upgrade in list.find_all(id='mw-customcollapsible-statsBoxMax'):
#        damage = str(upgrade(string=re.compile('[0-9a-zA-Z]')))
#        print(damage)
