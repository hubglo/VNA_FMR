

import tkinter as tk
from KittelPlotter import *

class VNA_FMR(tk.Frame):
   
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.root=parent

        self.buttonContainer=tk.Frame(self)
        self.buttonContainer.pack(side='left')
    
        self.button = tk.Button(self.buttonContainer, text="Kittel plotter", 
                                command=self.create_window)
        self.button.pack(side="top", padx=100, pady=100)

        self.buttonDane = tk.Button(self.buttonContainer, text="printDane", 
                                command=self.printDane)
        self.buttonDane.pack()


        self.graphContainer=tk.Frame(self)
        self.graphContainer.pack(side='left')

        self.fig = Figure(figsize=(5, 4), dpi=100)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graphContainer)  # A tk.DrawingArea.
        self.graph1 = self.fig.add_subplot(111)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(self.canvas, self.graphContainer)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    def create_window(self):
        # self.hide()
        self.t = KittelPlotter(self)

    def printDane(self):
        print(self.t.dane)   

    def show(self):
        self.root.update()
        self.root.deiconify()

    def hide(self):
        self.root.withdraw()
  
        
if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("VNA-FMR")
    
    main = VNA_FMR(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()