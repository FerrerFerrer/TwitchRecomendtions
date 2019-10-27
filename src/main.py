#Main program - User Interface

#Global variables
ls_channel = [] #List to saves the user fav channels

MOTHER_PATH = "saves\{}.txt" #Static path name to save options for later
DEPTH = 1 #How many layers it is going to calculate (op -> follower -> follower) for today only 1 layer deep
C_ACTIVITY = False #Compute and ponder based on the channel activity
LIMIT_RECOMENDATIONS = 5 #How many channels its going to calculate; -1 for all
AVOID_BLOCKED = True #Avoid blocked channels to recomendations (blocked and double recomendations)

#Add a channel locally
def addFollower(channel):
    pass

#Reomve a channel locally
def removeFollower(channel):
    pass

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
    pass

def doAction(comand):
    pass

def main():
    print(getOptions())
    # static_sim = "saves\{}.txt"
    # ls_channel.append("Prueba")
    # t = 0
    # with open(static_sim.format("prueba"), "wb") as temp_path:
    #     pickle.dump(ls_channel, temp_path)
    #
    # with open("saves\prueba.txt", "rb") as temp_path:
    #     t = pickle.load(temp_path)
    #
    # print(t)
    pass

if __name__ == '__main__':
    main()
