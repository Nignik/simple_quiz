import user_interface
import pandas
import platform
import os
import random
import time
from colorama import init, Fore, Back, Style
from quiz import Quiz

def clear_console():
    match platform.system():
        case "Windows":
            os.system("cls")
        case "Linux":
            os.system("clear")

class Brain:
    def __init__(self):
        self.quiz = None
        self.best_score = None

    def begin(self):
        print("What quiz would you like to play?")
        user_interface.menu()

        quiz_name = input()

        self.quiz = Quiz(quiz_name)
        try:
            self.best_score = pandas.read_csv("data/best_scores.csv").to_dict()[quiz_name]
        except KeyError:
            print(f"best_scores.csv doesn't contain a best score for that quiz")

        clear_console()

        print("choose game mode")
        user_interface.show_mode_menu()
        game_mode = input()

        match game_mode:
            case "1":
                self.begin_non_repeat_mode()
            case "2":
                self.begin_double_mode()

    def begin_double_mode(self):
        while self.ask_double_question():
            continue

    def begin_non_repeat_mode(self):
        while self.ask_non_repeat_question():
            continue

    def ask_non_repeat_question(self):
        self.quiz.set_question_next()
        print(Fore.CYAN + self.quiz.question + Fore.WHITE)
        answer = input()

        match answer:
            case "quit":
                return False

        clear_console()

        if self.quiz.check_answer(answer):
            print(Fore.WHITE + "Correct: " + Fore.GREEN + self.quiz.answer)
        else:
            print(Fore.WHITE + "Correct: " + Fore.GREEN + self.quiz.answer)
            print(Fore.WHITE + "Incorrect: " + Fore.RED + answer)
        print(Fore.WHITE)

        return True

    def ask_double_question(self):
        self.quiz.set_question_next()
        question1 = self.quiz.question
        answer1 = self.quiz.answer
        self.quiz.set_question_next()
        question2 = self.quiz.question
        answer2 = self.quiz.answer

        cnt_question1 = 0
        cnt_question2 = 0

        while cnt_question1 <= 3 or cnt_question2 <= 3:
            question = random.randint(1, 2)

            if question == 1 and cnt_question1 <= 3:
                cnt_question1 += 1

                print(Fore.CYAN + question1 + Fore.WHITE)
                answer = input()
                if answer == "quit":
                    return False

                clear_console()

                if answer == answer1:
                    print(Fore.WHITE + "correct: " + Fore.GREEN + answer1)
                    print(Fore.WHITE + "answer:  " + Fore.GREEN + answer)
                else:
                    print(Fore.WHITE + "correct: " + Fore.GREEN + answer1)
                    print(Fore.WHITE + "answer:  " + Fore.RED + answer)

            elif question == 2 and cnt_question2 <= 3:
                cnt_question2 += 1

                print(Fore.CYAN + question2 + Fore.WHITE)
                answer = input()
                if answer == "quit":
                    return False

                clear_console()

                if answer == answer2:
                    print(Fore.WHITE + "correct: " + Fore.GREEN + answer2)
                    print(Fore.WHITE + "answer:  " + Fore.GREEN + answer)
                else:
                    print(Fore.WHITE + "correct: " + Fore.GREEN + answer2)
                    print(Fore.WHITE + "answer:  " + Fore.RED + answer)

        return True


