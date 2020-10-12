import tkinter as tk
from googletrans import Translator

win = tk.Tk()
win.title("Rath Translator")
win.geometry("500x500")

# function

def translation():
    word = entry.get()
    translator = Translator(service_urls=['translate.google.com'])
    translation1 = translator.translate(word,dest="fr")
    label1 = tk.Label(win,text=translation1.text, bg="skyblue")
    label1.grid(row=2,column=0)

label = tk.Label(win,text="Enter")
label.grid(row=0,column=0,sticky="W")

entry = tk.Entry(win)
entry.grid(row=1,column=0)

button = tk.Button(win,text="Translate",command=translation, bg="purple")
button.grid(row=1,column=2)
   
win.mainloop()
    
