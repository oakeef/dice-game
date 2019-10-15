__author__ = 'w0174181'
#importing randint from random
from random import randint

#amount of dice we are working with, could change to any number
number_of_dice = 5

#create 5 random generated numbers
#create array of 5 randomly generated numbers
#function called getRandom that grabs a specified length
def getDice():
    #returning an array of random numbers from 1 to 6
    #range is 0 to whatever length we put in to it via number_of_dice
    return [randint(1, 6) for p in range(0, number_of_dice)]

#Test the dice
#this function sorts the dice array then check numbers in the array to find what combination it has
#starts from the best at the top and works its way down
def test(dice):
    dice.sort()
    if all(x == dice[0] for x in dice):
        return "Five of kind! (definitely not YAHTZEE)"
    if dice[0] == dice[1] == dice[2] and dice[3] == dice[4] or dice[0] == dice[1] and dice[2] == dice[3] == dice[4]:
        return "Full House!"
    if dice[1] == (dice[0] + 1) and dice[2] == (dice[1] + 1) and dice[3] == (dice[2] + 1) and dice[4] == (dice[3] + 1):
        return "Large Straight!"
    if dice[1] == (dice[0] + 1) and dice[2] == (dice[1] + 1) and dice[3] == (dice[2] + 1) or dice[2] == (dice[1] + 1) and dice[3] == (dice[2] + 1) and dice[4] == (dice[3] + 1):
        return "Small Straight!"
    if dice[0] == dice[1] == dice[2] and dice[3] or dice[1] == dice[2] == dice[3] and dice[4]:
        return "Four of a Kind!"
    if dice[0] == dice[1] == dice[2] or dice[1] == dice[2] == dice[3] or dice[2] == dice[3] == dice[4]:
        return "Three of a Kind!"
    if dice[0] == dice[1] and dice[2] == dice[3] or dice[0] == dice[1] and dice[3] == dice[4] or dice[1] == dice[2] and dice[3] == dice[4]:
        return "Two Pair!"
    if dice[0] == dice[1] or dice[1] == dice[2] or dice[2] == dice[3] or dice[3] == dice[4]:
        return "One Pair!"
    else:
        return "No Combo :("

#dice is the variable that stores the dice we generated
dice = getDice()

#output dice
print("Dice 1: ", dice[0])
print("Dice 2: ", dice[1])
print("Dice 3: ", dice[2])
print("Dice 4: ", dice[3])
print("Dice 5: ", dice[4])

#output best combination
print("Highest Combination: ", test(dice))

