from .abs.absBolt import AbstactBolt
from classes import channel

class mockBolt(AbstactBolt):
        def __init__(self, api, basedatos):
            super().__init__(basedatos)
            self.api = api
            self.ls_recomendated = []

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

        def calculate(self):
            print("Calculating")

        def printRecomendations(self):
            print("This are your recomendations!")

        def get_index_in_list(self, name):
            idx = -1
            #for r in range(len())

        def get_session(self):
            pass

        def save_session(self):
            pass

        ####################
        ##  Ponderations  ##
        ####################
        def ponderByUnionOfChannels(self):
            rep = {}
            for channel in channels:
                ## FIXME:
                #multiplyer = ponderByFollowers(channel)
                #multiplyer = len()
                multiplyer = random.random() + 1
                for subchannel in channel: #channel.getFollowers():
                    if subchannel in rep.keys():
                        rep[subchannel] += multiplyer
                    else:
                        rep[subchannel] = multiplyer

            ls = [ [k,v] for k, v in rep.items() ]
            ls = sorted(ls, key = lambda x: x[1], reverse = True)
            return ls[:10]
