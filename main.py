import sys
from PyQt5 import QtWidgets
import design
import tables_operations as top
import rank

class windowApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
	"""docstring for windowApp"""
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.faq_btn.clicked.connect(self.instructions)
		self.overall_browse_btn.clicked.connect(self.browse_overall)
		self.overall_clear_btn.clicked.connect(self.clear_overall_line)
		self.season_browse_btn.clicked.connect(self.browse_season)
		self.season_clear_btn.clicked.connect(self.clear_season_line)
		self.games_browse_btn.clicked.connect(self.browse_games)
		self.games_clear_btn.clicked.connect(self.clear_games_line)
		self.exit_btn.clicked.connect(sys.exit)
		self.action_btn.clicked.connect(self.action)
		self.overall_line.setReadOnly(True)
		self.season_line.setReadOnly(True)
		self.games_line.setReadOnly(True)
		self.msg_plain.setReadOnly(True)

	def instructions(self):
		self.msg_plain.clear()
		self.msg_plain.setPlainText("Программа создана для подсчёта рейтингов КВИЗ,ПЛИЗ!\n\n"+
		"Как посчитать?\n 1. Необходимо выбрать файлы с общим рейтингом, рейтингом сезона и итогами игры. Для этого нажми кнопку \"Выбор файла\" под соответствующим полем."
		+"Откроется окно файловой системы, где можно будет найти и выбрать файл(ы). Если не выбран файл с рейтингом сезона,"+
		" то новый рейтинг сезона будет сформирован из итогов игры. Можно выбирать несколько файлов с итогами игры, например все игры за неделю.\n"+
		"3. После выбора файлов нажми кнопку \"Посчитай,плиз!\". Программа сделает свою работу и запросит у тебя места сохранения и названия"+
		" для новых файлов с общим рейтингом и рейтингом сезона, открыв поочередно два окна:" + 
		"\"Сохранить файл с общим рейтингом\" и \"Сохранить файл с рейтингом сезона\", соответственно. По окончании своей работы в прямоугольном поле будет выведено сообщение "+
		"\"ГОТОВО\" и список команд с повышениями, если таковые имеются. Если рейтинг сезона не требуется, его подсчёт можно отключить.\n"+ 
		"4. Открой эти файлы.\n5. PROFIT! Проделав все шаги предыдущие шаги можно посчитать рейтинги ещё раз.\n6. Для завершения работы программы нажми выход.\n\n"+
		"\t!!!Есть ограничения по работе программы!!!\n1.Для корретной работы таблицы с итогами игры должны быть в следующем формате:\n"+
		"Столбец \"А\" (1 столбец) должен содержать названия команд, столбец \"I\" (9 столбец) - итоговые баллы!\n"+
		"2.Программа различает регистры, не исправляет ошибки и опечатки. Если название команды написано иначе, чем уже имеющееся в таблице - оно будет вписано в конец,"+
		" как новая команда.")

	def action(self):
		self.msg_plain.clear()
		text = ''
		errors_msgs = ['Не выбран файл с общим рейтингом!','Не выбран файл с рейтингом сезона!','Не выбран файл итогов игры!']
		if self.overall_line.text() == '':
			text = errors_msgs[0]

		if self.season_line.text() == '':
			text = text + errors_msgs[1]
			season_team = dict()
		else:
			season_team = top.season(self.season_line.text())

		if self.games_line.text() == '':
			text = text + errors_msgs[2]

		if self.games_line.text() != '' and self.overall_line.text() != '':
			team = top.overall(self.overall_line.text())
			played = top.gameres(*self.games_line.text().split(', '))
			gametype = self.gametype_box.currentIndex()
			#promoted = rank.rank(team, played.keys(), gametype)
			promoted = score(team, season_team, played, gametype)
			save_name = QtWidgets.QFileDialog.getSaveFileName(self,"Сохранить файл с общим рейтингом")
			top.newbook(team, save_name[0])

			if self.season_on.isChecked() is True:
				save_name = QtWidgets.QFileDialog.getSaveFileName(self,"Сохранить файл с рейтингом сезона")
				top.newbook(season_team, save_name[0])
			
			if promoted != {}:
				text = 'ГОТОВО\n\n'+'Поздравляем с повышением!\n'
				for i in promoted.keys():
					text = text + '\n' + i + ':\n' + '\n'.join(promoted[i]) + '\n'
			else: text = 'ГОТОВО'

		
		self.msg_plain.setPlainText(text)

	def clear_overall_line(self):
		self.overall_line.clear()

	def browse_overall(self):
		self.overall_line.clear()
		file_overall = QtWidgets.QFileDialog.getOpenFileName(self,"Выберите файл")
		self.overall_line.setText(file_overall[0])
	
	def clear_season_line(self):
		self.season_line.clear()

	def browse_season(self):
		self.season_line.clear()
		file_season = QtWidgets.QFileDialog.getOpenFileName(self,"Выберите файл")
		self.season_line.setText(file_season[0])
	
	def clear_games_line(self):
		self.games_line.clear()

	def browse_games(self):
		self.games_line.clear()
		files_games = QtWidgets.QFileDialog.getOpenFileNames(self,"Выберите файл(ы)")
		text = ', '.join(files_games[0])
		self.games_line.setText(text)	

def score(team,season_team,played,gametype):
	promoted = {'nedosyag':[],'chuck':[],'rambo':[],'gener':[],'liet':[],'serg':[],
	'kim8':[],'kim7':[],'kim6':[],'kim5':[],'kim4':[], 'kim3':[], 'kim2':[], 'kim1':[],
	'lvl10':[],'lvl9':[],'lvl8':[],'lvl7':[],'lvl6':[],'lvl5':[],'lvl4':[],'lvl3':[],'lvl2':[],'lvl1':[],
	'ilon-strim':[],'nedosyag-strim':[],'chuck-strim':[],'rambo-strim':[],'marsh-strim':[],'gener-strim':[],'liet-strim':[],'serg-strim':[]}
	for title in played.keys():
		if title in team:
			team[title] = [team[title][0] + played[title][0],
			team[title][1] + played[title][1], 
			team[title][2],
			team[title][3]]
			rank.rank(team,title,gametype,promoted)
		else: 
			team[title] = [played[title][0],
			played[title][1], 
			None,
			None]
			rank.rank(team,title,gametype,promoted)

		if title in season_team and title in team:
			season_team[title] = [season_team[title][0] + played[title][0],
			season_team[title][1] + played[title][1], 
			team[title][2]]
		else:
			season_team[title] = [played[title][0],
			played[title][1], 
			team[title][2]]

	promoted = {rank:teams for rank, teams in promoted.items() if teams != []}
	ranks = {'nedosyag':'Недосягаемые','chuck':'Чак Норрис','rambo':'Рэмбо','gener':'Генерал','liet':'Лейтенант','serg':'Сержант',
	'kim8':'Бриллиантовая пластинка','kim7':'Платиновая пластинка','kim6':'3 золотые пластинки','kim5':'2 золотые пластинки',
	'kim4':'1 золотая пластинка', 'kim3':'3 виниловые пластинки', 'kim2':'2 виниловые пластинки', 'kim1':'1 виниловая пластинка',
	'lvl10':'10 уровень','lvl9':'9 уровень','lvl8':'8 уровень','lvl7':'7 уровень','lvl6':'6 уровень','lvl5':'5 уровень',
	'lvl4':'4 уровень','lvl3':'3 уровень','lvl2':'2 уровень','lvl1':'1 уровень',
	'ilon-strim':'Илон в маске и перчатках','nedosyag-strim':'Невыходные','chuck-strim':'Чак QR-кодис','rambo-strim':'Рэмбо Балконный',
	'marsh-strim':'Маршал удаленного полка',
	'gener-strim':'Генерал кухонной армии',
	'liet-strim':'Лейтенант диванных войск',
	'serg-strim':'Сержант кресельного батальона', None : ''}
	promoted= {ranks[rank]: promoted[rank] for rank in promoted.keys()}
	return promoted

def main():
	app = QtWidgets.QApplication(sys.argv)
	window = windowApp()
	window.show()
	app.exec_()

def logic():
	team = top.season('./25 игра + ГП.xlsx')
	#print(team)
	played = []
	top.gameres( team, played,'./Среда.xlsx')
	#print(team)
	#print(type(team))
	gametype = 'classic'
	promoted = rank.rank(team, played, gametype)
	top.newbook(team)
	print(promoted,'\n')

if __name__ == '__main__':
	#logic()
	main()