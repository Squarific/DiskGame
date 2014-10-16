class Board:
	"""Board class used by the DiskGame class"""
	def __init__ (self, board_size=(7, 7)): #Board size (width, height)
		"""Create a list of collumns containing disks according to the provided board_size"""
		self.changesize(board_size)
		self.winpatterns = []

	def __str__ (self):
		string = ""
		for y in range(0, self.board_size[1]):
			string += "| "
			for x in range(0, self.board_size[0]):
				string += str(self.get_disk((x, y))) + " "
			string += "| \n"
		string += "=" * (self.board_size[0] * 2 + 3)
		return string

	def changesize (self, size):
		self.board_size = size
		self.disks = [[] for i in range(0, size[0])]

	def add_win_pattern (self, pattern):
		self.winpatterns.append(pattern)

	def reset_patterns (self):
		self.winpatterns = []

	def get_disk (self, point):
		""" Get the disk at point (x, y) where the left top corner is (0,0) and left down increases"""
		try:
			# Python doesn't throw errors on negative indexes
			# Python will not be constrained by your opressiveness

			y = self.board_size[1] - point[1] - 1
			if y < 0:
				return 0

			return self.disks[point[0]][y]
		except:
			return 0

	def drop_disk (self, disk, collumn):
		""" Drop the disk in the 0-indexed collumn of disks if it does not exceed the collumn size"""
		if len(self.disks[collumn]) >= self.board_size[1]:
			return False
		
		self.disks[collumn].append(disk)
		return self.disks

	def check_win (self, last_collumn):
		""" Check if there was a win when the last disk was inserted in last_collumn"""

		# We first need the coords of the last inserted disk
		coords = (last_collumn, self.board_size[1] - len(self.disks[last_collumn]))

		disk = self.get_disk(coords)
		if disk == 0:
			return False

		# For every pattern we need to see if the pattern exists shifted to so
		# that the last disk can be any of the disks in the pattern
		for pattern in self.winpatterns:
			for relativey in range(len(pattern)):
				for relativex in range(len(pattern[relativey])):
					if self.check_pattern(pattern, disk, coords[0] - relativex, coords[1] - relativey):
						return True
		return False

	def check_pattern (self, pattern, disk, x, y):
		""" Check if the given pattern exists for a given disk at location (x, y) coords start left top corner (0, 0) increasing left down"""
		for relativey in range(len(pattern)):
			for relativex in range(len(pattern[relativey])):
				if pattern[relativey][relativex] == 1 and self.get_disk((x + relativex, y + relativey)) != disk:
					return False
		return True

	def board_full (self):
		for collumn in self.disks:
			if len(collumn) < self.board_size[1]:
				return False
		return True