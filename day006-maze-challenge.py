import random
import time
from os import WCONTINUED


def generate_maze(size, wall_density):
    # Generate an empty maze filled with white squares
    maze = []
    for row in range(size):
        row_list = []
        for col in range(size):
            row_list.append("⬜️")
        maze.append(row_list)
    # or
    # maze = [["⬜️" for col in range(size)] for row in range(size)]

    # Create a guaranteed path from start to end
    path = [(0, 0)]
    x, y = 0, 0
    while (x, y) != (size - 1, size - 1):
        if x == size - 1:
            y += 1
        elif y == size - 1:
            x += 1
        else:
            if random.choice([True, False]):
                x += 1
            else:
                y += 1
        path.append((x, y))

    # Add random walls (never overwrite the guaranteed path)
    for i in range(size):
        for j in range(size):
            if (i, j) not in path and random.random() < wall_density:
                maze[i][j] = "⬛️"

    return maze, path


def print_maze(maze, pos, start, end):
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if (i, j) == pos:
                print("🤖", end="")
            elif (i, j) == start:
                print("🟦", end="")
            elif (i, j) == end:
                print("🟥", end="")
            else:
                print(col, end="")
        print()
    time.sleep(0.1)


print("Welcome to Maze Challenge!")

while True:
    difficulty = input("\nChoose difficulty (easy / medium / hard): ").lower()

    if difficulty == "easy":
        size = 6
        density = 0.15
        break
    elif difficulty == "medium":
        size = 8
        density = 0.25
        break
    elif difficulty == "hard":
        size = 10
        density = 0.35
        break
    else:
        print("Invalid difficulty level! Please enter 'easy', 'medium', or 'hard'.")

print(f"Difficulty set to {difficulty}. Maze size: {size}, density: {density}")

maze, guaranteed_path = generate_maze(size, density)
start = (0, 0)
end = (size - 1, size - 1)

pos = start
current_path = [start]

while True:
    # Reset all non-path positions to white
    for i in range(size):
        for j in range(size):
            if maze[i][j] == "🟩":
                maze[i][j] = "️️️⬜️"

    # Mark the current path
    for x, y in current_path:
        if (x, y) != start and (x, y) != end:
            maze[x][y] = "🟩"

    print_maze(maze, pos, start, end)

    move = input("\nMove (w=up, s=down, a=left, d=right): ").lower()
    x, y = pos
    if move == "w":
        new_pos = (x - 1, y)
    elif move == "s":
        new_pos = (x + 1, y)
    elif move == "a":
        new_pos = (x, y - 1)
    elif move == "d":
        new_pos = (x, y + 1)
    else:
        print("\nInvalid move!")
        continue

    new_x, new_y = new_pos
    if 0 <= new_x < size and 0 <= new_y < size and maze[new_x][new_y] != "⬛️":
        pos = new_pos
        if pos in current_path:
            idx = current_path.index(pos)
            current_path = current_path[:idx + 1]
        else:
            current_path.append(pos)
    else:
        print("\nCan't move there!")

    if pos == end:
        # Mark the final path before exiting
        for x, y in current_path:
            if (x, y) != start and (x, y) != end:
                maze[x][y] = "🟩"
        print_maze(maze, pos, start, end)
        print("\nYou reached the exit!")
        break
