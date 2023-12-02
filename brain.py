import user_interface
import pandas
import platform
import os
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

        while self.ask_question():
            continue


    def ask_question(self):
        self.quiz.next_question()
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
            print(Fore.WHITE + "Incorrect: " + Fore.RED + self.quiz.answer)
        print(Fore.WHITE)

        return True

