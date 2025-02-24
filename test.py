import unittest

from maze_util import Window, Maze, Point

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        print("hello world")
        test_window = Window(200, 200)
        num_rows = 12
        num_cols =10
        m1 = Maze(Point(0,0), num_rows, num_cols, 10)
        print(len(m1.cells))
        self.assertEqual(
            len(m1.cells),
            num_rows
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols
        )
