#from guizero import App, Text, PushButton
from player import Player
from gamemode import GameMode
from questions import Question

from tkinter import *
from tkinter import ttk
from datetime import datetime
from buildhat import Hat
#import time

question_count = 10

hat = Hat()
print(hat.get())

def set_question(question_text):
    instructionLabel.config(text = question_text)
    
def doPolling():
    global game_mode, red_player_ready, blue_player_ready, questions, question_number
    if game_mode == GameMode.WaitingToStart:
        #print('WaitingToStart...')
        if red_player_ready == False:
            red_player_ready = (red_player.get_color() != "")
            if red_player_ready:
                set_question("Red player ready! Waiting for Blue...")
                
        if blue_player_ready == False:
            blue_player_ready = (blue_player.get_color() != "")
            if blue_player_ready:
                set_question("Blue player ready! Waiting for Red...")
            
        if (red_player_ready and blue_player_ready):
            game_mode = GameMode.Playing
            question_number = 0
            instructionLabel.config(text = "Let's play!")

    elif game_mode == GameMode.Playing:
        #print('Playing...')
        set_question(questions[question_number].text)
        question_number = question_number + 1
        if question_number >= len(questions):
           question_number = 0 
        
    frame.after(1000, doPolling)
            
global game_mode
game_mode = GameMode.WaitingToStart

question_number = 0
questions = Question.get_random(question_count)
print("First question:", questions[0].text)
#print(game_mode)

red_player = Player('D', 'A', 1)
blue_player = Player('C', 'B', -1)
red_player_ready = False
blue_player_ready = False

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
instructionLabel = ttk.Label(frame, text="When each player is ready, hold any card over the card reader on your side.", style="Question.TLabel")
instructionLabel.grid(column=0, row=0, columnspan=2)
label1 = ttk.Label(frame, text="1").grid(column=0, row=1)
label3 = ttk.Label(frame, text="3").grid(column=1, row=1)


frame.place(x=1900, y=400, width=1200, height=300, anchor="ne")
frame.after(1000, doPolling)
root.mainloop()


