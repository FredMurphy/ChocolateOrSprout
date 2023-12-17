#from guizero import App, Text, PushButton
from player import Player
from gamemode import GameMode
from questions import Question

from tkinter import *
from tkinter import ttk
from buildhat import Hat
#from PIL import ImageTk

#import time

poll_time = 100
timer_reset = 100

question_count = 3
timer = timer_reset

hat = Hat()
hat_ready = False
while hat_ready == False:
    print("Waiting for BuildHat...")
    hat_ready = hat.get()['A']['connected']

def set_question(question_text):
    instructionLabel.config(text = question_text)

def show_timer():
    global timer
    timer_percent = timer * 100 / timer_reset
    progress['value'] = timer_percent
    
def show_score():
    global red_score, blue_score, red_player, blue_player
    red_score.config(text = red_player.score)
    blue_score.config(text = blue_player.score)
    
def waiting_to_start():
    global game_mode, timer, red_player_ready, blue_player_ready, red_answer, blue_answer
    game_mode = GameMode.WaitingToStart
    set_question("OK. Load up your prizes. Chocolate at the front, sprout at the back.\nWhen each player is ready, hold any card over the card reader on your side.")
    timer = timer_reset
    red_player_ready = False
    blue_player_ready = False
    red_answer = ""
    blue_answer = ""

def about_to_play():
    global game_mode, timer
    game_mode = GameMode.AboutToPlay
    set_question("Let's play! First question coming up...")
    timer = timer_reset
    red_answer = ""
    blue_answer = ""
    
def start_game():
    global game_mode, question_number, red_player, blue_player, timer
    game_mode = GameMode.Playing
    timer = timer_reset
    question_number = 0
    set_question(questions[question_number].text)
    red_player.zero()
    blue_player.zero()
    show_timer()
    #show_score()

def finish_game():
    global game_mode, timer
    game_mode = GameMode.Finished
    timer = timer_reset
    set_question('The game has finished! Here are your prizes...')
    if blue_player.score > red_player.score:
        #blue wins
        blue_player.drop_chocolate()
        red_player.drop_sprout()
    elif red_player.score > blue_player.score:
        # red wins
        red_player.drop_chocolate()
        blue_player.drop_sprout()
    else:
        # it's a tie
        blue_player.drop_chocolate()
        red_player.drop_chocolate()
        
def check_answers():
    global red_answer, blue_answer
    if red_answer == "":
        red_answer = red_player.get_color()
        
    if blue_answer == "":
        blue_answer = blue_player.get_color()
    # to do - change image
    red_answer_label.config(text = red_answer)
    blue_answer_label.config(text = blue_answer)

def next_question():
    global questions, question_number, timer, timer_reset, red_answer, blue_answer
    question_number = question_number + 1
    if question_number >= len(questions):
        finish_game()
        return

    timer = timer_reset
    set_question(questions[question_number].text)
    red_answer = ""
    blue_answer = ""

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
            
        if red_player_ready and blue_player_ready:
            about_to_play()
            
    elif game_mode == GameMode.AboutToPlay:
        #print('Time to play...')
        timer = timer - 1
        show_timer()
        if timer <= 0:
            start_game()
        
    elif game_mode == GameMode.Playing:
        #print('Playing...')
        check_answers()
        timer = timer - 1
        show_timer()
        
        if timer <= 0:
            if questions[question_number].is_correct(red_answer):
                red_player.add_point()
            if questions[question_number].is_correct(blue_answer):
                blue_player.add_point()
            show_score()
            next_question()
    
    elif game_mode == GameMode.Finished:
        print('Finished...', timer)
        timer = timer - 1
        if timer <= 0:
            waiting_to_start()
            
    frame.after(poll_time, tick)

global game_mode
game_mode = GameMode.WaitingToStart

question_number = 0
questions = Question.get_random(question_count)

red_player = Player('D', 'A', -1)
blue_player = Player('C', 'B', 1)

red_answer = ""
blue_answer = ""

root = Tk()
root.title("Chocolate or Sprouts")
root.geometry("1920x1080")

backgroundImage =  PhotoImage(file="background1920x1080.png")
canvas = Canvas(root, width=1920, height=1080)
canvas.pack(fill="both", expand=True)
canvas.create_image(0,0,image=backgroundImage, anchor="nw")
canvas.create_text(600, 20, anchor="nw", text="Welcome to Chocolate or Sprouts!", fill="white", font="Tahoma 40")
canvas.create_text(600, 120, anchor="nw", text="This is a game where you battle against your opponent to answer some Christmas questions.\nThe winner gets rewarded with a chocolate. The loser gets a Brussels Sprout!", fill="white", font="Tahoma 20")

style = ttk.Style()
style.configure("TFrame", background="#21138a")
style.configure("Question.TLabel", font="Tahoma 20", background="#21138a", foreground="#ffffff")

frame = ttk.Frame(root, borderwidth=2, padding=10)
instructionLabel = ttk.Label(frame, text="Loading...", style="Question.TLabel")
instructionLabel.grid(column=0, row=0, columnspan=2)

ttk.Label(frame, text="Red").grid(column=0, row=1)
ttk.Label(frame, text="Blue").grid(column=1, row=1)

#image_thinking = ImageTk.PhotoImage(Image.open("thinking_1.png"))
#image_answered = ImageTk.PhotoImage(Image.open("answered_1.png"))

red_answer_label = ttk.Label(frame, text = "")
red_answer_label.grid(column=0, row=2)
blue_answer_label = ttk.Label(frame, text = "")
blue_answer_label.grid(column=1, row=2)

red_score = ttk.Label(frame, text="-")
red_score.grid(column=0, row=3)
blue_score = ttk.Label(frame, text="-")
blue_score.grid(column=1, row=3)

#timer_label = ttk.Label(frame, text = "-")
#timer_label.grid(column=0, row=4, columnspan=2)

frame.place(x=1900, y=400, width=1200, height=300, anchor="ne")

progress = ttk.Progressbar(length=1200)
progress.place(x=1900, y=700, width=1200, height=100, anchor="ne")
progress['value'] = 100


waiting_to_start()
frame.after(poll_time, tick)
root.mainloop()


