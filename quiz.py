import pandas
import random

class Quiz:
    def __init__(self, quiz_name):
        self.quiz_name = quiz_name
        self.current_score = 0
        self.data = None
        self.question = None
        self.answer = None
        self.question_nr = 0
        self.init_data()

    def init_data(self):
        try:
            self.data = pandas.read_csv("tests/" + self.quiz_name)
        except FileNotFoundError:
            print(f"{self.quiz_name}.csv not found, try different quiz name")

    def set_question_random(self):
        self.question_nr = random.randint(0, len(self.data["question"].to_list()))
        self.set_question()

    def set_question_next(self):
        self.question_nr = (self.question_nr + 1) % len(self.data["question"].to_list())
        self.set_question()

    def set_question(self):
        self.question = self.data["question"][self.question_nr]
        self.answer = self.data["answer"][self.question_nr].strip()


    def check_answer(self, answer):
        if answer == self.answer:
            return True
        else:
            return False






