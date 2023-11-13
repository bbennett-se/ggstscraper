from bs4 import BeautifulSoup
import pip._vendor.requests as requests

data = []
url = 'https://www.dustloop.com/w/GGST/Sol_Badguy/Frame_Data'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

table1 = soup.find('table', attrs={'data-tooltips': ",,How this attack can be guarded. All non-throws can be air blocked.,Number of frames for this move to reach its first active frame (includes the first active frame).,Number of active frames in this attack. Values in ( ) are for inactive frames between hits of an attack.,Number of frames this move is in a recovery state before returning to neutral.,After blocking this attack&#44; how soon the attacker can act compared to the defender.<br>A positive value means the attacker can move first. Assumes the attack connects on the first active frame and is not canceled into anything else.,After getting hit by this attack&#44; how soon the attacker can act compared to the defender.<br>A positive value means the attacker can move first. Assumes the attack connects on the first active frame and is not canceled into anything else.,Attack Level generally determines the amount of hitstun&#44; blockstun&#44; and hitstop this attack will inflict; and the amount of Tension gained on hit or block.,The type of Counter Hit this attack triggers. There are four types: Very Small&#44; Small&#44; Mid&#44; and Large.,Attribute and hitbox invincibility for this move."})
tbod1 = table1.find('tbody')

rows = tbod1.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append ([ele for ele in cols if ele])

print(data)