# Functions for use in main

import game_data
import random

def pick_name(already_used):
    """Picks a name from the game_data file"""
    n = random.randint(0, len(game_data.data) - 1)
    for item in already_used:
        if game_data.data[n]['name'] == item:
            pick_name(already_used)
        else:
            return game_data.data[n]

def display_comparison(person1, person2):
    """Displays the first person and their follower count and just the second person"""
    print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}, with {person1['follower_count']} followers")
    print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")

def higher_lower_comparison(person1, person2, userGuess, score):
    """Checks if user response is correct and displays score"""
    if userGuess == 'A' and person1['follower_count'] > person2['follower_count']:
        score += 1
        print(f'Correct! Your score is {score}')
    elif userGuess == 'B' and person1['follower_count'] < person2['follower_count']:
        score += 1
        print(f'Correct! Your score is {score}')
    elif userGuess == 'A' and person1['follower_count'] < person2['follower_count']:
        print(f'Incorrect! Your final score was {score}')
    elif userGuess == 'B' and person1['follower_count'] > person2['follower_count']:
        print(f'Incorrect! Your final score was {score}')
    elif userGuess != 'A' and userGuess != 'B':
        print('Invalid response, please try again. ')
        higher_lower_comparison(person1, person2, userGuess, score)
    else:
        print('Error.')
    return score