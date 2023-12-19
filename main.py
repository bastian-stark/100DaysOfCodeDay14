# Higher Lower Game App

import functions

# Intro
print('Welcome to the Higher Lower Game! ')
gameState = True
# Begin game loop
while gameState == True:
    already_used = [""]
    score = 0
    gameLoop = True
    # Pick first person
    person1 = functions.pick_name(already_used)
    already_used.append(person1)
    # Begin round loop
    while gameLoop == True:
        # Pick second person and ensure second person is not the same as first person
        person2 = functions.pick_name(already_used)
        if person1['name'] == person2['name']:
            while person1['name'] == person2['name']:
                person2 = functions.pick_name(already_used)
        already_used.append(person2)
        # Display the comparison for user
        functions.display_comparison(person1, person2)
        # Ask user for a guess
        userGuess = input('Who has more followers? Type "A" or "B": ').upper()
        # Update score
        newScore = score
        score = functions.higher_lower_comparison(person1, person2, userGuess, score)
        # Check if user lost
        if newScore == score:
            print('You lose...')
            cont = input('Would you like to play again? ("Y"/"N"): ').lower()
            if cont == "n":
                # Ends game
                gameState = False
                gameLoop = False
            else:
                # Begin new game
                print('Beginning new game...')
        # Uses person2 as person 1 for next round
        else:
            person1 = person2
            continue
print('Game Over...')