from abs.absBolt import AbstactBolt

class mockBolt(AbstactBolt):
        def __init__(self):
            super().__init__()

        def addChanel(self, channel):
            print("Adding...", channel)

        def removeChanel(self, channel):
            print("Removing...", channel)

        def blockChanel(self, channel):
            print("Blocking...", channel)

        def calculate(self):
            print("Calculating")

        def printRecomendations(self):
            print("This are your recomendations!")
