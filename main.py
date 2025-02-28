from maze_util import *

def main():
    win = Window(800, 600)
    maze = Maze(Point(0, 0), 20, 15, 40, win)
    maze.generate_maze()
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
