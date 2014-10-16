import DiskGame

three_on_a_line = DiskGame.DiskGame()

three_on_a_line.add_win_pattern([[1, 1, 1]]) #Horizontal pattern
three_on_a_line.add_win_pattern([[1],[1],[1]]) #Vertical pattern

three_on_a_line.add_win_pattern([
	[1, 0, 0],
	[0, 1, 0],
	[0, 0, 1]
])

three_on_a_line.add_win_pattern([
	[0, 0, 1],
	[0, 1, 0],
	[1, 0, 0]
])

# Tryhard patterns

"""three_on_a_line.add_win_pattern([
	[1, 1, 1]
	[1, 0, 1])
three_on_a_line.add_win_pattern([
	[1, 0, 1],
	[0, 1, 0],
	[1, 0, 1]])
"""

three_on_a_line.start_game()