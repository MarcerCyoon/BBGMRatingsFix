import json

'''
Fix Ratings in a BBGM JSON according to the modifications you want. The default modifications were specified by ClevelandFan and Jlebron13.
'''


# EDIT HOW MUCH YOU WANT TO CHANGE THE RATINGS HERE:
hgtChange = -1
streChange = -6
spdChange = -6
jmpChange = -6
enduChange = -18
insChange = -10
dnkChange = -7
ftChange = -9
fgChange = -10 # Mid-Range
tpChange = -6 # Three-Point
diqChange = -2
oiqChange = -6
drbChange = 2
pssChange = 3
rebChange = 3

# Change Details to Accomodate Your File
fileName = "fixExport.json"

# Open File
with open(fileName, 'r', encoding='utf-8-sig') as file:
	export = json.load(file)

players = export['players']

for player in players:
	if (player['tid'] == -3):
		continue
	else:
		player['hgt'] = max(0, player['hgt'] + hgtChange)
		player['ratings'][-1]['hgt'] = max(0, player['ratings'][-1]['hgt'] + hgtChange)
		player['ratings'][-1]['stre'] = max(0, streChange + player['ratings'][-1]['stre'])
		player['ratings'][-1]['spd'] = max(0, spdChange + player['ratings'][-1]['spd'])
		player['ratings'][-1]['jmp'] = max(0, jmpChange + player['ratings'][-1]['jmp'])
		player['ratings'][-1]['endu'] = max(0, enduChange + player['ratings'][-1]['endu'])
		player['ratings'][-1]['ins'] = max(0, insChange + player['ratings'][-1]['ins'])
		player['ratings'][-1]['dnk'] = max(0, dnkChange + player['ratings'][-1]['dnk'])
		player['ratings'][-1]['ft'] = max(0, ftChange + player['ratings'][-1]['ft'])
		player['ratings'][-1]['fg'] = max(0, fgChange + player['ratings'][-1]['fg'])
		player['ratings'][-1]['tp'] = max(0, tpChange + player['ratings'][-1]['tp'])
		player['ratings'][-1]['diq'] = max(0, diqChange + player['ratings'][-1]['diq'])
		player['ratings'][-1]['oiq'] = max(0, oiqChange + player['ratings'][-1]['oiq'])
		player['ratings'][-1]['drb'] = max(0, drbChange + player['ratings'][-1]['drb'])
		player['ratings'][-1]['pss'] = max(0, pssChange + player['ratings'][-1]['pss'])
		player['ratings'][-1]['reb'] = max(0, rebChange + player['ratings'][-1]['reb'])

# Replace Export Data with Fixed Data
export['players'] = players

# Create a new file with fixed ratings
with open("fixedExport.json", 'w') as file:
	json.dump(export, file)


print("Done.")