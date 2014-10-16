from Board import *

""" Over-engineered three on a line game """

class DiskGame:
	"""Game where people have to create a pattern by adding disks at the top of collumns aka three on a line overbuild beta edition"""

	gamemodes = {
		
	}

	def __init__ (self, board_size=(7,7), playercount=2):
		"""Initiate with a board_size (height, width)"""
		self.board = Board(board_size)
		self.history = []
		self.names = []
		self.playercount = playercount
		self.movenumber = 0
		self.last_collumn = 0

	def ask_names (self):
		""" Ask each player hes name and put it in the player list """

		while len(self.names) < self.playercount:
			self.names.append(input("Wat is de naam van speler " + str(len(self.names) + 1) + "? \n"))
			if self.names[-1] == "2secret4me":
				self.open_secret_menu()

	def print_board (self):
		""" Print the board to a terminal """
		print(self.board)

	def print_history (self):
		print("Het spel verliep als volgt:")
		for data in self.history:
			print("Speler " + self.names[data[0]] + " heeft de schijf laten vallen in kolom " + str(data[1]))

	def open_secret_menu (self):
		self.names = []

		for i in range(0, 15):
			print("")
		print("=====================================")
		print("= Welcome in the super secret menu! =")
		print("=====================================")
		print("")
		print("Possible commands:")
		print("  - playercount [int: newplayercount]")
		print("     Change the playercount to [newplayercount]")
		print("")
		print("  - size [int: width] [int: height]")
		print("     Change the board size to ([width], [height])")
		print("")
		print("  - gamemode [str: gamemode]")
		print("     Change the gamemode to one of the following: ")
		print("")
		print("       tryhard: a gamemode thats way too difficult")
		print("       threeonaline: a gamemode where the first player does always win")
		print("       fouronaline: a gamemode in which the first player does NOT always win")
		print("       disksonaline [int: disks]: generalized on a line game")
		print("")
		print("  - pattern [list: pattern]")
		print("     Manually add a win condition, examples:")
		print("       [[1], [1], [1], [1]]: four disks vertically")
		print("       [[1, 1, 1, 1]]: four disks horizontally")
		print("       [[0, 0, 1], [0, 1, 0], [1, 0, 0]]: three disks diagonally")
		print("")
		print("  - quit")
		print("     Exit this menu")
		print("")
		print("")

		while True:
			command = input("Please provide me with your command: ").split()
			if command[0] == "quit":
				for i in range(0, 15):
					print("")
				break

			if command[0] == "playercount":
				try:
					self.playercount = int(command[1])
					print("New playercount: " + command[1] + "\n")
				except:
					print("Invalid input! \n")

			if command[0] == "size":
				try:
					self.board.changesize((int(command[1]), int(command[2])))
					print("New boardsize: (" + command[1] + ", " + command[2] + ")\n")
				except:
					print("Invalid input! \n")
			
			if command[0] == "gamemode":
				self.gamemodes
				
			if command[0] == "addpattern":
				pass

	def ask_target_collumn (self):
		"""Ask the player in which collumn he wants to drop hes disk starting at 1"""
		while True:
			try:
				collumn = int(input(self.names[self.movenumber % len(self.names)] + ", in welke kolom wens je je stuk te laten vallen (1 - " + str(self.board.board_size[0]) + ") \n"))
				if collumn > 0 and collumn <= self.board.board_size[0]:
					return collumn
			except:
				pass
			print("Voer een geldig nummer in tussen 1 en " + str(self.board.board_size[0]))

	def add_win_pattern (self, pattern):
		self.board.add_win_pattern(pattern)

	def do_next_move (self):
		""" Ask the player which collumn and put a disk there """
		while True:
			disk = (self.movenumber % len(self.names)) + 1
			collumn = self.ask_target_collumn() - 1

			if self.board.drop_disk(disk, collumn):
				break

		self.history.append((disk - 1, collumn + 1))
		self.last_collumn = collumn
		self.movenumber += 1
		
	def start_game (self):
		self.ask_names()
		
		while (not self.board.check_win(self.last_collumn)) and (not self.board.board_full()):
			self.print_board()
			self.do_next_move()

		self.print_board()
		print("Proficiat " + self.names[(self.movenumber - 1) % len(self.names)] + ", u wint! \n")
		self.print_history()