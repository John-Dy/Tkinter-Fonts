from tkinter import *
from tkinter import ttk
from tkinter import font

class Fonts:

    def __init__(self):
        #Create Window
        self.root = Tk()
        self.root.title("tkinter Fonts")
        self.root.geometry("1400x800")
        #Create Main Frame
        self.frame = Frame(self.root)
        self.frame.pack(fill="both", expand=True)
        #Create Canvas
        self.canvas = Canvas(self.frame)
        self.canvas.pack(side="left", fill="both", expand=True)
        
        #Add Vertical Scrollbar
        self.verticalScroll = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.verticalScroll.pack(side="right", fill="y")
        #Add Horizontal Scrollbar
        self.horizontalScroll = ttk.Scrollbar(self.root, orient="horizontal", command=self.canvas.xview)
        self.horizontalScroll.pack(side="bottom",fill="x")

        #Configuration
        self.canvas.config(yscrollcommand=self.verticalScroll.set, xscrollcommand=self.horizontalScroll.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.config(scrollregion=self.canvas.bbox("all")))        
        #Create Another Frame Inside The Canvas
        self.newFrame = Frame(self.canvas)
        #Add New Frame To Window Inside Canvas
        self.canvas.create_window((0,0), window=self.newFrame, anchor="nw")

        #Add Labels Containing Fonts
        self.xCord = 0
        self.yCord = 0
        for f in font.families():
            Label(self.newFrame, text=str(f), borderwidth=1, relief="solid", fg="red", font=("Arial", 9), anchor="nw", bg="White").grid(column=self.xCord, row=self.yCord, sticky="news") #Sticky parameter ensures all the boxes are the same size
            Label(self.newFrame, text=str(f), borderwidth=1, relief="solid", font=(str(f), 15), anchor="nw", bg="White", wraplength=200).grid(column=self.xCord, row=self.yCord+1, sticky="news")
            if self.xCord < 10:
                self.xCord += 1
            else:
                self.yCord += 2
                self.xCord = 0

        #Activate Program
        self.root.mainloop()

if __name__ == "__main__":
    Fonts()