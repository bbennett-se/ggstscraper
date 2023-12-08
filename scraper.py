import time
from bs4 import BeautifulSoup
import pip._vendor.requests as requests
import colorama
from colorama import init
init(convert=True)
from colorama import Fore, Style

line = "==============================================================================="
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
menu['26'] = "Elphelt Valentine"

data = []
url = ''
while True:
    #prints character menu
    print(" 1. Sol Badguy           11. Leo WhiteFang        21. Bridget")
    print(" 2. Ky Kiske             12. Nagoriyuki           22. Sin Kiske")
    print(" 3. May                  13. Giovanna             23. Bedman?")
    print(" 4. Axl Low              14. Anji Mito            24. Asuka R#")
    print(" 5. Chipp Zanuff         15. I-No                 25. Johnny")
    print(" 6. Potemkin             16. Goldlewis Dickinson  26. Elphelt Valentine")
    print(" 7. Faust                17. Jack-o Valentine      0. Quit")
    print(" 8. Millia Rage          18. Happy Chaos")
    print(" 9. Zato-1               19. Baiken")
    print("10. Ramlethal Valentine  20. Testament")
    
        
    selection = input("Select Your Character: ")
    #takes character input and sets url for scraping
    if selection == '0':
       exit()
    elif selection == '1':
        url = 'https://www.dustloop.com/w/GGST/Sol_Badguy/Frame_Data'
    elif selection == '2':
        url = 'https://www.dustloop.com/w/GGST/Ky_Kiske/Frame_Data'
    elif selection == '3':
        url = 'https://www.dustloop.com/w/GGST/May/Frame_Data'
    elif selection == '4':
        url = 'https://www.dustloop.com/w/GGST/Axl_Low/Frame_Data'
    elif selection == '5':
        url = 'https://www.dustloop.com/w/GGST/Chipp_Zanuff/Frame_Data'
    elif selection == '6':
        url = 'https://www.dustloop.com/w/GGST/Potemkin/Frame_Data'
    elif selection == '7':
        url = 'https://www.dustloop.com/w/GGST/Faust/Frame_Data'
    elif selection == '8':
        url = 'https://www.dustloop.com/w/GGST/Millia_Rage/Frame_Data'
    elif selection == '9':
        url = 'https://www.dustloop.com/w/GGST/Zato-1/Frame_Data'
    elif selection == '10':
        url = 'https://www.dustloop.com/w/GGST/Ramlethal_Valentine/Frame_Data'
    elif selection == '11':
        url = 'https://www.dustloop.com/w/GGST/Leo_Whitefang/Frame_Data'
    elif selection == '12':
        url = 'https://www.dustloop.com/w/GGST/Nagoriyuki/Frame_Data'
    elif selection == '13':
        url = 'https://www.dustloop.com/w/GGST/Giovanna/Frame_Data'
    elif selection == '14':
        url = 'https://www.dustloop.com/w/GGST/Anji_Mito/Frame_Data'
    elif selection == '15':
        url = 'https://www.dustloop.com/w/GGST/I-No/Frame_Data'
    elif selection == '16':
        url = 'https://www.dustloop.com/w/GGST/Goldlewis_Dickinson/Frame_Data'
    elif selection == '17':
        url = 'https://www.dustloop.com/w/GGST/Jack-O/Frame_Data'
    elif selection == '18':
        url = 'https://www.dustloop.com/w/GGST/Happy_Chaos/Frame_Data'
    elif selection == '19':
        url = 'https://www.dustloop.com/w/GGST/Baiken/Frame_Data'
    elif selection == '20':
        url = 'https://www.dustloop.com/w/GGST/Testament/Frame_Data'
    elif selection == '21':
        url = 'https://www.dustloop.com/w/GGST/Bridget/Frame_Data'
    elif selection == '22':
        url = 'https://www.dustloop.com/w/GGST/Sin_Kiske/Frame_Data'
    elif selection == '23':
        url = 'https://www.dustloop.com/w/GGST/Bedman/Frame_Data'
    elif selection == '24':
        url = 'https://www.dustloop.com/w/GGST/Asuka_R/Frame_Data'
    elif selection == '25':
        url = 'https://www.dustloop.com/w/GGST/Johnny/Frame_Data'
    elif selection == '26':
        url = 'https://www.dustloop.com/w/GGST/Elphelt_Valentine/Frame_Data'


    #scrapes frame data page and parses the html
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #tables on the website are formatted weird
    #takes two result sets with frame data and then combines them into one result set
    tables = soup.find_all('table', {'data-tooltips': ",,How this attack can be guarded. All non-throws can be air blocked.,Number of frames for this move to reach its first active frame (includes the first active frame).,Number of active frames in this attack. Values in ( ) are for inactive frames between hits of an attack.,Number of frames this move is in a recovery state before returning to neutral.,After blocking this attack&#44; how soon the attacker can act compared to the defender.<br>A positive value means the attacker can move first. Assumes the attack connects on the first active frame and is not canceled into anything else.,After getting hit by this attack&#44; how soon the attacker can act compared to the defender.<br>A positive value means the attacker can move first. Assumes the attack connects on the first active frame and is not canceled into anything else.,Attack Level generally determines the amount of hitstun&#44; blockstun&#44; and hitstop this attack will inflict; and the amount of Tension gained on hit or block.,The type of Counter Hit this attack triggers. There are four types: Very Small&#44; Small&#44; Mid&#44; and Large.,Attribute and hitbox invincibility for this move."})
    specials = soup.find_all('table', {'data-tooltips': ",,,How this attack can be guarded. All non-throws can be air blocked.,Number of frames for this move to reach its first active frame (includes the first active frame).,Number of active frames in this attack. Values in ( ) are for inactive frames between hits of an attack.,Number of frames this move is in a recovery state before returning to neutral.,After blocking this attack&#44; how soon the attacker can act compared to the defender.<br>A positive value means the attacker can move first. Assumes the attack connects on the first active frame and is not canceled into anything else.,After getting hit by this attack&#44; how soon the attacker can act compared to the defender.<br>A positive value means the attacker can move first. Assumes the attack connects on the first active frame and is not canceled into anything else.,Attack Level generally determines the amount of hitstun&#44; blockstun&#44; and hitstop this attack will inflict; and the amount of Tension gained on hit or block.,The type of Counter Hit this attack triggers. There are four types: Very Small&#44; Small&#44; Mid&#44; and Large.,Attribute and hitbox invincibility for this move."})
    specials.reverse()
    for special in specials:
        tables.insert(1, special)

    #tracks current table to manage data formatting
    tcount = 0

    #iterates through result set and prints frame data
    for table in tables:
        rows = table.find_all('tr')
        tcount +=1
        
        #prints normals
        if tcount == 1:
            
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                count = 0
                for col in cols: 
                    match count:
                        case 1:
                            print(line)
                            print("Input: ", end = "")
                            print(col)
                            print('')
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
                            print(col)
                            print('')
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
                            print(col)
                            print('')
                        case 11:
                            print("Invuln: ", end = "")
                            if(col == ""): 
                                print("N/A", end = " | ")
                            else:
                                print(col, end = " | ")
                        case 12:
                            print("Proration: ", end = "")
                            print(col, end = " | ")
                        case 13:
                            print("R.I.S.C. Gain: ", end = "")
                            print(col, end = " | ")
                        case 14:
                            print("R.I.S.C Loss: ", end = "")
                            print(col, end = " | ")
                    count +=1
                print('')
                print('')

        #prints special moves
        elif tcount == 2:
            for row in rows:
                cols = row.find_all('td')
                cols = [ele2.text.strip() for ele2 in cols]
                count = 0
                for col in cols: 
                    if col != "":
                        match count:
                            case 1:
                                print(line)
                                print("Input: ", end = "")

                                print(col, end = " | ")
                            case 2:
                                print("Name: ", end = "")
                                print(col)
                                print('')
                            case 3:
                                print("Damage: ", end = "")
                                print(col, end = ' | ')
                            case 4:
                                print("Guard: ", end = "")
                                print(col, end = ' | ')
                            case 5:
                                print("Startup: ", end = "")
                                print(col, end = " | ")
                            case 6:
                                print("Active: ", end = "")
                                print(col, end = " | ")
                            case 7:
                                print("Recovery: ", end = "")
                                print(col)
                                print('')
                            case 8:
                                print("On-Block: ", end = "")
                                print(col, end = " | ")
                            case 9:
                                print("On-Hit: ", end = "")
                                print(col, end = " | ")
                                print('')
                            case 10:
                                print("Level: ", end = "")
                                print(col, end = " | ")
                            case 11:
                                print("Counter Type: ", end = "")
                                print(col)
                                print('')
                            case 12:
                                print("Invuln: ", end = "")
                                if(col == ""): 
                                    print("N/A", end = " | ")
                                else:
                                    print(col, end = " | ")
                            case 13:
                                print("Proration: ", end = "")
                                print(col, end = " | ")
                            case 14:
                                print("R.I.S.C. Gain: ", end = "")
                                print(col, end = " | ")
                            case 15:
                                print("R.I.S.C Loss: ", end = "")
                                print(col, end = " | ")
                    count +=1
                print('')
                print('')

        #prints overdrives
        elif tcount == 3:
            for row in rows:
                cols = row.find_all('td')
                cols = [ele3.text.strip() for ele3 in cols]
                count = 0
                for col in cols: 
                    if col != "":
                        match count:
                            case 1:
                                print(line)
                                print("Input: ", end = "")
                                print(col, end = " | ")
                            case 2:
                                print("Name: ", end = "")
                                print(col)
                                print('')
                            case 3:
                                print("Damage: ", end = "")
                                print(col, end = ' | ')
                            case 4:
                                print("Guard: ", end = "")
                                print(col, end = " | ")
                            case 5:
                                print("Startup: ", end = "")
                                print(col, end = " | ")
                            case 6:
                                print("Active: ", end = "")
                                print(col, end = " | ")
                            case 7:
                                print("Recovery: ", end = "")
                                print(col)
                                print('')
                            case 8:
                                print("On-Block: ", end = "")
                                print(col, end = " | ")
                            case 9:
                                print("On-Hit: ", end = "")
                                print(col, end = " | ")
                                print('')
                            case 10:
                                print("Level: ", end = "")
                                print(col, end = " | ")
                            case 11:
                                print("Counter Type: ", end = "")
                                print(col)
                                print('')
                            case 12:
                                print("Invuln: ", end = "")
                                if(col == ""): 
                                    print("N/A", end = " | ")
                                else:
                                    print(col, end = " | ")
                            case 13:
                                print("Proration: ", end = "")
                                print(col, end = " | ")
                            case 14:
                                print("R.I.S.C. Gain: ", end = "")
                                print(col, end = " | ")
                            case 15:
                                print("R.I.S.C Loss: ", end = "")
                                print(col, end = " | ")
                    count +=1
                print('')
                print('')

        #prints throws/universal mechanics(Wild Assault, etc.)
        elif tcount == 4:
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                count = 0
                for col in cols: 
                    if col != "":
                        match count:
                            case 1:
                                print(line)
                                print("Name: ", end = "")
                                print(col)
                                print('')
                            case 2:
                                print("Damage: ", end = "")
                                print(col, '')
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
                                print(col)
                                print('')
                            case 7:
                                print("On-Block: ", end = "")
                                print(col, end = " | ")
                            case 8:
                                print("On-Hit: ", end = "")
                                print(col, end = " | ")
                                print('')
                            case 9:
                                print("Level: ", end = "")
                                print(col, end = " | ")
                            case 10:
                                print("Counter Type: ", end = "")
                                print(col)
                                print('')
                            case 11:
                                print("Invuln: ", end = "")
                                if(col == ""): 
                                    print("N/A", end = " | ")
                                else:
                                    print(col, end = " | ")
                            case 12:
                                print("Proration: ", end = "")
                                print(col, end = " | ")
                            case 13:
                                print("R.I.S.C. Gain: ", end = "")
                                print(col, end = " | ")
                            case 14:
                                print("R.I.S.C Loss: ", end = "")
                                print(col, end = " | ")                    
                    count +=1
                print('')
                print('')
    time.sleep(1)