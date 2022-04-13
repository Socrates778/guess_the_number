from random import randrange
import math

lower_bound = int(input("Please enter lower bound: "))
upper_bound = int(input("Please enter upper bound: "))

def guess(lower, upper):
    number = randrange(lower, upper)
    user_guess = math.inf
    i = 0
    while number != user_guess:
        user_guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
        if user_guess < number: 
            i += 1
            print("Your number is lower: ")
        elif user_guess > number:
            i += 1
            print("Your numebr is upper: ")
       
    print('Congrulation, you are correct: ', 'You needed', i+1,' try to guess')


guess(lower_bound, upper_bound)


