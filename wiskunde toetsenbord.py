from time import sleep
import ctypes
import json
import keyboard
import os
import tkinter as tk

user32 = ctypes.windll.user32
defaultData = {'sleeptime' : 0.03, 'char' : [ "≠", "∈", "⊂", "∪", "∩", "∨", "∧", "∅", "ℕ", "ℤ", "ℚ", "ℝ", "ℂ"] }

#lees de tijd dat het programma moet wachten tussen key presses uit het json bestand, als het programma niet naar behoren werkt raad ik aan dit getal te verhogen
#kijk of het bestand bestaat
if (os.path.exists("variables.json")):
    #open het bestand
    with open("variables.json", 'r+') as file:
        #probeer of sleeptime een getal is, zo niet maak de file opnieuw met standard variabelen
        try:
            data = json.load(file)
            float(data['sleeptime'])
        except:
            data = defaultData
            file.truncate(0)
            file.seek(0)
            json.dump(data, file)
        #maak de variabelen aan vanaf het bestand
        sleeptime = data['sleeptime']
        char = data['char']
#bestand bestaat niet, maak een aan met standard variabelen
else:
    data = defaultData
    sleeptime = data['sleeptime']
    char = data['char']
    with open("variables.json", 'w') as file:
        json.dump(data, file)

#alt+tab naar de vorige actieve window
def alttab():
    user32.keybd_event(0x12, 0, 0, 0) #Alt press
    sleep(sleeptime)
    user32.keybd_event(0x09, 0, 0, 0) #Tab press
    sleep(sleeptime)
    user32.keybd_event(0x12, 0, 2, 0) #Alt release
    sleep(sleeptime)
    user32.keybd_event(0x09, 0, 2, 0) #Tab release
    sleep(sleeptime)
    
def write(char):
    #ga terug naar vorige active window
    alttab()
    
    #write char naar textbox
    keyboard.write(char)

    #ga terug naar het toetsenbord
    alttab()
    

#maak de window
root = tk.Tk()
root.title("Wiskundig toetsenbord")
frame = tk.Frame(root)
frame.pack()

#voor ieder karakter in de lijst, maak een knop in de window
for x in char:
    button = tk.Button(frame,text=x,font=("Courier", 20), takefocus = 0, command= lambda x=x: write(x))
    button.pack(side=tk.LEFT)

#start het programma met de gemaakte window
root.mainloop()
