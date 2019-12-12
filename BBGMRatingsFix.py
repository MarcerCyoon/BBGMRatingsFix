import json

'''
Fix Ratings in a BBGM JSON according to the modifications you want:
hgt -1
stre -6
spd -6
jmp -6
end -18
ins -10
dnk -7
ft -9
midrange -10
threes -6
oiq -6
diq -2
drb +2
pss +3
reb +3
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
currentSeason = 2025

# Open File
with open(fileName, 'r', encoding='utf-8-sig') as file:
	export = json.load(file)

players = export['players']

print(players[56]['firstName'] + " " + players[56]['lastName'])
print(players[56]['ratings']['season' == currentSeason])

for player in players:
	if (player['tid'] == -3):
		continue
	else:
		player['hgt'] = max(0, player['hgt'] + hgtChange)
		player['ratings']['season' == currentSeason]['hgt'] = max(0, player['ratings']['season' == currentSeason]['hgt'] + hgtChange)
		player['ratings']['season' == currentSeason]['stre'] = max(0, streChange + player['ratings']['season' == currentSeason]['stre'])
		player['ratings']['season' == currentSeason]['spd'] = max(0, spdChange + player['ratings']['season' == currentSeason]['spd'])
		player['ratings']['season' == currentSeason]['jmp'] = max(0, jmpChange + player['ratings']['season' == currentSeason]['jmp'])
		player['ratings']['season' == currentSeason]['endu'] = max(0, enduChange + player['ratings']['season' == currentSeason]['endu'])
		player['ratings']['season' == currentSeason]['ins'] = max(0, insChange + player['ratings']['season' == currentSeason]['ins'])
		player['ratings']['season' == currentSeason]['dnk'] = max(0, dnkChange + player['ratings']['season' == currentSeason]['dnk'])
		player['ratings']['season' == currentSeason]['ft'] = max(0, ftChange + player['ratings']['season' == currentSeason]['ft'])
		player['ratings']['season' == currentSeason]['fg'] = max(0, fgChange + player['ratings']['season' == currentSeason]['fg'])
		player['ratings']['season' == currentSeason]['tp'] = max(0, tpChange + player['ratings']['season' == currentSeason]['tp'])
		player['ratings']['season' == currentSeason]['diq'] = max(0, diqChange + player['ratings']['season' == currentSeason]['diq'])
		player['ratings']['season' == currentSeason]['oiq'] = max(0, oiqChange + player['ratings']['season' == currentSeason]['oiq'])
		player['ratings']['season' == currentSeason]['drb'] = max(0, drbChange + player['ratings']['season' == currentSeason]['drb'])
		player['ratings']['season' == currentSeason]['pss'] = max(0, pssChange + player['ratings']['season' == currentSeason]['pss'])
		player['ratings']['season' == currentSeason]['reb'] = max(0, rebChange + player['ratings']['season' == currentSeason]['reb'])

print(players[56]['ratings']['season' == currentSeason])

# Replace Export Data with Fixed Data
export['players'] = players

# Create a new file with fixed ratings
with open("fixedExport.json", 'w') as file:
	json.dump(export, file)


print("Done.")