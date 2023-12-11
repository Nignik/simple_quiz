import os
import platform
from colorama import init, Fore


def clear_console():
    if 'PYCHARM_HOSTED' in os.environ:
        print('\n')
    else:
        match platform.system():
            case "Windows":
                os.system("cls")
            case "Linux":
                os.system("clear")

def show_commands():
    print("""
    "reset": resets both score and answered questions
    "menu": goes to menu
    "(quiz name)": starts quiz of name (quiz name)
    """)

def choose_mode():
    print(Fore.CYAN + "choose game mode" + Fore.WHITE)
    print(Fore.YELLOW + """
    1: non_repeat_mode
    2: double_question_mode
    """ + Fore.WHITE)

    return input()

def choose_quiz():
    directory = os.getcwd() + "\\tests"

    print(Fore.CYAN + "What quiz would you like to play?" + Fore.WHITE)

    print()
    for file in os.listdir(directory):
        if file.split(".")[-1] == "csv":
            print(Fore.YELLOW + file + Fore.WHITE)
    print()

    return input()

def print_correct(answer):
    print(Fore.WHITE + "correct: " + Fore.GREEN + answer + Fore.WHITE)
    print(Fore.WHITE + "answer:  " + Fore.GREEN + answer + Fore.WHITE)

def print_incorrect(user_answer, correct_answer):
    print(Fore.WHITE + "correct: " + Fore.GREEN + correct_answer + Fore.WHITE)
    print(Fore.WHITE + "answer:  " + Fore.RED + user_answer + Fore.WHITE)

def ask_question(question):
    print(Fore.CYAN + question + Fore.WHITE)

def take_input():
    user_input = input()

    match user_input:
        case "quit":
            return False
        case _:
            clear_console()
            return user_input