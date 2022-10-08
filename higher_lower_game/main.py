from art import logo, vs
from game_data import data
import random

game_continue = True
score = 0

def check_answer(guess,account_a,account_b):
    if account_a > account_b:
        return guess == 'a'
    else:
        return guess == 'b'

B = random.choice(data)

while game_continue:
    print(logo)
    if score !=0:
        print(f"You're right! Current score: {score}.")

    A = B
    B = random.choice(data)
    if A == B:
        B = random.choice(data)

    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")
    
    user_input = input("Who has more followers? Type 'A' or 'B':").lower()

    isCorrect = check_answer(user_input,A['follower_count'],B['follower_count'])
    
    if isCorrect:
        score += 1
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score} ")
