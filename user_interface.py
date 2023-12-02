import os
from colorama import init, Fore
def show_commands():
    print("""
    "reset": resets both score and answered questions
    "menu": goes to menu
    "(quiz name)": starts quiz of name (quiz name)
    """)

def menu():
    directory = os.getcwd() + "\\tests"

    print()
    for file in os.listdir(directory):
        if file.split(".")[-1] == "csv":
            print(Fore.YELLOW + file + Fore.WHITE)
    print()
