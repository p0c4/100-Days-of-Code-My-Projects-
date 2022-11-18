import random
from art import logo
from art import vs
from game_data import data
import os


def dictionary_value():
    dic_A = random.choice(data)
    dic_B = random.choice(data)
    while dic_A["name"] == dic_B["name"]:
        dic_B = random.choice(data)
    return dic_A, dic_B


def ask_question(dic_A, dic_B):
    print(f"""Compare A: {dic_A["name"]}, {dic_A["description"]}, from {dic_A["country"]}""")
    print(vs)
    print(f"""Against B: {dic_B["name"]}, {dic_B["description"]}, from {dic_B["country"]}""")
    answer = (input("Type 'A' or 'B':  ")).lower()
    return answer


def check_answer(dic_A, dic_B, answer):
    if (answer == "a" and dic_A["follower_count"] > dic_B["follower_count"]) or (
            answer == "b" and dic_B["follower_count"] > dic_A["follower_count"]):
        guess = 1
    else:
        guess = 0
    return guess


def game():
    score = 0
    is_game = True
    guess = 1
    print(logo)
    while is_game:
        dic_A, dic_B = dictionary_value()
        answer = ask_question(dic_A, dic_B)
        guess = check_answer(dic_A, dic_B, answer)
        os.system("clear")
        print(logo)
        if guess == 1:
            score += 1
            print(f"You are right! Your score is {score}")
        else:
            os.system("clear")
            print(f"Game Over! Your final score is {score}")
            is_continue = input("Do you want to continue? 'y' or 'n' :")
            if is_continue == "y":
                score = 0
            else:
                is_game = False


game()
