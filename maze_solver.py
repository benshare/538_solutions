from Queue import *

def ReverseSolve(maze_info, find_all_solutions=True):
	maze, start_positions, end = maze_info
	num_rows = len(maze)
	num_cols = len(maze[0])
	frontier = PriorityQueue()

	seen = []
	seen.append(end)
	frontier.put((end, [end], 0), 0)

	solutions = []
	while not frontier.empty():
		current_option = frontier.get()
		current_pos, current_path, current_cost = current_option

		next_squares = []
		x, y = current_pos
		if x > 0:
			next_squares.append(((x - 1, y), "D"))
		if x < num_rows - 1:
			next_squares.append(((x + 1, y), "U"))
		if y > 0:
			next_squares.append(((x, y - 1), "R"))
		if y < num_cols - 1:
			next_squares.append(((x, y + 1), "L"))

		for next_square in next_squares:
			next_position = next_square[0]
			if next_position in seen:
				continue
			seen.append(next_position)
			# print next_type(aze[14])
			next_cost, next_movement = maze[next_position[0]][next_position[1]]
			if next_cost == -1:
				continue
			if next_square[1] not in next_movement:
				continue

			# print next_position
			# print type(current_path)
			# print type(next_position)
			# print type(current_cost)
			# print type(next_cost)
			next_option = [next_position, current_path + [next_position], current_cost + next_cost]
			if next_position in start_positions:
				if not find_all_solutions:
					return next_option
				solutions.append(next_option)
			else:
				frontier.put(next_option, next_option[2])
	forward_solutions = [[solution[0], solution[1][::-1], solution[2]] for solution in solutions]
	return forward_solutions
	
if __name__ == "__main__":
	full_maze = []
	with open("maze") as f:
		# i = 1
		line = f.readline()
		while line:
			row_list = line.split()
			# print i, len(row_list)
			# i += 1
			new_row = []
			for label in row_list:
				if label in ['-1', '0', '1', '2', '3']:
					new_row.append((int(label), "UDLR"))
				else:
					new_row.append((0, label))
			full_maze.append(new_row)
			line = f.readline()

	full_start = []
	l = len(full_maze)
	for i in range(l - 1):
		full_start.extend([(0, i), (i, l - 1), (l - 1, l - 1 - i), (l - 1 - i, 0)])
	full_end = (l / 2, l / 2)
	full_info = [full_maze, full_start, full_end]
	# mini_maze = [[(0, "R"), (0, "UD")], [(1, "UDLR"), (0, "UDLR")]]
	# mini_info = (mini_maze, [(0, 0), (1, 0)], (1, 1))
	# print ReverseSolve(full_info)
	for solution in ReverseSolve(full_info):
		for line in solution[1]:
			print line
		break
		# print solution
