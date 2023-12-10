#from guizero import App, Text, PushButton
from tkinter import *
from tkinter import ttk
#from buildhat import Hat, Motor, ColorDistanceSensor
#import time

#hat = Hat()
#print(hat.get())

#app = App(title="Chocolate or Sprouts", width=1920, height=1080, bg='#ff0000')
#welcome_message = Text(app, text="Welcome to Chocolate or Sprouts", size=40, font="Tahoma", color="white")
#app.display()
#app.set_full_screen()
root = Tk()
root.title("Chocolate or Sprouts")
root.geometry("1920x1080")

backgroundImage =  PhotoImage(file="background1920x1080.png")
canvas = Canvas(root, width=1920, height=1080)
canvas.pack(fill="both", expand=True)
canvas.create_image(0,0,image=backgroundImage, anchor="nw")
canvas.create_text(600, 20, anchor="nw", text="Welcome to Chocolate or Sprouts!", fill="white", font="Tahoma 40")
canvas.create_text(600, 120, anchor="nw", text="This is a game where you battle against your oponent to answer some Christmas questions.\nThe winner gets rewarded with a chocolate. The loser gets a Brussels Sprout!", fill="white", font="Tahoma 20")

style = ttk.Style()
style.configure("TFrame", background="#21138a")
style.configure("Question.TLabel", font="Tahoma 20", background="#21138a", foreground="#ffffff")

frame = ttk.Frame(root, borderwidth=2, padding=10)
instructionLabel = ttk.Label(frame, text="Hold any card over the left hand scanner to get started", style="Question.TLabel").grid(column=0, row=0, columnspan=2)
label1 = ttk.Label(frame, text="1").grid(column=0, row=1)
label3 = ttk.Label(frame, text="3").grid(column=1, row=1)


frame.place(x=1900, y=400, width=1200, height=300, anchor="ne")

root.mainloop()
