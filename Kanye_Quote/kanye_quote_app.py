from email.mime import image
from tkinter import *
from turtle import hideturtle
import requests
#-----------------API REQUEST FOR THE QUOTE----------------#
def kanye():
    response = requests.get(url="https://api.kanye.rest")
    quote = response.json()
    canvas.itemconfig(quote_text,text = quote["quote"])

#-----------------BUILDING THE UI----------------#
window = Tk()
window.config(padx=20,pady=20)

canvas = Canvas(height=500,width=400,highlightthickness=0)
bg_img = PhotoImage(file="background.png")
canvas.create_image(200,250,image = bg_img)
quote_text = canvas.create_text(200, 150, text="", font=("Arial",20,"bold"))
canvas.grid(column=0,row=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img,highlightthickness=0, command=kanye)
kanye_button.grid(column=0,row=1)

kanye()

window.mainloop()
