__author__ = 'w0174181'
#importing randint from random
from random import randint

#possible dice combos
five_of_a_kind = 1
full_house = 2
large_straight = 3
small_straight = 4
four_of_a_kind = 5
three_of_a_kind = 6
two_pair = 7
one_pair = 8
no_combo = 9

#amount of dice we are working with, could change to any number
number_of_dice = 5

#create 5 random generated numbers
#create array of 5 randomly generated numbers
#function called getRandom that grabs a specified length
def getDice():
    #returning an array of random numbers from 1 to 6
    #range is 0 to whatever length we put in to it via number_of_dice
    return [randint(1, 6) for p in range(0, number_of_dice)]

#find best combination
#made a function full of functions that look for best combination
def getHighestCombination(dice):
    #organize array in numerical order
    dice.sort()
    if five_of_a_kind(dice):
        return five_of_a_kind
    if full_house(dice):
        return full_house
    if large_straight(dice):
        return large_straight
    if small_straight(dice):
        return small_straight
    if four_of_a_kind(dice):
        return four_of_a_kind
    if three_of_a_kind(dice):
        return three_of_a_kind
    if two_pair(dice):
        return two_pair
    if one_pair(dice):
        return one_pair
    return no_combo

#after I organized dice in numberical order it was easier to find specific sets
#these functions check numbers in the array to find what combination it has
#starts from the best at the top and works its way down
def five_of_a_kind(dice):
    if dice[0] == dice[1] == dice[2] == dice[3] == dice [4]:
        return True
    return False

def full_house(dice):
    if dice[0] == dice[1] == dice[2] and dice[3] == dice[4]:
        return True
    if dice[0] == dice[1] and dice[2] == dice[3] == dice[4]:
        return True
    return False

def large_straight(dice):
    if dice[1] == (dice[0] + 1) and dice[2] == (dice[1] + 1) and dice[3] == (dice[2] + 1) and dice[4] == (dice[3] + 1):
        return True
    return False

def small_straight(dice):
    if dice[1] == (dice[0] + 1) and dice[2] == (dice[1] + 1) and dice[3] == (dice[2] + 1):
        return True
    if dice[2] == (dice[1] + 1) and dice[3] == (dice[2] + 1) and dice[4] == (dice[3] + 1):
        return True

def four_of_a_kind(dice):
    if dice[0] == dice[1] == dice[2] and dice[3]:
        return True
    if dice[1] == dice[2] == dice[3] and dice[4]:
        return True
    return False

def three_of_a_kind(dice):
    if dice[0] == dice[1] == dice[2]:
        return True
    if dice[1] == dice[2] == dice[3]:
        return True
    if dice[2] == dice[3] == dice[4]:
        return True
    return False

def two_pair(dice):
    if dice[0] == dice[1] and dice[2] == dice[3]:
        return True
    if dice[0] == dice[1] and dice[3] == dice[4]:
        return True
    if dice[1] == dice[2] and dice[3] == dice[4]:
        return True
    return False

def one_pair(dice):
    if dice[0] == dice[1]:
        return True
    if dice[1] == dice[2]:
        return True
    if dice[2] == dice[3]:
        return True
    if dice[3] == dice[4]:
        return True


#dice is the variable that stores the dice we generated
dice = getDice()

#output dice
print("Dice 1: ", dice[0])
print("Dice 2: ", dice[1])
print("Dice 3: ", dice[2])
print("Dice 4: ", dice[3])
print("Dice 5: ", dice[4])

#output best combination
hand = getHighestCombination(dice)
if hand == five_of_a_kind:
    print("Highest Combination: Five of kind! (definitely not YAHTZEE)")
if hand == full_house:
    print("Highest Combination: Full House!")
if hand == large_straight:
    print("Highest Combination: Large Straight!")
if hand == small_straight:
    print("Highest Combination: Small Straight!")
if hand == four_of_a_kind:
    print("Highest Combination: Four of a Kind!")
if hand == three_of_a_kind:
    print("Highest Combination: Three of a Kind!")
if hand == two_pair:
    print("Highest Combination: Two Pair!")
if hand == one_pair:
    print("Highest Combination: One Pair!")
if hand == no_combo:
    print("Highest Combination: No Combo :(")


