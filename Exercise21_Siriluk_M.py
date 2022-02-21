from tkinter import *
import math
def leftClickButton(event):
    bmi = (float(Weight.get())/math.pow(float(Height.get())/100,2))
    if bmi >= 30:
        labelResult["text"] = "อ้วนมาก"
    elif bmi >= 25:
        labelResult["text"] = "อ้วน"
    elif bmi >= 23:
        labelResult["text"] = "น้ำหนักเกิน"
    elif bmi >= 18.6:
        labelResult["text"] = "น้ำหนักปกติ เหมาะสม"
    elif bmi <= 18.5:
        labelResult["text"] = "ผอมเกินไป"


MainWindow = Tk()
labelHeight = Label(MainWindow,text= "Height(cm.)")
labelHeight.grid(row=0,column=0)
Height = Entry(MainWindow)
Height.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="Weight(Kg.)")
labelWeight.grid(row=1,column=0)
Weight = Entry(MainWindow)
Weight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text ="calculate",width = 20,fg="Blue", bg="yellow")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="result",width = 30)
labelResult.grid(row=2,column=1,)
MainWindow.mainloop()
calculateButton = Button(MainWindow,text ="calculate")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="result")
labelResult.grid(row=2,column=1)
MainWindow.mainloop()