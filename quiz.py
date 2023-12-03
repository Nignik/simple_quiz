import pandas
import random
import time

class Quiz:
    def __init__(self, quiz_name):
        self.quiz_name = quiz_name
        self.current_score = 0
        self.data = None
        self.question = None
        self.answer = None
        self.init_data()

    def init_data(self):
        try:
            self.data = pandas.read_csv("tests/" + self.quiz_name + ".csv")
        except FileNotFoundError:
            print(f"{self.quiz_name}.csv not found, try different quiz name")

    def next_question(self):
        random.seed(time.time())
        question_nr = random.randint(0, len(self.data["question"].to_list()) - 1)
        self.question = self.data["question"][question_nr]
        self.answer = self.data["answer"][question_nr].strip()

    def check_answer(self, answer):
        if answer == self.answer:
            return True
        else:
            return False






