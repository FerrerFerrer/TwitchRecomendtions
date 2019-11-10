from abs.absBolt import AbstactBolt
from classes import channel

class mockBolt(AbstactBolt):
        def __init__(self, api, bd):
            super().__init__()
            self.api = api
            self.bd = bd

        def addChanel(self, name):
            self.ls_channel.append(name)
            print("Adding...", name)

        def removeChanel(self, name):
            self.ls_channel.remove(name)
            print("Removing...", name)

        def blockChanel(self, name):
            for x in self.ls_channel:
                t = x.name
                if t is name:
                    x.block(True)
                    return

            print("Blocking...", channel)

        def calculate(self):
            print("Calculating")

        def printRecomendations(self):
            print("This are your recomendations!")

        def get_index_in_list(self, name):
            for
