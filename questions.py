import random

class Question:

    def __init__(self, text, answer_color):
        self.text = text
        self.answer_color = answer_color

    def get_random(count):
        if count > len(questions):
            count = len(questions)
        random.shuffle(questions)
        return questions[:count]
        
questions = [
    Question('01. The answer is red', 'red'),
    Question('02. The answer is green', 'green'),
    Question('03. The answer is blue', 'blue'),
    Question('04. The answer is yellow', 'yellow'),
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
