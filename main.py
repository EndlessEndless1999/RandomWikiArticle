import tkinter

import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser

root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)


def new():
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    global title
    title = soup.find(class_="firstHeading").text
    myLabel.text = title
    print(myLabel.text)


def yes():
    url = "https://en.wikipedia.org/wiki/%s" % title
    webbrowser.open(url)


def no():
    print("Try again!")
    new()


button1 = Button(leftframe, text="Go to Article!", command=yes)
button1.pack(padx=3, pady=3)

button1 = Button(rightframe, text="Refresh!", command=no)
button1.pack(padx=3, pady=3)

myLabel = Label(text='HELLO WORLD', foreground='white')
myLabel.pack(padx=5, pady=6)

root.title("Test")

title = ''


new()


root.mainloop()
