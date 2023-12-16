#from guizero import App, Text, PushButton
from player import Player
from gamemode import GameMode
from questions import Question

from tkinter import *
from tkinter import ttk
from buildhat import Hat
#import time

poll_time = 1000
timer_reset = 10

question_count = 10
timer = timer_reset

hat = Hat()
hat_ready = False
while hat_ready == False:
    print("Waiting for BuildHat...")
    hat_ready = hat.get()['A']['connected']

def set_question(question_text):
    instructionLabel.config(text = question_text)

def show_timer():
    global timer, timer_label
    timer_label.config(text = str(timer) + "...")
    
def show_score():
    global red_score, blue_score, red_player, blue_player
    red_score.config(text = red_player.score)
    blue_score.config(text = blue_player.score)
    
def start_game():
    global game_mode, question_number, red_player, blue_player, timer
    game_mode = GameMode.Playing
    question_number = -1
    timer = timer_reset
    instructionLabel.config(text = "Let's play!")
    red_player.zero()
    blue_player.zero()
    show_score()

def tick():
    global game_mode, red_player, red_player_ready, blue_player, blue_player_ready, questions, question_number, timer, timer_reset
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
            start_game()

    elif game_mode == GameMode.Playing:
        #print('Playing...')
        # check answers
        timer = timer - 1
        show_timer()
        
        if timer <= 0:
            show_score()
            question_number = question_number + 1
            timer = timer_reset
            set_question(questions[question_number].text)
            # todo: work out who to give point to
            red_player.add_point()
            show_score()
            if question_number >= len(questions):
                # todo: finish game
               start_game() 
        
    frame.after(poll_time, tick)
            
global game_mode
game_mode = GameMode.WaitingToStart

question_number = 0
questions = Question.get_random(question_count)
#print("First question:", questions[0].text)
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

ttk.Label(frame, text="Red").grid(column=0, row=1)
ttk.Label(frame, text="Blue").grid(column=1, row=1)

red_answer = ttk.Label(frame, text="?")
red_answer.grid(column=0, row=2)
blue_answer = ttk.Label(frame, text="?")
blue_answer.grid(column=1, row=2)

red_score = ttk.Label(frame, text="-")
red_score.grid(column=0, row=3)
blue_score = ttk.Label(frame, text="-")
blue_score.grid(column=1, row=3)

timer_label = ttk.Label(frame, text = "-")
timer_label.grid(column=0, row=4, columnspan=2)

frame.place(x=1900, y=400, width=1200, height=300, anchor="ne")
frame.grid_propagate(0)
frame.after(poll_time, tick)
root.mainloop()


