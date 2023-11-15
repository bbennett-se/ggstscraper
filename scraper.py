from bs4 import BeautifulSoup
import pip._vendor.requests as requests
import colorama
from colorama import init
init(convert=True)
from colorama import Fore

menu = {}
menu['1'] = "Sol Badguy"
menu['2'] = "Ky Kiske"
menu['3'] = "May"
menu['4'] = "Axl Low"
menu['5'] = "Chipp Zanuff"
menu['6'] = "Potemkin"
menu['7'] = "Faust"
menu['8'] = "Millia Rage"
menu['9'] = "Zato=1"
menu['10'] = "Ramlethal Valentine"
menu['11'] = "Leo Whitefang"
menu['12'] = "Nagoriyuki"
menu['13'] = "Giovanna"
menu['14'] = "Anji Mito"
menu['15'] = "I-No"
menu['16'] = "Goldlewis Dickinson"
menu['17'] = "Jack-o Valentine"
menu['18'] = "Happy Chaos"
menu['19'] = "Baiken"
menu['20'] = "Testament"
menu['21'] = "Bridget"
menu['22'] = "Sin Kiske"
menu['23'] = "Bedman?"
menu['24'] = "Asuka R#"
menu['25'] = "Johnny"

data = []
url = ''

while True:
    options=menu.keys()
    options.sort()
    for entry in options:
        print(entry, menu[entry])
        
    selection = raw_input("Select Your Character:")
    if selection == '1':
        url = 'https://www.dustloop.com/w/GGST/Sol_Badguy/Frame_Data'
    elif selection == '2':
        url = 'https://www.dustloop.com/w/GGST/Ky_Kiske/Frame_Data'
    elif selection == '3':
        url = 'https://www.dustloop.com/w/GGST/Ky_Kiske/Frame_Data'
    elif selection == '4':
        url = 'https://www.dustloop.com/w/GGST/May/Frame_Data'
    elif selection == '5':
        url = 'https://www.dustloop.com/w/GGST/Axl_Low/Frame_Data'
    elif selection == '6':
        url = 'https://www.dustloop.com/w/GGST/Chipp_Zanuff/Frame_Data'
    elif selection == '7':
        url = 'https://www.dustloop.com/w/GGST/Potemkin/Frame_Data'
    elif selection == '8':
        url = 'https://www.dustloop.com/w/GGST/Faust/Frame_Data'
    elif selection == '9':
        url = 'https://www.dustloop.com/w/GGST/Millia_Rage/Frame_Data'
    elif selection == '10':
        url = 'https://www.dustloop.com/w/GGST/Zato-1/Frame_Data'
    elif selection == '11':
        url = 'https://www.dustloop.com/w/GGST/Ramlethal_Valentine/Frame_Data'
    elif selection == '12':
        url = 'https://www.dustloop.com/w/GGST/Leo_Whitefang/Frame_Data'
    elif selection == '13':
        url = 'https://www.dustloop.com/w/GGST/Nagoriyuki/Frame_Data'
    elif selection == '14':
        url = 'https://www.dustloop.com/w/GGST/Giovanna/Frame_Data'
    elif selection == '15':
        url = 'https://www.dustloop.com/w/GGST/Anji_Mito/Frame_Data'
    elif selection == '16':
        url = 'https://www.dustloop.com/w/GGST/I-No/Frame_Data'
    elif selection == '17':
        url = 'https://www.dustloop.com/w/GGST/Goldlewis_Dickinson/Frame_Data'
    elif selection == '18':
        url = 'https://www.dustloop.com/w/GGST/Jack-O/Frame_Data'
    elif selection == '19':
        url = 'https://www.dustloop.com/w/GGST/Happy_Chaos/Frame_Data'
    elif selection == '20':
        url = 'https://www.dustloop.com/w/GGST/Baiken/Frame_Data'
    elif selection == '21':
        url = 'https://www.dustloop.com/w/GGST/Testament/Frame_Data'
    elif selection == '22':
        url = 'https://www.dustloop.com/w/GGST/Bridget/Frame_Data'
    elif selection == '23':
        url = 'https://www.dustloop.com/w/GGST/Sin_Kiske/Frame_Data'
    elif selection == '24':
        url = 'https://www.dustloop.com/w/GGST/Bedman/Frame_Data'
    elif selection == '25':
        url = 'https://www.dustloop.com/w/GGST/Asuka_R/Frame_Data'



    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    table1 = soup.find('table', attrs={'data-tooltips': ",,How this attack can be guarded. All non-throws can be air blocked.,Number of frames for this move to reach its first active frame (includes the first active frame).,Number of active frames in this attack. Values in ( ) are for inactive frames between hits of an attack.,Number of frames this move is in a recovery state before returning to neutral.,After blocking this attack&#44; how soon the attacker can act compared to the defender.<br>A positive value means the attacker can move first. Assumes the attack connects on the first active frame and is not canceled into anything else.,After getting hit by this attack&#44; how soon the attacker can act compared to the defender.<br>A positive value means the attacker can move first. Assumes the attack connects on the first active frame and is not canceled into anything else.,Attack Level generally determines the amount of hitstun&#44; blockstun&#44; and hitstop this attack will inflict; and the amount of Tension gained on hit or block.,The type of Counter Hit this attack triggers. There are four types: Very Small&#44; Small&#44; Mid&#44; and Large.,Attribute and hitbox invincibility for this move."})
    tbod1 = table1.find('tbody')

    rows = tbod1.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        count = 0
        for col in cols: 
            match count:
                case 1:
                    print("Input: ", end = "")
                    fore = ""
                    if col.__contains__("P"):
                        fore = Fore.LIGHTRED_EX
                    elif col.__contains__("K"):
                        fore = Fore.CYAN
                    elif col.__contains__("S"):
                        fore = Fore.GREEN
                    elif col.__contains__("HS"):
                        fore = Fore.RED
                    else:
                        fore = Fore.YELLOW
                        
                    print(fore + col, end = " | ")
                case 2:
                    print("Damage: ", end = "")
                    print(col, end = " | ")
                case 3:
                    print("Guard: ", end = "")
                    print(col, end = " | ")
                case 4:
                    print("Startup: ", end = "")
                    print(col, end = " | ")
                case 5:
                    print("Active: ", end = "")
                    print(col, end = " | ")
                case 6:
                    print("Recovery: ", end = "")
                    print(col, end = " | ")
                case 7:
                    print("On-Block: ", end = "")
                    print(col, end = " | ")
                case 8:
                    print("On-Hit: ", end = "")
                    print(col, end = " | ")
                case 9:
                    print("Level: ", end = "")
                    print(col, end = " | ")
                case 10:
                    print("Counter Type: ", end = "")
                    print(col, end = " | ")
                case 11:
                    print("Invuln: ", end = "")
                    if(col == ""): 
                        print("N/A", end = " | ")
                    else:
                        print(col, end = " | ")
                case 12:
                    print("Proration: ", end = "")
                    print(col, end = " | ")
                case 12:
                    print("R.I.S.C. Gain: ", end = "")
                    print(col, end = " | ")
                case 12:
                    print("R.I.S.C Loss: ", end = "")
                    print(col, end = " | ")
            count +=1
        print('')
        print('')