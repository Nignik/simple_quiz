import random
import importlib.util
import sys
spec = importlib.util.spec_from_file_location("czaswoniki", "tests/niemiecki_czasowniki.py")
test = importlib.util.module_from_spec(spec)
sys.modules["czasowniki"] = test
spec.loader.exec_module(test)
czasowniki = test.czasowniki.copy()

def get_question():
    question = random.choice(list(czasowniki.keys()))
    return question

def get_answer(question):
    answer = czasowniki[question]
    return answer

def get_input(question):
    user_input = input(f"{question}: ")
    return user_input

def check(input, answer):
    return input == answer

def print_good():
    print("Odpowiedz poprawna")
    
def print_bad(answer):
    print(f"Odpowiedz bledna, prawidlowa odpowiedz to: {answer}")


def main():
    global czasowniki
    
    while True:
        question = get_question()
        answer = get_answer(question)
        user_input = get_input(question)
        
        if check(user_input, answer):
            print_good()
            del czasowniki[question]
            if len(czasowniki) == 0:
                czasowniki = test.czasowniki.copy()
        else:
            print_bad(answer)
        
    

if __name__ == "__main__":
    main()