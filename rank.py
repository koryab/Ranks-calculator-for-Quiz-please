def rank(team,i,gametype, promoted):
	if gametype == 0: #classic
		previous_rank = team[i][2]
		if team[i][1] < 100: team[i][2] = None
		elif team[i][1] >= 100 and team[i][1] < 250: team[i][2] = 'serg'
		elif team[i][1] >= 250 and team[i][1] < 500: team[i][2] = 'liet'
		elif team[i][1] >= 500 and team[i][1] < 1000: team[i][2] = 'gener'
		elif team[i][1] >= 1000 and team[i][1] < 2000: team[i][2] = 'rambo'
		elif team[i][1] >= 2000 and team[i][1] < 6000: team[i][2] = 'chuck'
		else : team[i][2] = 'nedosyag'
		if team[i][2] != previous_rank: promoted[team[i][2]].append(i)
	elif gametype == 1: #kim
		previous_rank = team[i][2]
		if team[i][1] < 100: team[i][2] = None
		elif team[i][1] >= 100 and team[i][1] < 250: team[i][2] = 'kim1'
		elif team[i][1] >= 250 and team[i][1] < 500: team[i][2] = 'kim2'
		elif team[i][1] >= 500 and team[i][1] < 1000: team[i][2] = 'kim3'
		elif team[i][1] >= 1000 and team[i][1] < 1500: team[i][2] = 'kim4'
		elif team[i][1] >= 1500 and team[i][1] < 2000: team[i][2] = 'kim5'
		elif team[i][1] >= 2000 and team[i][1] < 3000: team[i][2] = 'kim6'
		elif team[i][1] >= 3000 and team[i][1] < 5000: team[i][2] = 'kim7'
		else : team[i][2] = 'kim8'
		if team[i][2] != previous_rank: promoted[team[i][2]].append(i)
	elif gametype == 2: #teens
		previous_rank = team[i][2]
		if team[i][1] < 20: team[i][2] = None
		elif team[i][1] >= 20 and team[i][1] < 50: team[i][2] = 'lvl1'
		elif team[i][1] >= 50 and team[i][1] < 100: team[i][2] = 'lvl2'
		elif team[i][1] >= 100 and team[i][1] < 150: team[i][2] = 'lvl3'
		elif team[i][1] >= 150 and team[i][1] < 200: team[i][2] = 'lvl4'
		elif team[i][1] >= 200 and team[i][1] < 250: team[i][2] = 'lvl5'
		elif team[i][1] >= 250 and team[i][1] < 300: team[i][2] = 'lvl6'
		elif team[i][1] >= 300 and team[i][1] < 500: team[i][2] = 'lvl7'
		elif team[i][1] >= 500 and team[i][1] < 1000: team[i][2] = 'lvl8'
		elif team[i][1] >= 1000 and team[i][1] < 3000: team[i][2] = 'lvl9'
		else : team[i][2] = 'lvl10'
		if team[i][2] != previous_rank: promoted[team[i][2]].append(i)
	elif gametype == 3:	#stream
		previous_rank = team[i][2]
		if team[i][1] < 50: team[i][2] = None
		elif team[i][1] >= 50 and team[i][1] < 100: team[i][2] = 'serg-strim'
		elif team[i][1] >= 100 and team[i][1] < 200: team[i][2] = 'liet-strim'
		elif team[i][1] >= 200 and team[i][1] < 400: team[i][2] = 'gener-strim'
		elif team[i][1] >= 400 and team[i][1] < 600: team[i][2] = 'marsh-strim'
		elif team[i][1] >= 600 and team[i][1] < 800: team[i][2] = 'rambo-strim'
		elif team[i][1] >= 800 and team[i][1] < 1000: team[i][2] = 'chuck-strim'
		elif team[i][1] >= 1000 and team[i][1] < 5000: team[i][2] = 'nedosyag-strim'
		else : team[i][2] = 'ilon-strim'
		if team[i][2] != previous_rank: promoted[team[i][2]].append(i)

if __name__ == '__main__':
	team = {'tima':[1,49,'serg'],'tima2':[2,8000,'serg'],'tima3':[20,1002,'rambo']}
	gameres = ['tima2','tima3']
	print(rank(team, gameres,'kim'))
	print(team)