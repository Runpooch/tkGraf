import tkinter as tk 
from tkinter import filedialog
from tkinter import Label, Button
import matplotlib.pyplot as plt
from tkinter import messagebox

# messagebox.showwarning("Varování","Nečuč")
# messagebox.askquestion("OK", "čus")

# neco = filedialog.askopenfilename()
# if neco == None :
#         messagebox.showwarning("Varování","Nečuč")

class Application(tk.Tk):
    name = "Grafy"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)

        self.Btn1 = tk.Button(self, text = "Vybrat soubor", command = self.nacist)
        self.Btn1.pack()
        self.Btn2 = tk.Button(self, text="Vykreslit graf",command = self.vykreslit)
        self.Btn2.pack()
        self.Btn3 = tk.Button(self, text="Quit", command= self.quit)
        self.Btn3.pack()

    def nacist (self):
        self.filename = filedialog.askopenfilename()

    def vykreslit (self):
        f = open(self.filename,"r")
        self.osaX = []                         
        self.osaY = []
        while 1:
            radek=f.readline()      
            if radek=='':
                break
            cisla=radek.split()
            self.osaX.append( float(cisla[0]))
            self.osaY.append(float(cisla[1]))
    
        plt.plot(self.osaX, self.osaY)           
        plt.grid()
        plt.show()
    
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop() 
