from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.geometry(f"{width}x{height}")
        self.__root.title("Window")
        self.canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Window closed")

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw_line(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw_line(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )

class Cell:
    def __init__(self, top_left_point, size, window,
                 has_left_wall=True,
                 has_right_wall=True,
                 has_top_wall=True,
                 has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = top_left_point.x
        self._x2 = top_left_point.x + size
        self._y1 = top_left_point.y
        self._y2 = top_left_point.y + size
        self._win = window

    def draw(self):
        left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_left_wall:
            left_line.draw_line(self._win.canvas, "black")
        if self.has_right_wall:
            right_line.draw_line(self._win.canvas, "black")
        if self.has_top_wall:
            top_line.draw_line(self._win.canvas, "black")
        if self.has_bottom_wall:
            bottom_line.draw_line(self._win.canvas, "black")

    def get_center(self):
        x = (self._x1 + self._x2)/2
        y = (self._y1 + self._y2)/2
        return Point(x, y)

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        center1 = self.get_center()
        center2 = to_cell.get_center()
        move_line = Line(center1, center2)
        move_line.draw_line(self._win.canvas, color)

class Maze:
    def __init__(self, top_left_point, num_rows, num_collums, cell_size, win=None):
        self._win = win
        self.cells = self._create_cells(top_left_point, num_rows, num_collums, cell_size)
        self._top_left = top_left_point
        self._width = num_rows
        self._height = num_collums
        self._animate()

    def _create_cells(self, top_left_point, num_rows, num_collums, cell_size):
        x = top_left_point.x
        y = top_left_point.y
        cells = []
        for i in range(num_rows):
            current_collum = []
            for j in range(num_collums):
                current_collum.append(Cell(Point(x, y), cell_size, self._win))
                y += cell_size
            x += cell_size
            y = top_left_point.y
            cells.append(current_collum)
        return cells

    def _draw_cell(self, i, j):
        cell = self.cells[i][j]
        cell.draw()

    def _animate(self):
        if self._win == None:
            return
        for i in range(self._width):
            for j in range(self._height):
                self._draw_cell(i, j)
                self._win.redraw()
                time.sleep(0.05)

    def _break_entrance_and_exit(self, i, j, side):
        pass

def main():
    win = Window(800, 600)
    line = Line(Point(0,0), Point(500, 600))
    win.draw_line(line, "black")
    #Test drawing cells
    test_cell = Cell(Point(20, 20), 20, win)
    test_cell.draw()
    test_cell2 = Cell(Point(60, 20), 20, win, has_left_wall=False)
    test_cell2.draw()
    test_cell3 = Cell(Point(60, 60), 20, win, has_top_wall=False, has_right_wall=False)
    test_cell3.draw()
    #Test drawing path
    test_cell.draw_move(test_cell2)
    test_cell2.draw_move(test_cell3, undo=True)

    maze = Maze(Point(90, 10), 10, 8, 10, win)

    win.wait_for_close()

if __name__=="__main__":
    main()
