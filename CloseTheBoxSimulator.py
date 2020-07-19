import random

theBox = [False, False, False, False, False, False, False, False, False, False, False, False]
# represents the Box, with 12
dieA = 0
dieB = 0
dieSum = 0
gamesWon = 0
gamesLost = 0
gamesToPlay = 1000  # how many time to play the game
gamesToLose = 100

def reset_the_box(thebox):
    thebox.clear()
    for x in range(12):
        thebox.append(False)
    # print('**********Resetting The Box*************')
    # print(thebox)
    # print(theBox)
def cover_numbers(a, b, thebox):
    #  take input Dice values, enter them into a list, and sort them!
    inputs = [a, b]
    inputs.sort(reverse=True)
    print(inputs)
    #  Check to see if a Double Value is present and cover up that value
    if inputs[0] == inputs[1]:
        # if the Summed number is uncovered, pick it
        if not(thebox[(inputs[0] + inputs[1])-1]):
            thebox[(inputs[0] + inputs[1])-1] = True
            print('covered the summed double number: ' + str(inputs[0] + inputs[1]))
            print(thebox)
            return True
        # if the Hard number is uncovered, pick it
        elif not(thebox[inputs[0]-1]):
            thebox[inputs[0]-1] = True
            print('covered the hard number: ' + str(inputs[0]))
            print(thebox)
            return True
        else:
            print('Hard double not available. Nothing Covered. Rolling Dice again.')
            print(thebox)
            return False
    #  Iterate through the given Dice values
    while inputs[0] > 0:
        # print('inputs: ' + str(inputs[0]) + ' ' + str(inputs[1]))
        # if the summed number is free, cover it.
        if not(thebox[(inputs[0] + inputs[1])-1]):
            thebox[(inputs[0] + inputs[1])-1] = True
            print('covered the summed (not hard) number: ' + str(inputs[0] + inputs[1]))
            print(thebox)
            return True
        # if the individual numbers, or componenents are free, cover it
        elif not(thebox[inputs[0]-1]) and not(thebox[inputs[1]-1]):
            thebox[inputs[0]-1] = True
            thebox[inputs[1]-1] = True
            print('covered individuals numbers: ' + str(inputs[0]) + ' and: ' + str(inputs[1]))
            print(thebox)
            return True
            print('should not reach here')
        else:
            inputs[0] -= 1
            inputs[1] += 1
            print('Trying next combination of numbers')
            print(thebox)
    print(thebox)
    return False

def all_numbers_covered(thebox):
    sumbool = 0
    sumbool = sum(thebox)
    if sumbool < 12:
        print('Sum of Booleans: ' + str(sumbool))
        return False
    else:
        print('all numbers covered')
        #  print('Sum: ' + str(sumbool))
        return True


"""
print(cover_numbers(6,6,theBox))
print(theBox)
print(cover_numbers(6,5,theBox))
print(theBox)
print(cover_numbers(6,5,theBox))
print(theBox)
print(cover_numbers(6,5,theBox))
print(theBox)
print(cover_numbers(6,5,theBox))
print(theBox)
print(cover_numbers(6,5,theBox))
print(theBox)
print(cover_numbers(6,5,theBox))
print(theBox)
print(cover_numbers(6,6,theBox))
print(theBox)
"""
reset_the_box(theBox)

# gamesToPlay = int(input('How many games to play: '))
for x in range(gamesToPlay):
    counter = 1
    while True:
        dieA = random.randint(1,6)
        dieB = random.randint(1,6)
        # dieA = int(input('Enter Die 1 value: '))
        # dieB = int(input('Enter Die 2 value: '))
        if not(cover_numbers(dieA, dieB, theBox)):
            print("Could not cover more numbers. Game Over")
            gamesLost += 1
            reset_the_box(theBox)
            if sum(theBox) > 0:
                print('The box was not reset!!')
            counter = 1
            break
        elif all_numbers_covered(theBox):
            print("Game won!!")
            gamesWon += 1
            reset_the_box(theBox)
            if sum(theBox) > 0:
                print('The box was not reset!!')
            counter = 1
            break
        else:
            counter += 1

print('Games Won: ' + str(gamesWon))
print('Games Lost: ' + str(gamesLost))







