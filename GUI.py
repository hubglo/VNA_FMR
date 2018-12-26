

import tkinter as tk
from KittelPlotter import *

class VNA_FMR(tk.Frame):
   
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="Kittel plotter", 
                                command=self.create_window)
        self.button.pack(side="top", padx=100, pady=100)

        self.buttonDane = tk.Button(self, text="printDane", 
                                command=self.printDane)
        self.buttonDane.pack()

    def create_window(self):
        
        self.t = KittelPlotter(self)

    def printDane(self):
        print(self.t.dane)    
        
if __name__ == "__main__":
    root = tk.Tk()
    main = VNA_FMR(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()