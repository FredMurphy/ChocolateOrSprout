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
    Question('In the film Home Alone, where were the family going for Christmas?', 'green'),
    Question('What language is the Christams song Feliz Navidad?', 'red'),
    Question('What country has panetone as their Christmas cake?', 'blue'),
    Question('What country has STOLLEN as their Christmas cake?', 'yellow'),
    Question('05. The answer is red', 'red'),
    Question('06. The answer is green', 'green'),
    Question('07. The answer is blue', 'blue'),
    Question('08. The answer is yellow', 'yellow'),
    Question('09. The answer is red', 'red'),
    Question('00. The answer is green', 'green'),
    Question('11. The answer is blue', 'blue'),
    Question('12. The answer is yellow', 'yellow'),
    Question('13. The answer is red', 'red'),
    Question('14. The answer is green', 'green'),
    Question('15. The answer is blue', 'blue'),
    Question('16. The answer is yellow', 'yellow')
    ]
