import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

import numpy as np


class KittelPlotter:
    
    def __init__(self,parent):
        tl = tk.Toplevel(parent)

        self.dane=[]        

        tl.wm_title("Window Kittel")
        # l = tk.Label(tl, text="This is window #%s" % self.counter)
        l = tk.Label(tl, text="This is window ")
        # l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        l.pack()

        container=tk.Frame(tl)
        container.pack(side="left")

        containerRight=tk.Frame(tl)
        containerRight.pack(side="left")

        PlotButton= tk.Button(container, text="Plot",
                            command=self.plotKittel)
        PlotButton.pack(side="top")

        l = tk.Label(container, text="MagnEntry")
        l.pack(side="top", fill="both", expand=True)

        self.MagnEntry=tk.Entry(container)   
        self.MagnEntry.insert(0,"1000")    
        self.MagnEntry.pack()
        
        l = tk.Label(container, text="gEntry")
        l.pack(side="top", fill="both", expand=True)


        self.gEntry=tk.Entry(container)
        self.gEntry.insert(0,"2")       
        self.gEntry.pack()

        self.fig = Figure(figsize=(5, 4), dpi=100)

        self.canvas = FigureCanvasTkAgg(self.fig, master=containerRight)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(self.canvas, containerRight)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    def plotKittel(self):
        
        H = np.arange(0.0, 14000, 50)
        f = float(self.gEntry.get()) * np.sqrt((H + 4 * np.pi * float(self.MagnEntry.get())) + H )
        self.dane.append(H)
        self.dane.append(f)
        print(self.MagnEntry.get())
        self.fig.add_subplot(111).plot(H,f)
        self.canvas.draw()
        