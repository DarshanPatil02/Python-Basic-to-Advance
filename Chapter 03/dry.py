# In the world of software development, maintaining clean, efficient, and manageable code is crucial. One fundamental principle that aids in achieving this goal is DRY, which stands for “Don't Repeat Yourself.” DRY is a software development principle that promotes code reusability, maintainability, and readability.

import random
winning_number=random.randint(1,100)
game_over=False
number=int(input("Enter number between 1 to 100: "))
guess=1

while not game_over:
    if number==winning_number:
        print(f"You win and you guessed this number in {guess} times")
        game_over=True
    else:
        if number<winning_number:
            print("too low")
        else:
            print("too high")
        guess+=1
        number=int(input("Guess again: "))
        # DRY -> Don't Repeate Yourself
