import user_interface
import random
from colorama import init, Fore, Back, Style
from quiz import Quiz

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        user_interface.print_correct(user_answer)
    else:
        user_interface.print_incorrect(user_answer, correct_answer)

class Brain:
    def __init__(self):
        self.quiz = None
        self.best_score = None

    def begin(self):
        quiz_name = user_interface.choose_quiz()

        success = False
        while not success:
            try:
                self.quiz = Quiz(quiz_name)
                success = True
            except FileNotFoundError:
                print(Fore.RED + quiz_name + ".csv not found, try different quiz name" + Fore.WHITE)
                quiz_name = user_interface.choose_quiz()

        game_mode = user_interface.choose_mode()

        match game_mode:
            case "1":
                self.begin_non_repeat_mode()
            case "2":
                self.begin_double_mode()

    def begin_non_repeat_mode(self):
        while self.ask_non_repeat_question():
            continue

    def begin_double_mode(self):
        while self.ask_double_question():
            continue


    def ask_non_repeat_question(self):
        self.quiz.set_question_next()
        question = self.quiz.question
        correct_answer = self.quiz.answer

        user_interface.ask_question(question)
        user_answer = user_interface.take_input()

        check_answer(user_answer, correct_answer)

        return True

    def ask_double_question(self):
        self.quiz.set_question_next()
        question1 = self.quiz.question
        correct_answer1 = self.quiz.answer
        self.quiz.set_question_next()
        question2 = self.quiz.question
        correct_answer2 = self.quiz.answer

        question_set = [(question1, correct_answer1) for i in range(3)]
        question_set.extend([(question2, correct_answer2) for i in range(3)])
        random.shuffle(question_set)

        for question, correct_answer in question_set:
            user_interface.ask_question(question)

            user_answer = user_interface.take_input()
            if not user_answer:
                return False

            check_answer(user_answer, correct_answer)


        return True


