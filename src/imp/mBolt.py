from .abs.absBolt import AbstactBolt
from channel import Channel


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

        def get_index_in_list(self, id, ls):
            for r in range(len(ls)):
                ls_in = ls[r].id
                if ls_in is id:
                    return r
            return -1

        def get_session(self):
            pass

        def save_session(self):
            pass

        ####################
        ##  Ponderations  ##
        ####################
        def ponderByFollowers(number):
            if number < 100:
                return 10.0
            elif number < 1000:
                return 15.0
            elif number < 5000:
                return 18.0
            elif number < 10000:
                return 20.0
            elif number < 50000:
                return 30.0
            elif number < 100000:
                return 40.0
            elif number < 1000000:
                return 50.0
            else:
                return 70.0

        def ponderByUnionOfChannels(self):
            self.ls_recomendated = []           #Reseting list...
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
