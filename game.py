import os
import random

def init():
    import time 
    os.system("clear")
    global name
    name = ""
    name = raw_input("What is your name ? : ")
    print "Hello " + name + ", Nice to meet you !\n\n" + "WELCOME TO BLACK JACK GAME\n\n"
    time.sleep(2)
    

def game():
    os.system("clear")
    ComputerHand = deal()
    PlayerHand = deal()

    print "------------------------START GAME--------------------------"
    print "Computer Hand: " + str(ComputerHand[0])
    print name + " Hand: " + str(PlayerHand)

    print "\n----------------------CURRENT SCORE------------------------"
    if(ComputeScore(PlayerHand) == 21) :
        print "21 ! You Win !"
        message()
    elif(ComputeScore(ComputerHand) == 21):
        print "21 ! Computer Wins !"
        message()
    print name + " Score: " + str(ComputeScore(PlayerHand))
    CardHit = raw_input("Do you want to hit (Y/N) : ")
    while (CardHit == "y" or CardHit == "Y"):
        hit(PlayerHand)

        print "\n----------------------NEW HAND SCORE------------------------"
        print name + " Hand: " + str(PlayerHand)
        print name + " Score: " + str(ComputeScore(PlayerHand))
        print "Computer Hand: " + str(ComputerHand)
        print "Computer Score: " + str(ComputeScore(ComputerHand))
        if (len(PlayerHand) == 5 and ComputeScore(PlayerHand) < 21) :
            print "Less than 5 and Under 21 : YOU WIN "
            message()
        elif(bust(PlayerHand) == 1):
            print "BUST. YOU LOSE"
            message()
        else:
            CardHit = raw_input("Do you want to hit (Y/N) : ")

    print "\n----------------------COMPUTER TURN------------------------"
    if (computerStrategy(ComputerHand) == "Hit"):
        hit(ComputerHand)
        print "Computer Hand: " + str(ComputerHand)
        print "Computer Score: " + str(ComputeScore(ComputerHand))
        
    else:
        print "I'm done."
        print "Computer Hand: " + str(ComputerHand)
        print "Computer Score: " + str(ComputeScore(ComputerHand))

    print "\n----------------------DETERMINE WINNER------------------------"
    print "COMPUTER: " + str(ComputeScore(ComputerHand))
    print name + " : " + str(ComputeScore(PlayerHand))

    if (winner(ComputerHand, PlayerHand) == "hand1" and bust(ComputerHand) == 0):
        print "Computer Won."
    if (winner(ComputerHand, PlayerHand) == "hand2" and bust(PlayerHand) == 1):
        print "Computer Won."
    if (winner(ComputerHand, PlayerHand) == "hand1" and bust(ComputerHand) == 1):
        print name + " Won."
    if (winner(ComputerHand, PlayerHand) == "hand2" and bust(PlayerHand) == 0):
        print name + " Won."
    message()

def message():
    again = raw_input("Do you want to play again ? (Y/N) : ")
    if (again == "Y" or again == "y"):
        game()
    else:
        print "\n\n-------Thank you for playing!--------\n\n"
        exit()
   
def deal():
    random1 = random.randint(2,14)
    random2 = random.randint(2,14)

    if (random1 == 11):random1 = "J"
    if (random1 == 12):random1 = "Q"
    if (random1 == 13):random1 = "K"
    if (random1 == 14):random1 = "A"

    if (random2 == 11):random2 = "J"
    if (random2 == 12):random2 = "Q"
    if (random2 == 13):random2 = "K"
    if (random2 == 14):random2 = "A"
    
    hand = [random1, random2]
    return hand

def ComputeScore(hand):
    total = 0
    for cards in hand:
        if cards == "J" or cards == "Q" or cards == "K":
            total += 10
        elif cards == "A":
            if total >= 11: total += 1
            else: total += 11
        else:
            total += cards
    return total

def hit(hand):
    newCard = random.randint(2, 14)

    if (newCard == 11):newCard = "J"
    if (newCard == 12):newCard = "Q"
    if (newCard == 13):newCard = "K"
    if (newCard == 14):newCard = "A"

    hand.append(newCard)
    return hand

def computerStrategy(hand):
    strategy = ""
    if (ComputeScore(hand) > 15): strategy = "Stay"
    if (ComputeScore(hand) <= 15): strategy = "Hit"
    return strategy

def winner(hand1, hand2):
    score1 = ComputeScore(hand1)
    score2 = ComputeScore(hand2)

    if score1 > 21: return "hand2"
    if score2 > 21: return "hand1"
    
    if(score1 > score2): return "hand1"
    else: return "hand2"

def bust(hand):
    if (ComputeScore(hand) > 21):
        return 1
    else:
        return 0

init()
game()