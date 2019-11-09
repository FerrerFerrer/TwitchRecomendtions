#Main program - User Interface
import sys
from mBD import mockBD
from mBolt import mockBolt

#Global setting variables
MOTHER_PATH = "saves\{}.txt" #Static path name to save options for later
DEPTH = 1 #How many layers it is going to calculate (op -> follower -> follower) for today only 1 layer deep
C_ACTIVITY = False #Compute and ponder based on the channel activity
LIMIT_RECOMENDATIONS = 5 #How many channels its going to calculate; -1 for all
AVOID_BLOCKED = True #Avoid blocked channels to recomendations (blocked and double recomendations)
DEBUG = True #If true, then print debug information to console

coneccion_bd = mockBD("123")
workingbolt = mockBolt()

def getOptions():
    return """
    1. Load Options
    2. Save Options
    3. Add channel
    4. Remove channel
    5. Block channel
    6. Calculate
    7. Get Recomendations
    0. Quit"""

def takeAction():
    errors = 0
    ret = -1
    while(ret is -1):
        try:
            c = int(input("> "))
            if c <= -1 or c >= 8:
                print("Out of bounds!")
                c = -1
            ret = c
        except:
            print("Please only numbers!")
    return c

def doAction(comand):
    global ls_channel
    if comand is 0:
        print("Goodbye!")
        sys.exit()
    elif comand is 1:
        workingbolt.ls_channel = coneccion_bd.get_list()
    elif comand is 2:
        coneccion_bd.save_list(workingbolt.ls_channel)
    elif comand is 3:
        workingbolt.addChanel("123")
    elif comand is 4:
        workingbolt.removeChanel("123")
    elif comand is 5:
        workingbolt.blockChanel("123")
    elif comand is 6:
        workingbolt.calculate()
    elif comand is 7:
        workingbolt.printRecomendations()
    else:
        print("Some error occured")

def main():
    print(getOptions())
    while(True):
        com = takeAction()
        doAction(com)

if __name__ == '__main__':
    main()
