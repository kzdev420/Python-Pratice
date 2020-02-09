import random

MINIMUM = 0
MAXIMUM = 100
NUMBER = random.randint(MINIMUM, MAXIMUM)
TRY = 0
RUNNING = True
ANSWER = None

while RUNNING:
    print ("Is it %s?" % str(NUMBER))
    ANSWER = input()
    if "no" in ANSWER.lower() and "lower" in ANSWER.lower():
        NUMBER -= random.randint(1, 4)
    elif "no" in ANSWER.lower() and "higher" in ANSWER.lower():
        NUMBER += random.randint(1, 4)
    elif ANSWER.lower() == "no":
        print ("Higher or lower?")
        ANSWER = input()
        if ANSWER.lower() == "higher":
            NUMBER += random.randint(1, 4)
        elif ANSWER.lower() == "lower":
            NUMBER -= random.randint(1, 4)
    elif ANSWER.lower() == "yes":
        if TRY < 2:
            print( "Yes! It only took me %s try!" % str(TRY))
        elif TRY < 2 and TRY < 10:
            print ("Pretty well for a robot, %s tries." % str(TRY))
        else:
            print ("That's so bad, %s tries." % str(TRY))
        RUNNING = False
    TRY += 1
    
print ("Thanks for the game!")



def guess():
    i = 0
    # i is the lowest number in range of possible guess
    j = 100
    # j is the highest number in range of possible guesses
    m = 50
    # m is the middle number in range of possible guesses
    counter = 1
    # counter is the number of guesses take.
    print ("Please guess a number")
    condition = input("Is your guess " + str(m) + "? (0 means it's too low, 1 means it's your guess and 2 means it's too high) ")
    while condition != 1:
        counter += 1
        if condition == 0:
            i = m + 1
        elif condition == 2:
            j = m - 1
        m = (i + j) / 2
        condition = input("Is your guess " + str(m) + "? (0 means it's too low, 1 means it's your guess and 2 means it's too high) ")
    print ("It took" , counter , "times to guess your number")
guess()