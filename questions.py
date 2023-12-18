import random

class Question:

    def __init__(self, text, answer_color):
        self.text = text
        self.answer_color = answer_color
    
    def is_correct(self, color):
        return color == self.answer_color
    
    def get_random(count):
        if count > len(questions):
            count = len(questions)
        random.shuffle(questions)
        return questions[:count]
        
questions = [
    # Flags
    Question("In the film Home Alone, where were the family going for Christmas?", "green"), # France
    Question("What language is the Christmas song Feliz Navidad?", "red"), # Spain
    Question("What country has panetone as their Christmas cake?", "blue"), # Italy
    Question("What country has stollen as their Christmas cake?", "yellow"), # Germany
    # People
    Question("Who has their birthday the furthest away from Christmas?", "red"), # Rich
    Question("Who has cooked the most (and probably the best) Christmas dinners?", "green"), # Pip
    Question("Who was supposed to be born on Christmas Eve (but wasn't)?", "blue"), # Daniel
    Question("Who once spent Christmas in hospital?", "yellow"), # Adam
    # Colours
    Question("What colour is Rudolph's nose?", "red"),
    Question("What colour was Sant's coat before Coca-Cola changed it to red?", "green"),
    Question("What colour Christmas did Elvis have in his song '____ Christmas'?", "blue"),
    Question("What colour are mistletoe berries?", "yellow"), # white card with yellow back
    # Numbers
    Question("How many reindeer pull Santa's sleigh, including Rudolf?", "red"), # 9
    Question("How many maids a milking are there in The Twelve Days of Christmas?", "green"), # 8
    Question("How many million turkeys are eaten in the UK on Christmas day?", "blue"), # 10
    Question("How many ghosts are there in A Christmas Carol?", "yellow"), # 4
    # Objects
    Question("What was originally in the mincemeat that's used for mince pies?", "red"), # cow (beef)
    Question("What do Swedish children leave out for Santa when he comes down the chimney?", "green"), # coffee
    Question("One snowman said to the other 'Can you smell _____?'", "blue"), # carrots
    Question("What strange ingredient is traditionally put into a Christmas pudding?", "yellow") # sixpence
]
