import Tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, master, w, h):
        tk.Frame.__init__(self, master, width=w, height=h)
        self.toolpanel = ToolPanel(self, 200, h)
        self.toolpanel.pack(side=tk.LEFT, fill=tk.Y)

class ToolPanel(tk.Frame):
    def __init__(self, master, w, h):
        tk.Frame.__init__(self, master, width=w, height=h, background='#000')

def main():
    root = tk.Tk()
    root.geometry('640x480')

    mainframe = MainFrame(root, 640, 480)
    #mainframe.pack()
    #mainframe.pack(fill="both", expand=True)
    mainframe.pack(side="left", fill="y")

    root.mainloop()
