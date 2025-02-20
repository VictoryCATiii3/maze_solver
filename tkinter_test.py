from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.geometry(f"{width}x{height}")
        self.__root.title("Window")
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.mainloop()

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
        self.__root.destroy()

def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__=="__main__":
    main()
