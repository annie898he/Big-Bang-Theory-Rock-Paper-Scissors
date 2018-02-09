######################################################################
#TODO: Author: Annie He
#TODO: username: hea
#
# Assignment: A2
# Purpose: As a class assignment to show use of nested if statements
# using multiple elif keywords
######################################################################
# Acknowledgements:
#   This program utilizes inspiration for the timey... wimey stuff
#   Assistance from Jan Pearce for outline and terminology for this program
######################################################################
import time          # import a library with time.sleep()
import random        # import a library with random.choice()
print('')           # This prints a blank line
print('Welcome! \nYou are about to play a game with the computer. \nGood luck! ')
# This is how to ask for input from the keyboard:
myinput = raw_input('Choose rock, paper, scissors, spock, or lizard. ')

print('Your choice is ' + myinput + '!')
time.sleep(.5)
print('')

# This is to assign variable for the computer's random choice
choice1 = 'My choice is rock!'
choice2 = 'I chose paper!'
choice3 = 'I chose scissors!'
choice4 = 'My choice is spock!'
choice5 = 'I chose lizard!'

c_choice = random.choice([choice1, choice2, choice3, choice4, choice5])

if myinput == 'rock' or myinput == 'paper' or myinput == 'scissors' or myinput == 'spock' or myinput == 'lizard':
#These if statements only run if one of the above choices were chosen
    print(c_choice)
    time.sleep(.5)
    #If player decides to enter rock
    if myinput == 'rock' and c_choice == choice1:
        print("It's a tie! \nPress F5 to play again and see who will win.")
    elif myinput == 'rock' and c_choice == choice2:
        print("Paper covers rock. Better luck next time. \nPress F5 to try again.")
    elif myinput == 'rock' and c_choice == choice3:
        print('Rock crushes scissors! You win! Congrats! \nPress F5 to play again and give me another chance.')
    elif myinput == 'rock' and c_choice == choice4:
        print('I chose Spock and Spock vaporizes rock. Sorry! \nPress F5 to try again.')
    elif myinput == 'rock' and c_choice == choice5:
        print('Rock crushes lizard! Good choice! \nPress F5 to play again.')
    
    #If player decides to enter paper
    if myinput == 'paper' and c_choice == choice1:
        print("You win! Paper covers rock! \nPress F5 to play again so that I have another chance.")
    elif myinput == 'paper' and c_choice == choice2:
        print("It's a tie! \nPress F5 to play again and see who will win.")
    elif myinput == 'paper' and c_choice == choice3:
        print('Snip, snip. Scissors cut paper. \nBetter luck next time! \nPress F5 to play again.')
    elif myinput == 'paper' and c_choice == choice4:
        print('Paper disproves Spock. Good choice! \nPress F5 to try again.')
    elif myinput == 'paper' and c_choice == choice5:
        print('Lizard eats paper! Sorry! \nPress F5 to try again.')
    
    #If player decides to enter scissors    
    if myinput == 'scissors' and c_choice == choice1:
        print("Rock crushes scissors. Sorry! \nTry again by clicking F5 to start a new game.")
    elif myinput == 'scissors' and c_choice == choice2:
        print("Scissors cut paper. Good job! \nPress F5 so that I have another chance.")
    elif myinput == 'scissors' and c_choice == choice3:
        print ("What are the odds? It's a tie! \nPress F5 to play again and see who wins.")
    elif myinput == 'scissors' and c_choice == choice4:
        print('I chose spock and spock smashes scissors. Better luck next time. \nPress F5 to try again.')
    elif myinput == 'scissors' and c_choice == choice5:
        print('Scissors decapitate lizard! Ouch! Good choice! \nPress F5 so I can try again.')  
    
    #If player decides to enter spock
    if myinput == 'spock' and c_choice == choice1:
        print("You win! Spock vaporizes rock! \nPress F5 to play again so that I have another chance.")
    elif myinput == 'spock' and c_choice == choice2:
        print("Paper disproves Spock. Sorry! \nPress F5 to try again.")
    elif myinput == 'spock' and c_choice == choice3:
        print('Spock smashes scissors! Good job! \nPress F5 to play again.')
    elif myinput == 'spock' and c_choice == choice4:
        print ("It's a tie! \nPress F5 and see who wins the next round.")
    elif myinput == 'spock' and c_choice == choice5:
        print('Lizard poisons Spock! Sorry! \nPress F5 to play again.')
    
    #If player decides to enter lizard
    if myinput == 'lizard' and c_choice == choice1:
        print("Rock crushes lizard. Better luck next time! \nPress F5 to play again.")
    elif myinput == 'lizard' and c_choice == choice2:
        print("Lizard eats paper. Good choice! \nPress F5 so I can try again.")
    elif myinput == 'lizard' and c_choice == choice3:
        print('Scissors decapitate lizard. Sorry! \nTry again by clicking F5 to start a new game.')
    elif myinput == 'lizard' and c_choice == choice4:
        print ("Lizard poisons Spock! You win! \nPress F5 to play again.")
    elif myinput == 'lizard' and c_choice == choice5:
        print('Lizard vs. Lizard. We tied! \nPress F5 to play again.')
   
#This is only for answers that are not rock, paper, scissors, spock, or lizard
else:
    print('Thanks for your answer, but ' + myinput + "? That's new. Maybe try an answer that I recognize.")
    
    