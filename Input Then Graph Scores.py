##### Golf Scores
##### Author: David Taylor
##### 03/21/2023
####### Python program that reads names of golfers and their scores using 
####### keyboard input and saves them to two lists respectively.
####### The program then prints a report by going through the information in the lists.


import datetime
import matplotlib.pyplot as plt

def inputInfo():

    golferNames = []
    scores = []
    count = 0

    askUser = input("Are there any golfer cards to input? (y/n) ")

    # loop until input = "n"
    while askUser != "n":
        name = input("Input golfers name: ")
        score = int(input("Input golfers score: "))

        # add inputs to end of lists
        golferNames.append(name)
        scores.append(score)
        count += 1

        askUser = input("Do you have more golfers to enter? (y/n) ")

    return golferNames, scores, count


def displayAll(names, scores):

    # get current date from system
    curDateTime = str(datetime.datetime.now())
    day = curDateTime[8:10]
    month = curDateTime[5:7]
    year = curDateTime[0:4]
    
    sortedScore = []
    sortedName = []
    totalScores = 0
    
    count = len(scores) - 1

    print(f'\n{"SPRINGFORK AMATEUR GOLD CLUB":^40}')
    print(f'{"TOURNAMENT DATE: " + day + " " + month + " " + year:^40}')
    print(f'{"GOLFER NAME":<35}',f'{"SCORE":^5}')
    dash = "-" 
    print(f'{dash*30:<35}', f'{dash*5:<6}')
# sort through lists to find lowest scores
# loop until count = -1
    while count != -1:
        lowScore = scores[count]
        lowName = names[count]

        # iterate through lists by highest index to low
        for x in range(count, -1, -1):
            # store lowest found value
            if lowScore > scores[x]:
                lowScore = scores[x]
                lowName = names[x]
        # add lowest score and name to end of new sorted list       
        sortedScore.append(lowScore)
        sortedName.append(lowName)
        
        # remove lowest current score from list
        scores.remove(lowScore)
        names.remove(lowName)

        #reduce count
        count -= 1
        
# print out sorted scores and names
    for x in range(len(sortedName)):
        print(f'{sortedName[x]:<35}', f'{sortedScore[x]:>5}')

        # add up total scores
        totalScores += sortedScore[x]
    # find average of scores
    avg = totalScores/len(sortedScore)
# print out average  
    print(f'\n{"Average score for all golfers":<30}', f'{avg:>10}')

    # build display bar graph
    plt.barh(sortedName, sortedScore, height = 0.1)
    plt.show()


    return sortedName[0], sortedScore[0]    

def main():
    
    golferNames = []
    golferScores = []
    
    # call inputInfo function
    golferNames, golferScores, numGolfers = inputInfo()

    # call displayAll function
    winnerName, winnerScore = displayAll(golferNames, golferScores)
    
    # print out winner
    print("\nWinner is", winnerName, "with score", winnerScore, "out of", numGolfers, "golfers.")

main()

