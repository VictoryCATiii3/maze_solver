import unittest

from maze_util import Window, Maze, Point

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 12
        num_cols =10
        m1 = Maze(Point(0,0), num_rows, num_cols, 10)
        self.assertEqual(
            len(m1.cells),
            num_rows
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols
        )

    def test_break_entrence_and_exit(self):
        num_rows = 4
        num_cols = 6
        m2 = Maze(Point(1, 1), num_rows, num_cols, 5)
        m2._break_entrance_and_exit()
        self.assertEqual(m2.cells[0][0].has_top_wall, False)
        self.assertEqual(m2.cells[0][0].has_left_wall, True)
        self.assertEqual(m2.cells[3][5].has_bottom_wall, False)
        self.assertEqual(m2.cells[3][5].has_right_wall, True)

    def test_reset_cells_visited(self):
        num_rows = 5
        num_cols = 5
        m3 = Maze(Point(0,0), num_rows, num_cols, 5)
        m3.generate_maze()
        self.assertEqual(m3.cells[0][0].visited, True)
        self.assertEqual(m3.cells[-1][-1].visited, False) # We finish here so it isn't marked as visited.
        self.assertEqual(m3.cells[2][2].visited, True)
        m3._reset_cells_visited() # All cells should once again be marked unvisited
        self.assertEqual(m3.cells[0][0].visited, False)
        self.assertEqual(m3.cells[-1][-1].visited, False) # End should remain false
        self.assertEqual(m3.cells[2][2].visited, False)

