import pygame, time, random
WINDOW_SIZE = (1000, 1000)
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)


maze_size = int(input("Size of maze (nxn):"))
maze = []
for i in range(0,maze_size):
	maze.append([])
	for j in range(0,maze_size):
		if random.randint(0,3) >= 1:
			maze[i].append(0)
		else:
			maze[i].append(1)
maze[0][0] = 0
maze[0][maze_size-1] = 0
maze[maze_size-1][0] = 0
maze[maze_size-1][maze_size-1] = 0

delay = 3/maze_size
if (maze_size > 100):
	delay = 0
"""
maze = [[1,0,0,1,0,1,0,1,0,1],
	[1,1,0,1,0,1,0,0,1,0],
	[1,0,0,1,0,0,0,1,0,0],
	[0,0,1,0,0,0,1,0,1,1],
	[1,0,0,0,0,0,1,1,1,1],
	[0,0,1,0,1,1,1,1,1,1],
	[0,1,0,0,1,1,1,1,0,0],
	[0,0,0,1,1,0,0,0,1,0],
	[0,1,0,1,0,0,1,0,0,0],
	[0,1,0,0,0,1,1,1,1,0]]
"""
SQUARE_SIZE = (WINDOW_SIZE[0]-len(maze)-1)/len(maze) 

pygame.init()
screen=pygame.display.set_mode(WINDOW_SIZE)

def solve(row,col):
	if (maze[row][col] == 1):
		return False
	if (maze[row][col] == 2) or (maze[row][col] == 3):
		return False
	maze[row][col] = 2
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			return True
	# color the board
	screen.fill(white)
	for row_1 in range(0, len(maze)):
		for col_1 in range(0,len(maze[0])):
			if maze[row_1][col_1] == 0:
				pygame.draw.rect(screen, black, [(1 + SQUARE_SIZE) * col_1 + 1, (1 + SQUARE_SIZE) * row_1 + 1, SQUARE_SIZE, SQUARE_SIZE])
			if maze[row_1][col_1] == 2:
				pygame.draw.rect(screen, green, [(1 + SQUARE_SIZE) * col_1 + 1, (1 + SQUARE_SIZE) * row_1 + 1, SQUARE_SIZE, SQUARE_SIZE])
			if maze[row_1][col_1] == 3:
				pygame.draw.rect(screen, red, [(1 + SQUARE_SIZE) * col_1 + 1, (1 + SQUARE_SIZE) * row_1 + 1, SQUARE_SIZE, SQUARE_SIZE])
	
	pygame.display.flip()
	time.sleep(delay)
	done = False
	if (row == len(maze)-1) and (col == len(maze)-1):
		print("solved")
		done = True;
	if (row != 0) and (not done):
		done = solve(row - 1, col)
	if (row != len(maze)-1) and (not done):
		done = solve(row + 1, col)
	if (col != 0) and (not done):
		done = solve(row, col - 1)
	if (col != len(maze)-1) and (not done):
		done = solve(row, col + 1)
	if (not done):
		maze[row][col] = 3
	return done

solve(len(maze)-1,0)
pygame.quit()
