#Main program - User Interface

#Global variables
ls_channel = [] #List to saves the user fav channels
ls_blocked_channels = [] #Try not to recomendate this channel

MOTHER_PATH = "saves\{}.txt" #Static path name to save options for later
DEPTH = 1 #How many layers it is going to calculate (op -> follower -> follower) for today only 1 layer deep
C_ACTIVITY = False #Compute and ponder based on the channel activity
LIMIT_RECOMENDATIONS = 5 #How many channels its going to calculate
AVOID_BLOCKED = False #Avoid blocked channels to recomendations (blocked and double recomendations)

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
    pass

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
